"""File writers, orchestration (preprocess_file/batch), and report printing."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from .constants import DEFAULT_NUM_CTX, DEFAULT_REVIEW_BATCH_SIZE
from .ollama import save_debug_file
from .parsing import (
    build_context_for_ids,
    build_context_items,
    parse_document_metadata,
    parse_transcript,
)
from .processing import (
    apply_drop_review,
    apply_keep_review,
    attach_items_to_results,
    build_quality_report,
    is_risky_keep_result,
    process_audit_batch,
    process_initial_batch,
    process_keep_review_batch,
    process_review_batch,
    process_with_retry,
)


# ────────────────────────────────────────────────────────────────
# Main preprocessing flow
# ────────────────────────────────────────────────────────────────


def preprocess_file(
    input_path: Path,
    output_dir: Path | None,
    model: str,
    batch_size: int,
    dry_run: bool = False,
    *,
    timeout: int = 300,
    json_mode: bool = True,
    num_ctx: int = DEFAULT_NUM_CTX,
    debug: bool = False,
    fallback_policy: str = "abort",
    context_window: int = 1,
    review_window: int = 1,
    review_batch_size: int = DEFAULT_REVIEW_BATCH_SIZE,
    skip_drop_review: bool = False,
    skip_keep_review: bool = False,
    audit_sample_size: int = 0,
) -> dict[str, Any]:
    """Preprocess one transcript file end-to-end."""
    print(f"  Processing: {input_path.name}")

    document_metadata = parse_document_metadata(input_path)
    parsed_data = parse_transcript(input_path)
    context_items = build_context_items(parsed_data, window=context_window)

    print(f"    Total sentence units extracted: {len(parsed_data)}")
    print(f"    Rule decisions: 0 | LLM initial candidates: {len(context_items)}")

    debug_dir: Path | None = None
    if debug and output_dir is not None:
        debug_dir = output_dir / "debug_logs" / document_metadata["company_folder"] / document_metadata["document_id"]
        save_debug_file(debug_dir, "document_metadata.json", document_metadata)
        save_debug_file(debug_dir, "parsed_units.json", parsed_data)
        save_debug_file(debug_dir, "context_items.json", context_items)

    # Pass 1: high-recall initial classification.
    initial_results: list[dict[str, Any]] = []
    total_batches = (len(context_items) + batch_size - 1) // batch_size if context_items else 0
    for i in range(0, len(context_items), batch_size):
        batch = context_items[i: i + batch_size]
        batch_num = i // batch_size + 1
        label = f"initial_batch_{batch_num:03d}"
        print(f"    Initial batch {batch_num}/{total_batches} ({len(batch)} items)...", end=" ", flush=True)
        try:
            batch_results = process_with_retry(
                batch, process_initial_batch, model=model, document_metadata=document_metadata,
                timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
                debug_dir=debug_dir, batch_label=label, fallback_policy=fallback_policy,
            )
            print("OK")
        except Exception as exc:
            print("FAILED")
            raise RuntimeError(f"Initial LLM pass failed for {input_path.name}, {label}: {exc}") from exc
        initial_results.extend(batch_results)

    # Pass 2: review only initial DISCARD decisions.
    review_results: list[dict[str, Any]] = []
    if skip_drop_review:
        print("    Drop review pass skipped.")
        final_results = [dict(r, initial_decision=r.get("decision"), initial_reason=r.get("reason"), reviewed=False, rescued=False) for r in initial_results]
    else:
        discard_ids = [r["source_id"] for r in initial_results if r.get("decision") == "DISCARD"]
        review_items = build_context_for_ids(parsed_data, discard_ids, window=review_window)
        print(f"    Drop review candidates: {len(review_items)}")

        review_batches = (len(review_items) + review_batch_size - 1) // review_batch_size if review_items else 0
        for i in range(0, len(review_items), review_batch_size):
            batch = review_items[i: i + review_batch_size]
            batch_num = i // review_batch_size + 1
            label = f"review_batch_{batch_num:03d}"
            print(f"    Review batch {batch_num}/{review_batches} ({len(batch)} items)...", end=" ", flush=True)
            try:
                batch_results = process_with_retry(
                    batch, process_review_batch, model=model, document_metadata=document_metadata,
                    timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
                    debug_dir=debug_dir, batch_label=label, fallback_policy=fallback_policy,
                )
                print("OK")
            except Exception as exc:
                print("FAILED")
                raise RuntimeError(f"Drop review pass failed for {input_path.name}, {label}: {exc}") from exc
            review_results.extend(batch_results)

        final_results = apply_drop_review(initial_results, review_results)

    # Pass 3: review risky kept/rescued/context/metadata-like items.
    keep_review_results: list[dict[str, Any]] = []
    if skip_keep_review:
        print("    Keep review pass skipped.")
    else:
        result_map = {r["source_id"]: r for r in final_results}
        risky_ids = [
            item["source_id"]
            for item in parsed_data
            if item["source_id"] in result_map
            and result_map[item["source_id"]].get("decision") in {"KEEP_FACT", "KEEP_CONTEXT", "MOVE_TO_METADATA"}
            and is_risky_keep_result(result_map[item["source_id"]], item["text"])
        ]
        keep_review_items = build_context_for_ids(parsed_data, risky_ids, window=review_window)
        for item in keep_review_items:
            cur = result_map[item["source_id"]]
            item["current_decision"] = cur.get("decision")
            item["current_reason"] = cur.get("reason")
            item["current_fact_category"] = cur.get("fact_category")
        save_debug_file(debug_dir, "keep_review_candidates.json", keep_review_items)

        keep_review_batches = (len(keep_review_items) + review_batch_size - 1) // review_batch_size if keep_review_items else 0
        print(f"    Risky keep-review candidates: {len(keep_review_items)}")
        for i in range(0, len(keep_review_items), review_batch_size):
            batch = keep_review_items[i: i + review_batch_size]
            batch_num = i // review_batch_size + 1
            label = f"keep_review_batch_{batch_num:03d}"
            print(f"    Keep-review batch {batch_num}/{keep_review_batches} ({len(batch)} items)...", end=" ", flush=True)
            try:
                batch_results = process_with_retry(
                    batch, process_keep_review_batch, model=model, document_metadata=document_metadata,
                    timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
                    debug_dir=debug_dir, batch_label=label, fallback_policy=fallback_policy,
                )
                print("OK")
            except Exception as exc:
                print("FAILED")
                raise RuntimeError(f"Keep review pass failed for {input_path.name}, {label}: {exc}") from exc
            keep_review_results.extend(batch_results)

        final_results = apply_keep_review(final_results, keep_review_results)

    clean_data, drop_data, rescued_data, metadata_data = attach_items_to_results(parsed_data, final_results)

    # Optional audit pass: reporting-only.
    audit_results: list[dict[str, Any]] = []
    if audit_sample_size > 0:
        audit_items = _build_audit_sample(parsed_data, final_results, sample_size=audit_sample_size, window=context_window)
        print(f"    Audit sample size: {len(audit_items)}")
        for i in range(0, len(audit_items), batch_size):
            batch = audit_items[i: i + batch_size]
            batch_num = i // batch_size + 1
            total = (len(audit_items) + batch_size - 1) // batch_size
            label = f"audit_batch_{batch_num:03d}"
            print(f"    Audit batch {batch_num}/{total} ({len(batch)} items)...", end=" ", flush=True)
            try:
                batch_results = process_with_retry(
                    batch, process_audit_batch, model=model, document_metadata=None,
                    timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
                    debug_dir=debug_dir, batch_label=label, fallback_policy=fallback_policy,
                )
                print("OK")
            except Exception as exc:
                print("FAILED")
                raise RuntimeError(f"Audit pass failed for {input_path.name}, {label}: {exc}") from exc
            audit_results.extend(batch_results)

    quality_report = build_quality_report(
        parsed_data=parsed_data, initial_results=initial_results,
        review_results=review_results, final_results=final_results,
        clean_data=clean_data, drop_data=drop_data,
        rescued_data=rescued_data, metadata_data=metadata_data,
        keep_review_results=keep_review_results, audit_results=audit_results,
    )

    clean_text = "\n".join(item["text"] for item in clean_data) + ("\n" if clean_data else "")

    output_path_str: str | None = None
    if not dry_run and output_dir is not None:
        company_dir = input_path.parent.name
        out_company = output_dir / company_dir
        out_company.mkdir(parents=True, exist_ok=True)
        out_file = out_company / input_path.name
        out_file.write_text(clean_text, encoding="utf-8")
        output_path_str = str(out_file)

        drop_dir = output_dir / "drop_logs" / company_dir
        drop_dir.mkdir(parents=True, exist_ok=True)
        stem = input_path.stem

        _write_drop_txt(
            drop_dir / f"{stem}.drop.txt",
            input_path=input_path, parsed_data=parsed_data,
            drop_data=drop_data, rescued_data=rescued_data,
            initial_results=initial_results, final_results=final_results,
            quality_report=quality_report,
        )
        _write_quality_md(
            drop_dir / f"{stem}.quality.md",
            input_path=input_path, quality_report=quality_report,
            rescued_data=rescued_data, drop_data=drop_data,
            audit_results=audit_results,
        )

        analysis_file = drop_dir / f"{stem}.analysis.json"
        analysis_file.write_text(
            json.dumps({
                "document_metadata": document_metadata,
                "initial_analysis_log": initial_results,
                "drop_review_log": review_results,
                "keep_review_log": keep_review_results,
                "final_analysis_log": final_results,
                "audit_log": audit_results,
                "clean_data": clean_data,
                "rescued_data": rescued_data,
                "metadata_data": metadata_data,
                "drop_data": drop_data,
                "quality_report": quality_report,
            }, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

        metadata_dir = output_dir / "metadata" / company_dir
        metadata_dir.mkdir(parents=True, exist_ok=True)
        metadata_file = metadata_dir / f"{stem}.metadata.json"
        metadata_file.write_text(
            json.dumps({"document_metadata": document_metadata, "metadata_data": metadata_data}, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

    return {
        "input_path": str(input_path),
        "output_path": output_path_str,
        "document_metadata": document_metadata,
        "parsed_data": parsed_data,
        "initial_analysis_log": initial_results,
        "drop_review_log": review_results,
        "keep_review_log": keep_review_results,
        "final_analysis_log": final_results,
        "audit_log": audit_results,
        "clean_data": clean_data,
        "rescued_data": rescued_data,
        "metadata_data": metadata_data,
        "drop_data": drop_data,
        "quality_report": quality_report,
        "lines_before": quality_report["sentence_units_before"],
        "lines_after": quality_report["sentence_units_after"],
        "reduction_pct": quality_report["final_reduction_pct"],
        "keep_fact": quality_report["final_keep_fact"],
        "keep_context": quality_report["final_keep_context"],
        "fallback_count": quality_report["fallback_count"],
        "rescued_by_review": quality_report["rescued_by_review"],
        "moved_to_metadata": quality_report["moved_to_metadata"],
        "dropped_by_keep_review": quality_report["dropped_by_keep_review"],
    }


def _build_audit_sample(
    parsed_data: list[dict[str, str]],
    final_results: list[dict[str, Any]],
    *,
    sample_size: int,
    window: int,
) -> list[dict[str, Any]]:
    """Build a deterministic sample for optional LLM audit."""
    contexts = {item["source_id"]: item for item in build_context_items(parsed_data, window=window)}
    final_drops = [r for r in final_results if r.get("decision") == "DISCARD"]
    final_keeps = [r for r in final_results if r.get("decision") in {"KEEP_FACT", "KEEP_CONTEXT"}]

    half = max(1, sample_size // 2)
    selected = final_drops[:half] + final_keeps[: max(0, sample_size - len(final_drops[:half]))]

    audit_items: list[dict[str, Any]] = []
    for r in selected:
        ctx = contexts.get(r["source_id"], {})
        audit_items.append({
            "source_id": r["source_id"],
            "final_decision": r.get("decision"),
            "target": ctx.get("target", ""),
            "context_before": ctx.get("context_before", []),
            "context_after": ctx.get("context_after", []),
            "reason": r.get("reason", ""),
            "fact_category": r.get("fact_category", ""),
        })
    return audit_items


# ────────────────────────────────────────────────────────────────
# File writers
# ────────────────────────────────────────────────────────────────


def _write_drop_txt(
    drop_file: Path,
    *,
    input_path: Path,
    parsed_data: list[dict[str, str]],
    drop_data: list[dict[str, Any]],
    rescued_data: list[dict[str, Any]],
    initial_results: list[dict[str, Any]],
    final_results: list[dict[str, Any]],
    quality_report: dict[str, Any],
) -> None:
    """Write a human-readable drop log."""
    lines = [
        f"=== DROP LOG (LLM-first): {input_path.name} ===",
        f"Source  : {input_path}",
        f"Total sentence units : {quality_report['sentence_units_before']}",
        f"Initial discarded    : {quality_report['initial_discarded']}",
        f"Rescued by review    : {quality_report['rescued_by_review']}",
        f"Final discarded      : {quality_report['final_discarded']}",
        f"Final kept           : {quality_report['sentence_units_after']}",
        f"Final reduction      : {quality_report['final_reduction_pct']}%",
        f"KEEP_FACT            : {quality_report['final_keep_fact']}",
        f"KEEP_CONTEXT         : {quality_report['final_keep_context']}",
        f"Fallback             : {quality_report['fallback_count']}",
        f"Moved to metadata    : {quality_report.get('moved_to_metadata', 0)}",
        f"Dropped by keep-review: {quality_report.get('dropped_by_keep_review', 0)}",
        "",
        "--- Rescued items from initial DISCARD ---",
        "",
    ]

    if not rescued_data:
        lines.extend(["(none)", ""])
    for item in rescued_data:
        lines.append(f"[source_id: {item['source_id']} | line: {item.get('line_id')} | sentence: {item.get('sentence_id')}] [{item.get('fact_category')}] [{item.get('reason')}]")
        lines.append(f"Initial reason: {item.get('initial_reason', '')}")
        lines.append(item["text"])
        lines.append("")

    metadata_items = [r for r in final_results if r.get("decision") == "MOVE_TO_METADATA"]
    lines.extend(["--- Items moved to metadata/conventions ---", ""])
    if not metadata_items:
        lines.extend(["(none)", ""])
    else:
        item_by_id = {x["source_id"]: x for x in parsed_data}
        for r in metadata_items:
            item = item_by_id.get(r["source_id"], {})
            lines.append(f"[source_id: {r['source_id']}] [{r.get('fact_category')}] [{r.get('reason')}]")
            lines.append(item.get("text", ""))
            lines.append("")

    lines.extend(["--- Final discarded sentence units ---", ""])
    for item in drop_data:
        lines.append(f"[source_id: {item['source_id']} | line: {item.get('line_id')} | sentence: {item.get('sentence_id')}] [{item.get('fact_category')}] [{item.get('reason')}]")
        if item.get("reviewed"):
            lines.append(f"Review: {item.get('review_decision', '')} — {item.get('review_reason', '')}")
        lines.append(item["text"])
        lines.append("")

    lines.append("--- Summary by final dropped fact_category ---")
    for category, count in quality_report["final_drop_category_counts"].items():
        lines.append(f"  {category:<30s}: {count:3d}")
    lines.append("")
    lines.append("--- Summary by final kept fact_category ---")
    for category, count in quality_report["final_keep_category_counts"].items():
        lines.append(f"  {category:<30s}: {count:3d}")
    lines.append("")

    drop_file.write_text("\n".join(lines), encoding="utf-8")


def _write_quality_md(
    quality_file: Path,
    *,
    input_path: Path,
    quality_report: dict[str, Any],
    rescued_data: list[dict[str, Any]],
    drop_data: list[dict[str, Any]],
    audit_results: list[dict[str, Any]],
) -> None:
    """Write a compact Markdown quality report."""
    qr = quality_report
    lines = [
        f"# Preprocess Quality Report — {input_path.name}", "",
        "## Core metrics", "",
        f"- Sentence units before: **{qr['sentence_units_before']}**",
        f"- Sentence units after: **{qr['sentence_units_after']}**",
        f"- Final discarded: **{qr['final_discarded']}**",
        f"- Final reduction: **{qr['final_reduction_pct']}%**",
        f"- Retention: **{qr['retention_pct']}%**",
        f"- Rescued by review: **{qr['rescued_by_review']}**",
        f"- Fallback count: **{qr['fallback_count']}**",
        f"- Moved to metadata: **{qr.get('moved_to_metadata', 0)}**",
        f"- Dropped by keep review: **{qr.get('dropped_by_keep_review', 0)}**",
        "", "## Category counts — final keep", "",
    ]
    for category, count in qr["final_keep_category_counts"].items():
        lines.append(f"- `{category}`: {count}")

    lines.extend(["", "## Category counts — final drop", ""])
    for category, count in qr["final_drop_category_counts"].items():
        lines.append(f"- `{category}`: {count}")

    lines.extend(["", "## Rescued examples", ""])
    if not rescued_data:
        lines.append("No rescued items.")
    for item in rescued_data[:20]:
        lines.append(f"- **{item['source_id']}** `{item.get('fact_category')}` — {item.get('text')}")

    lines.extend(["", "## Final dropped examples", ""])
    for item in drop_data[:20]:
        lines.append(f"- **{item['source_id']}** `{item.get('fact_category')}` — {item.get('text')}")

    if audit_results:
        lines.extend(["", "## Optional audit summary", ""])
        for label, count in qr["audit_counts"].items():
            lines.append(f"- `{label}`: {count}")

    quality_file.write_text("\n".join(lines), encoding="utf-8")


# ────────────────────────────────────────────────────────────────
# Directory processing and reporting
# ────────────────────────────────────────────────────────────────


def preprocess_batch_dir(
    input_dir: Path,
    output_dir: Path,
    model: str,
    batch_size: int,
    dry_run: bool = False,
    *,
    timeout: int = 300,
    json_mode: bool = True,
    num_ctx: int = DEFAULT_NUM_CTX,
    debug: bool = False,
    fallback_policy: str = "abort",
    context_window: int = 1,
    review_window: int = 1,
    review_batch_size: int = DEFAULT_REVIEW_BATCH_SIZE,
    skip_drop_review: bool = False,
    skip_keep_review: bool = False,
    audit_sample_size: int = 0,
) -> list[dict[str, Any]]:
    """Process all .txt files under a directory."""
    txt_files = sorted(input_dir.rglob("*.txt"))
    results: list[dict[str, Any]] = []
    errors = 0

    print(f"Found {len(txt_files)} .txt files in {input_dir}\n")

    for txt_file in txt_files:
        try:
            result = preprocess_file(
                txt_file, output_dir, model, batch_size, dry_run,
                timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
                debug=debug, fallback_policy=fallback_policy,
                context_window=context_window, review_window=review_window,
                review_batch_size=review_batch_size,
                skip_drop_review=skip_drop_review, skip_keep_review=skip_keep_review,
                audit_sample_size=audit_sample_size,
            )
            results.append(result)
        except Exception as exc:
            errors += 1
            print(f"  ERROR: {txt_file} — {exc}", file=sys.stderr)
            if fallback_policy == "abort":
                break

    print(f"\nDone: {len(results)} success, {errors} errors")
    return results


def print_file_report(result: dict[str, Any]) -> None:
    """Print concise report for one file."""
    qr = result["quality_report"]
    name = Path(result["input_path"]).name
    print(f"\n{'=' * 78}")
    print(f"  PREPROCESS REPORT: {name}")
    print(f"{'=' * 78}")
    print(f"\n  Summary:")
    print(f"    Sentence units before       : {qr['sentence_units_before']}")
    print(f"    Sentence units after        : {qr['sentence_units_after']}")
    print(f"    Final reduction             : {qr['final_reduction_pct']}%")
    print(f"    KEEP_FACT                   : {qr['final_keep_fact']}")
    print(f"    KEEP_CONTEXT                : {qr['final_keep_context']}")
    print(f"    Fallback decisions          : {qr['fallback_count']}")
    if result["output_path"]:
        print(f"\n  Output: {result['output_path']}")
    else:
        print("\n  (dry-run — no files written)")
    print(f"{'=' * 78}\n")


def print_batch_report(results: list[dict[str, Any]]) -> None:
    """Print aggregate report for batch mode."""
    total_before = sum(r["quality_report"]["sentence_units_before"] for r in results)
    total_after = sum(r["quality_report"]["sentence_units_after"] for r in results)
    avg_reduction = ((total_before - total_after) / total_before * 100) if total_before else 0.0

    print(f"\n{'=' * 78}")
    print("  BATCH PREPROCESS REPORT")
    print(f"{'=' * 78}")
    print(f"  Total files          : {len(results)}")
    print(f"  Items before         : {total_before}")
    print(f"  Items after          : {total_after}")
    print(f"  Total reduction      : {avg_reduction:.1f}%")
    print(f"{'=' * 78}\n")
