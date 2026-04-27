"""LLM batch processing, retry logic, and decision merging."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .constants import (
    AUDIT_PROMPT_TEMPLATE,
    DROP_REVIEW_PROMPT_TEMPLATE,
    INITIAL_PROMPT_TEMPLATE,
    KEEP_REVIEW_PROMPT_TEMPLATE,
)
from .ollama import (
    call_ollama,
    parse_model_json,
    save_debug_file,
    validate_audit_items,
    validate_initial_decisions,
    validate_keep_review_decisions,
    validate_review_decisions,
)


# ────────────────────────────────────────────────────────────────
# LLM processing functions
# ────────────────────────────────────────────────────────────────


def process_initial_batch(
    batch: list[dict[str, Any]],
    model: str,
    document_metadata: dict[str, str],
    *,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
) -> list[dict[str, Any]]:
    """Run pass 1: high-recall initial classification."""
    prompt = INITIAL_PROMPT_TEMPLATE.format(
        document_metadata_json=json.dumps(document_metadata, ensure_ascii=False),
        input_json=json.dumps(batch, ensure_ascii=False, indent=2),
    )
    return _run_prompt_and_validate(
        prompt=prompt, model=model, timeout=timeout, json_mode=json_mode,
        num_ctx=num_ctx, debug_dir=debug_dir, batch_label=batch_label,
        expected_key="decisions", validator=validate_initial_decisions, batch=batch,
    )


def process_review_batch(
    batch: list[dict[str, Any]],
    model: str,
    document_metadata: dict[str, str],
    *,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
) -> list[dict[str, Any]]:
    """Run pass 2: review only initial DISCARD decisions to prevent false drops."""
    prompt = DROP_REVIEW_PROMPT_TEMPLATE.format(
        document_metadata_json=json.dumps(document_metadata, ensure_ascii=False),
        input_json=json.dumps(batch, ensure_ascii=False, indent=2),
    )
    return _run_prompt_and_validate(
        prompt=prompt, model=model, timeout=timeout, json_mode=json_mode,
        num_ctx=num_ctx, debug_dir=debug_dir, batch_label=batch_label,
        expected_key="decisions", validator=validate_review_decisions, batch=batch,
    )


def process_keep_review_batch(
    batch: list[dict[str, Any]],
    model: str,
    document_metadata: dict[str, str],
    *,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
) -> list[dict[str, Any]]:
    """Run pass 3: review risky kept/rescued/metadata-like decisions."""
    prompt = KEEP_REVIEW_PROMPT_TEMPLATE.format(
        document_metadata_json=json.dumps(document_metadata, ensure_ascii=False),
        input_json=json.dumps(batch, ensure_ascii=False, indent=2),
    )
    return _run_prompt_and_validate(
        prompt=prompt, model=model, timeout=timeout, json_mode=json_mode,
        num_ctx=num_ctx, debug_dir=debug_dir, batch_label=batch_label,
        expected_key="decisions", validator=validate_keep_review_decisions, batch=batch,
    )


def process_audit_batch(
    batch: list[dict[str, Any]],
    model: str,
    *,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
) -> list[dict[str, Any]]:
    """Optional audit pass (reporting-only, does not change clean output)."""
    prompt = AUDIT_PROMPT_TEMPLATE.format(input_json=json.dumps(batch, ensure_ascii=False, indent=2))
    return _run_prompt_and_validate(
        prompt=prompt, model=model, timeout=timeout, json_mode=json_mode,
        num_ctx=num_ctx, debug_dir=debug_dir, batch_label=batch_label,
        expected_key="audit", validator=validate_audit_items, batch=batch,
    )


def _run_prompt_and_validate(
    *,
    prompt: str,
    model: str,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
    expected_key: str,
    validator,
    batch: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Shared Ollama prompt execution with debug artifacts and validation."""
    save_debug_file(debug_dir, f"{batch_label}.prompt.txt", prompt)
    try:
        result = call_ollama(prompt, model, timeout, json_mode, num_ctx)
        save_debug_file(debug_dir, f"{batch_label}.payload.json", result["payload"])
        save_debug_file(debug_dir, f"{batch_label}.raw_response.json", result["response"])

        content = result["response"].get("message", {}).get("content", "")
        save_debug_file(debug_dir, f"{batch_label}.model_content.txt", content)

        parsed = parse_model_json(content, expected_key=expected_key)
        validated = validator(parsed, batch)
        save_debug_file(debug_dir, f"{batch_label}.validated.json", validated)
        return validated
    except Exception as exc:
        save_debug_file(debug_dir, f"{batch_label}.error.txt", repr(exc))
        return []


def process_with_retry(
    batch: list[dict[str, Any]],
    processor,
    *,
    model: str,
    document_metadata: dict[str, str] | None = None,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
    debug_dir: Path | None,
    batch_label: str,
    fallback_policy: str,
) -> list[dict[str, Any]]:
    """Run an LLM batch with recursive splitting on failure."""
    kwargs = {
        "model": model, "timeout": timeout, "json_mode": json_mode,
        "num_ctx": num_ctx, "debug_dir": debug_dir, "batch_label": batch_label,
    }
    if document_metadata is not None:
        kwargs["document_metadata"] = document_metadata

    decisions = processor(batch, **kwargs)
    if decisions:
        return decisions

    if len(batch) > 1:
        mid = len(batch) // 2
        left = process_with_retry(
            batch[:mid], processor, model=model, document_metadata=document_metadata,
            timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
            debug_dir=debug_dir, batch_label=f"{batch_label}_a", fallback_policy=fallback_policy,
        )
        right = process_with_retry(
            batch[mid:], processor, model=model, document_metadata=document_metadata,
            timeout=timeout, json_mode=json_mode, num_ctx=num_ctx,
            debug_dir=debug_dir, batch_label=f"{batch_label}_b", fallback_policy=fallback_policy,
        )
        return left + right

    return fallback_decisions(batch, fallback_policy, f"failed single-item batch {batch_label}", processor_name=getattr(processor, "__name__", ""))


def fallback_decisions(batch: list[dict[str, Any]], policy: str, reason: str, processor_name: str = "") -> list[dict[str, Any]]:
    """Create fallback decisions when a single-item batch still fails."""
    if policy == "abort":
        raise RuntimeError(reason)

    if processor_name == "process_review_batch":
        review_decision = "RESCUE_KEEP_CONTEXT" if policy in {"keep", "undecided"} else "CONFIRM_DISCARD"
        return [{"source_id": item["source_id"], "review_decision": review_decision, "reason": f"LLM failed; fallback_policy={policy}; {reason}", "fact_category": "other", "fallback": True} for item in batch]

    if processor_name == "process_keep_review_batch":
        action = "CONFIRM_KEEP" if policy in {"keep", "undecided"} else "DROP_NOISE"
        return [{"source_id": item["source_id"], "keep_review_decision": action, "reason": f"LLM failed; fallback_policy={policy}; {reason}", "fact_category": "other", "fallback": True} for item in batch]

    if policy == "keep":
        decision = "KEEP_CONTEXT"
    elif policy == "discard":
        decision = "DISCARD"
    elif policy == "undecided":
        decision = "KEEP_CONTEXT"
    else:
        raise ValueError(f"Unknown fallback policy: {policy}")

    return [{"source_id": item["source_id"], "decision": decision, "reason": f"LLM failed; fallback_policy={policy}; {reason}", "fact_category": "other", "rule_based": False, "fallback": True} for item in batch]


# ────────────────────────────────────────────────────────────────
# Decision merging
# ────────────────────────────────────────────────────────────────


def is_risky_keep_result(result: dict[str, Any], text: str) -> bool:
    """Select kept items that are likely to be false keeps."""
    decision = result.get("decision")
    category = result.get("fact_category", "other")
    if decision == "MOVE_TO_METADATA":
        return True
    if decision == "KEEP_CONTEXT":
        return True
    if result.get("rescued"):
        return True
    if category in {"boilerplate", "greeting", "logistics", "speaker", "metadata", "metric_convention", "risk", "other"}:
        return True

    lowered = text.strip().lower()
    risky_starts = (
        "these statements", "this conference call", "certain financial metrics",
        "a reconciliation", "thank you", "good morning", "at this time",
        "with me today", "before we begin", "as a reminder",
    )
    return lowered.startswith(risky_starts)


def apply_keep_review(
    final_results: list[dict[str, Any]],
    keep_review_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Apply risky-keep review decisions."""
    review_map = {r["source_id"]: r for r in keep_review_results}
    updated: list[dict[str, Any]] = []

    for item in final_results:
        result = dict(item)
        review = review_map.get(result["source_id"])
        result["keep_reviewed"] = bool(review)
        result.setdefault("moved_to_metadata", False)

        if not review:
            updated.append(result)
            continue

        result["keep_review_decision"] = review.get("keep_review_decision", "")
        result["keep_review_reason"] = review.get("reason", "")

        action = review.get("keep_review_decision")
        if action == "CONFIRM_KEEP":
            result["fact_category"] = review.get("fact_category", result.get("fact_category", "other"))
        elif action == "MOVE_TO_METADATA":
            result["decision"] = "MOVE_TO_METADATA"
            result["reason"] = "moved_by_keep_review: " + review.get("reason", "")
            result["fact_category"] = review.get("fact_category", "metadata")
            result["moved_to_metadata"] = True
        elif action == "DROP_NOISE":
            result["decision"] = "DISCARD"
            result["reason"] = "dropped_by_keep_review: " + review.get("reason", "")
            result["fact_category"] = review.get("fact_category", result.get("fact_category", "other"))

        updated.append(result)

    return updated


def apply_drop_review(
    initial_results: list[dict[str, Any]],
    review_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Merge review decisions into initial decisions."""
    review_map = {r["source_id"]: r for r in review_results}
    final_results: list[dict[str, Any]] = []

    for initial in initial_results:
        result = dict(initial)
        result["initial_decision"] = initial.get("decision")
        result["initial_reason"] = initial.get("reason")
        result["reviewed"] = False
        result["rescued"] = False

        if initial.get("decision") != "DISCARD":
            final_results.append(result)
            continue

        review = review_map.get(initial["source_id"])
        if review is None:
            final_results.append(result)
            continue

        result["reviewed"] = True
        result["review_decision"] = review.get("review_decision")
        result["review_reason"] = review.get("reason")

        if review.get("review_decision") == "RESCUE_KEEP_FACT":
            result["decision"] = "KEEP_FACT"
            result["reason"] = "rescued_by_drop_review: " + review.get("reason", "")
            result["fact_category"] = review.get("fact_category", result.get("fact_category", "other"))
            result["rescued"] = True
        elif review.get("review_decision") == "RESCUE_KEEP_CONTEXT":
            result["decision"] = "KEEP_CONTEXT"
            result["reason"] = "rescued_by_drop_review: " + review.get("reason", "")
            result["fact_category"] = "context_anchor"
            result["rescued"] = True
        elif review.get("review_decision") == "MOVE_TO_METADATA":
            result["decision"] = "MOVE_TO_METADATA"
            result["reason"] = "moved_by_drop_review: " + review.get("reason", "")
            result["fact_category"] = review.get("fact_category", "metadata")
            result["rescued"] = True
            result["moved_to_metadata"] = True

        final_results.append(result)

    return final_results


def attach_items_to_results(
    parsed_data: list[dict[str, str]],
    results: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Build clean_data, drop_data, rescued_data, and metadata_data from final decisions."""
    decision_map = {r["source_id"]: r for r in results}
    clean_data: list[dict[str, Any]] = []
    drop_data: list[dict[str, Any]] = []
    rescued_data: list[dict[str, Any]] = []
    metadata_data: list[dict[str, Any]] = []

    for item in parsed_data:
        decision = decision_map.get(item["source_id"], {})
        merged = {
            **item,
            "decision": decision.get("decision", "MISSING"),
            "reason": decision.get("reason", "missing decision"),
            "fact_category": decision.get("fact_category", "unknown"),
            "fallback": bool(decision.get("fallback", False)),
            "reviewed": bool(decision.get("reviewed", False)),
            "rescued": bool(decision.get("rescued", False)),
            "initial_decision": decision.get("initial_decision", decision.get("decision", "MISSING")),
            "initial_reason": decision.get("initial_reason", ""),
            "review_decision": decision.get("review_decision", ""),
            "review_reason": decision.get("review_reason", ""),
        }

        if merged["decision"] in {"KEEP_FACT", "KEEP_CONTEXT"}:
            clean_data.append(item)
            if merged["rescued"]:
                rescued_data.append(merged)
        elif merged["decision"] == "MOVE_TO_METADATA":
            metadata_data.append(merged)
        elif merged["decision"] == "DISCARD":
            drop_data.append(merged)

    return clean_data, drop_data, rescued_data, metadata_data


def count_by_key(items: Iterable[dict[str, Any]], key: str) -> dict[str, int]:
    """Count items by a key for reports."""
    counts: dict[str, int] = {}
    for item in items:
        value = str(item.get(key, "unknown"))
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def build_quality_report(
    *,
    parsed_data: list[dict[str, str]],
    initial_results: list[dict[str, Any]],
    review_results: list[dict[str, Any]],
    final_results: list[dict[str, Any]],
    clean_data: list[dict[str, Any]],
    drop_data: list[dict[str, Any]],
    rescued_data: list[dict[str, Any]],
    metadata_data: list[dict[str, Any]],
    keep_review_results: list[dict[str, Any]],
    audit_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Compute preprocessing metrics for quality tracking."""
    total = len(parsed_data)
    kept = len(clean_data)
    dropped = len(drop_data)
    metadata_count = len(metadata_data)
    initial_discard = sum(1 for r in initial_results if r.get("decision") == "DISCARD")
    rescued = len(rescued_data)
    reviewed = len(review_results)

    audit_counts = count_by_key(audit_results, "audit_label") if audit_results else {}

    return {
        "sentence_units_before": total,
        "sentence_units_after": kept,
        "final_discarded": dropped,
        "moved_to_metadata": metadata_count,
        "final_reduction_pct": round(((dropped + metadata_count) / total * 100), 1) if total else 0.0,
        "retention_pct": round((kept / total * 100), 1) if total else 0.0,
        "initial_keep_fact": sum(1 for r in initial_results if r.get("decision") == "KEEP_FACT"),
        "initial_keep_context": sum(1 for r in initial_results if r.get("decision") == "KEEP_CONTEXT"),
        "initial_discarded": initial_discard,
        "reviewed_discarded": reviewed,
        "rescued_by_review": rescued,
        "risky_keep_reviewed": len(keep_review_results),
        "dropped_by_keep_review": sum(1 for r in final_results if str(r.get("reason", "")).startswith("dropped_by_keep_review")),
        "moved_by_review": metadata_count,
        "confirmed_discarded_after_review": max(0, initial_discard - rescued),
        "rescue_rate_over_initial_discards_pct": round((rescued / initial_discard * 100), 1) if initial_discard else 0.0,
        "final_keep_fact": sum(1 for r in final_results if r.get("decision") == "KEEP_FACT"),
        "final_keep_context": sum(1 for r in final_results if r.get("decision") == "KEEP_CONTEXT"),
        "fallback_count": sum(1 for r in final_results if r.get("fallback")),
        "final_keep_category_counts": count_by_key(
            [r for r in final_results if r.get("decision") in {"KEEP_FACT", "KEEP_CONTEXT"}],
            "fact_category",
        ),
        "final_drop_category_counts": count_by_key(drop_data, "fact_category"),
        "metadata_category_counts": count_by_key(metadata_data, "fact_category"),
        "audit_enabled": bool(audit_results),
        "audit_counts": audit_counts,
    }
