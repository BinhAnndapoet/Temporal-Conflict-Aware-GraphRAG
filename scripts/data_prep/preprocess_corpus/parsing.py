"""Transcript parsing, sentence splitting, and context-window construction."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .constants import ABBREVIATIONS


def parse_document_metadata(input_path: Path) -> dict[str, str]:
    """Parse document metadata from the corpus filename.

    Expected filename pattern: {stock_code}_{sector}_{year}_{quarter}.txt
    Example: CROX_consumer_discretionary_2024_q1.txt
    """
    stem = input_path.stem
    parts = stem.split("_")
    metadata = {
        "document_id": stem,
        "company_folder": input_path.parent.name,
        "stock_code": "",
        "sector": "",
        "year": "",
        "quarter": "",
    }

    if len(parts) >= 4:
        metadata["stock_code"] = parts[0]
        metadata["year"] = parts[-2]
        metadata["quarter"] = parts[-1]
        metadata["sector"] = "_".join(parts[1:-2])

    return metadata


def split_sentences(text: str) -> list[str]:
    """Split one transcript line/paragraph into sentence-like units.

    This function is intentionally conservative and purely mechanical.
    It does NOT classify text.
    """
    text = text.strip()
    if not text:
        return []

    if len(text) <= 80 and (text == "--" or not re.search(r"[.!?]", text)):
        return [text]

    protected = text
    placeholder_map: dict[str, str] = {}

    for i, abbr in enumerate(ABBREVIATIONS):
        token = f"__ABBR_{i}__"
        placeholder_map[token] = abbr
        protected = protected.replace(abbr, token)

    parts = re.split(
        r"(?<=[.!?])\s+(?=(?:[A-Z0-9\[]|And\b|But\b|For\b|In\b|As\b|Now\b|Turning\b|Finally\b|Overall\b|First\b|Second\b|Third\b))",
        protected,
    )

    restored: list[str] = []
    for part in parts:
        sent = part.strip()
        for token, abbr in placeholder_map.items():
            sent = sent.replace(token, abbr)
        if sent:
            restored.append(sent)

    return restored or [text]


def parse_transcript(file_path: str | Path) -> list[dict[str, str]]:
    """Read a raw corpus .txt file and split it into sentence units."""
    path = Path(file_path)
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    parsed_data: list[dict[str, str]] = []
    for line_idx, line in enumerate(lines, start=1):
        text = line.strip()
        if not text:
            continue
        for sent_idx, sent in enumerate(split_sentences(text), start=1):
            parsed_data.append(
                {
                    "source_id": f"{line_idx}.{sent_idx}",
                    "line_id": str(line_idx),
                    "sentence_id": str(sent_idx),
                    "text": sent,
                }
            )

    return parsed_data


def build_context_items(parsed_data: list[dict[str, str]], *, window: int = 1) -> list[dict[str, Any]]:
    """Attach local context around each sentence unit for LLM decisions."""
    items: list[dict[str, Any]] = []
    for idx, item in enumerate(parsed_data):
        before = parsed_data[max(0, idx - window): idx]
        after = parsed_data[idx + 1: idx + 1 + window]
        items.append(
            {
                "source_id": item["source_id"],
                "target": item["text"],
                "context_before": [x["text"] for x in before],
                "context_after": [x["text"] for x in after],
            }
        )
    return items


def build_context_for_ids(
    parsed_data: list[dict[str, str]],
    source_ids: list[str] | set[str],
    *,
    window: int = 1,
) -> list[dict[str, Any]]:
    """Build context-window payloads for a selected set of source_ids."""
    wanted = set(source_ids)
    all_context = build_context_items(parsed_data, window=window)
    return [item for item in all_context if item["source_id"] in wanted]
