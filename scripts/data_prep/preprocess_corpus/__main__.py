"""
CLI entry point for the preprocess_corpus package.

Usage (from repo root):
    set -a; source ../my_workspace/.env; set +a

    uv run python -m scripts.data_prep.preprocess_corpus \\
        --input ../my_workspace/data/raw_txt/ \\
        --output ../my_workspace/data/clean_corpus/ \\
        --mode batch

    uv run python -m scripts.data_prep.preprocess_corpus \\
        --env-file ../my_workspace/.env \\
        --input ../my_workspace/data/raw_txt/Crocs_Inc/CROX_consumer_discretionary_2024_q1.txt \\
        --output ../my_workspace/data/clean_corpus/ \\
        --mode file
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from .constants import (
    DEFAULT_BATCH_SIZE,
    DEFAULT_MODEL,
    DEFAULT_NUM_CTX,
    DEFAULT_REVIEW_BATCH_SIZE,
    OLLAMA_CHAT_MODEL_ENV,
)
from .writers import preprocess_batch_dir, preprocess_file, print_batch_report, print_file_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="preprocess_corpus",
        description=(
            "LLM-first preprocessing: filter earnings-call transcript sentence units.\n"
            "Uses local Ollama models for high-recall KEEP/DISCARD classification."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  # Use workspace .env for OLLAMA_CHAT_MODEL / OLLAMA_BASE_URL\n"
            "  uv run python -m scripts.data_prep.preprocess_corpus \\\n"
            "      --env-file ../my_workspace/.env \\\n"
            "      --input ../my_workspace/data/raw_txt/Crocs_Inc/CROX_consumer_discretionary_2024_q1.txt \\\n"
            "      --output ../my_workspace/data/clean_corpus/ \\\n"
            "      --mode file\n\n"
            "  # Single file with explicit model override\n"
            "  uv run python -m scripts.data_prep.preprocess_corpus \\\n"
            "      --input ../my_workspace/data/raw_txt/Crocs_Inc/CROX_consumer_discretionary_2024_q1.txt \\\n"
            "      --output ../my_workspace/data/clean_corpus/ \\\n"
            "      --mode file --model qwen3:14b\n\n"
            "  # Batch all files with explicit model override\n"
            "  uv run python -m scripts.data_prep.preprocess_corpus \\\n"
            "      --input ../my_workspace/data/raw_txt/ \\\n"
            "      --output ../my_workspace/data/clean_corpus/ \\\n"
            "      --mode batch --model qwen3:14b\n"
        ),
    )
    parser.add_argument("--input", "-i", required=True, type=Path, help="Input file or directory")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Output directory for clean corpus")
    parser.add_argument("--mode", "-m", choices=["file", "batch"], default="file", help="Processing mode")
    parser.add_argument("--env-file", type=Path, help="Optional workspace .env file to load before resolving Ollama settings")
    parser.add_argument("--model", help=f"Ollama model name (default: ${OLLAMA_CHAT_MODEL_ENV} or {DEFAULT_MODEL})")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE, help=f"Items per LLM batch (default: {DEFAULT_BATCH_SIZE})")
    parser.add_argument("--review-batch-size", type=int, default=DEFAULT_REVIEW_BATCH_SIZE, help=f"Items per review batch (default: {DEFAULT_REVIEW_BATCH_SIZE})")
    parser.add_argument("--timeout", type=int, default=300, help="Ollama API timeout seconds (default: 300)")
    parser.add_argument("--num-ctx", type=int, default=DEFAULT_NUM_CTX, help=f"Ollama context window size (default: {DEFAULT_NUM_CTX})")
    parser.add_argument("--context-window", type=int, default=1, help="Sentence context window for initial pass (default: 1)")
    parser.add_argument("--review-window", type=int, default=1, help="Context window for review passes (default: 1)")
    parser.add_argument("--dry-run", action="store_true", help="Process without writing output files")
    parser.add_argument("--debug", action="store_true", help="Save debug artifacts (prompts, raw responses)")
    parser.add_argument("--json-mode", action="store_true", default=True, help="Request JSON output from Ollama (default: on)")
    parser.add_argument("--no-json-mode", action="store_false", dest="json_mode", help="Disable JSON output mode")
    parser.add_argument("--fallback-policy", choices=["keep", "discard", "abort", "undecided"], default="abort", help="Fallback when LLM fails (default: abort)")
    parser.add_argument("--skip-drop-review", action="store_true", help="Skip pass 2 (drop review)")
    parser.add_argument("--skip-keep-review", action="store_true", help="Skip pass 3 (keep review)")
    parser.add_argument("--audit-sample-size", type=int, default=0, help="Number of items to audit (0 = disabled)")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.env_file:
        load_dotenv(args.env_file)

    model = args.model or os.getenv(OLLAMA_CHAT_MODEL_ENV) or DEFAULT_MODEL
    input_path: Path = args.input.resolve()
    output_dir: Path = args.output.resolve()

    common_kwargs = {
        "model": model,
        "batch_size": args.batch_size,
        "dry_run": args.dry_run,
        "timeout": args.timeout,
        "json_mode": args.json_mode,
        "num_ctx": args.num_ctx,
        "debug": args.debug,
        "fallback_policy": args.fallback_policy,
        "context_window": args.context_window,
        "review_window": args.review_window,
        "review_batch_size": args.review_batch_size,
        "skip_drop_review": args.skip_drop_review,
        "skip_keep_review": args.skip_keep_review,
        "audit_sample_size": args.audit_sample_size,
    }

    print(f"Model          : {model}")
    print(f"Mode           : {args.mode}")
    print(f"Input          : {input_path}")
    print(f"Output         : {output_dir}")
    print(f"Batch size     : {args.batch_size}")
    print(f"Context window : {args.context_window}")
    print(f"Fallback policy: {args.fallback_policy}")
    print()

    if args.mode == "file":
        if not input_path.is_file():
            print(f"ERROR: Not a file: {input_path}", file=sys.stderr)
            sys.exit(1)
        result = preprocess_file(input_path, output_dir, **common_kwargs)
        print_file_report(result)
    else:
        if not input_path.is_dir():
            print(f"ERROR: Not a directory: {input_path}", file=sys.stderr)
            sys.exit(1)
        results = preprocess_batch_dir(input_path, output_dir, **common_kwargs)
        if results:
            print_batch_report(results)


if __name__ == "__main__":
    main()
