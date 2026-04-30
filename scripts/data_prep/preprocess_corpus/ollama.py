"""Ollama API interaction, JSON parsing, and decision validation."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

import requests

from .constants import (
    ALLOWED_AUDIT_LABELS,
    ALLOWED_INITIAL_DECISIONS,
    ALLOWED_KEEP_REVIEW_DECISIONS,
    ALLOWED_REVIEW_DECISIONS,
    OLLAMA_BASE_URL_ENV,
    OLLAMA_CHAT_URL_ENV,
    OLLAMA_URL,
    SYSTEM_PROMPT,
)


def strip_model_noise(text: str) -> str:
    """Remove markdown fences and common Qwen thinking blocks from model output."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "").strip()
    return text


def parse_model_json(content: str, expected_key: str) -> dict[str, Any]:
    """Parse model output into a dictionary containing expected_key."""
    text = strip_model_noise(content)

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        data = json.loads(text[start: end + 1])

    if isinstance(data, list):
        return {expected_key: data}
    if isinstance(data, dict):
        if expected_key in data:
            return data
        if expected_key == "decisions" and "results" in data and isinstance(data["results"], list):
            return {"decisions": data["results"]}
        if expected_key == "audit" and "results" in data and isinstance(data["results"], list):
            return {"audit": data["results"]}

    raise ValueError(f"Model JSON does not contain {expected_key!r}")


def _validate_decision_objects(
    *,
    data: dict[str, Any],
    key: str,
    batch: list[dict[str, Any]],
    decision_field: str,
    allowed: set[str],
    extra_defaults: dict[str, Any],
) -> list[dict[str, Any]]:
    """Generic decision validation preserving input order."""
    objects = data.get(key)
    if not isinstance(objects, list):
        raise ValueError(f"{key} is not a list")

    expected_ids = {str(item["source_id"]) for item in batch}
    order = {str(item["source_id"]): idx for idx, item in enumerate(batch)}
    validated: list[dict[str, Any]] = []
    seen: set[str] = set()

    for obj in objects:
        if not isinstance(obj, dict):
            continue
        sid = str(obj.get("source_id", "")).strip()
        decision = str(obj.get(decision_field, "")).strip().upper()
        if sid not in expected_ids:
            continue
        if decision not in allowed:
            raise ValueError(f"Invalid {decision_field} for {sid}: {decision!r}")

        normalized = {
            "source_id": sid,
            decision_field: decision,
            "reason": str(obj.get("reason", "")).strip() or "no reason provided",
        }
        if key != "audit":
            normalized["fact_category"] = str(obj.get("fact_category", "other")).strip() or "other"
        normalized.update(extra_defaults)
        validated.append(normalized)
        seen.add(sid)

    missing = expected_ids - seen
    if missing:
        raise ValueError(f"Missing {decision_field} for source_ids: {sorted(missing)}")

    return sorted(validated, key=lambda x: order[x["source_id"]])


def validate_initial_decisions(data: dict[str, Any], batch: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate initial KEEP_FACT/KEEP_CONTEXT/DISCARD decisions."""
    return _validate_decision_objects(
        data=data, key="decisions", batch=batch,
        decision_field="decision", allowed=ALLOWED_INITIAL_DECISIONS,
        extra_defaults={"rule_based": False, "fallback": False},
    )


def validate_review_decisions(data: dict[str, Any], batch: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate drop-review rescue/confirm decisions."""
    return _validate_decision_objects(
        data=data, key="decisions", batch=batch,
        decision_field="review_decision", allowed=ALLOWED_REVIEW_DECISIONS,
        extra_defaults={"fallback": False},
    )


def validate_keep_review_decisions(data: dict[str, Any], batch: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate risky-keep review decisions."""
    return _validate_decision_objects(
        data=data, key="decisions", batch=batch,
        decision_field="keep_review_decision", allowed=ALLOWED_KEEP_REVIEW_DECISIONS,
        extra_defaults={"fallback": False},
    )


def validate_audit_items(data: dict[str, Any], batch: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate optional audit labels."""
    return _validate_decision_objects(
        data=data, key="audit", batch=batch,
        decision_field="audit_label", allowed=ALLOWED_AUDIT_LABELS,
        extra_defaults={},
    )


def get_ollama_chat_url() -> str:
    """Resolve the Ollama chat endpoint from env, falling back to localhost."""
    chat_url = os.getenv(OLLAMA_CHAT_URL_ENV)
    if chat_url:
        return chat_url.rstrip("/")

    base_url = os.getenv(OLLAMA_BASE_URL_ENV)
    if base_url:
        return f"{base_url.rstrip('/')}/api/chat"

    return OLLAMA_URL


def call_ollama(
    prompt: str,
    model: str,
    timeout: int,
    json_mode: bool,
    num_ctx: int,
) -> dict[str, Any]:
    """Call local Ollama chat endpoint with deterministic settings."""
    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "options": {
            "temperature": 0.0,
            "num_ctx": num_ctx,
        },
    }
    if json_mode:
        payload["format"] = "json"

    resp = requests.post(get_ollama_chat_url(), json=payload, timeout=timeout)
    resp.raise_for_status()
    return {"payload": payload, "response": resp.json()}


def save_debug_file(debug_dir: Path | None, name: str, content: str | dict | list) -> None:
    """Write debug content if --debug is enabled."""
    if debug_dir is None:
        return
    debug_dir.mkdir(parents=True, exist_ok=True)
    path = debug_dir / name
    if isinstance(content, (dict, list)):
        path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        path.write_text(content, encoding="utf-8")
