"""Copy clean corpus text files into a GraphRAG workspace input directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKIP_DIRS = {"drop_logs", "metadata"}


def is_clean_text_file(path: Path, clean_corpus: Path) -> bool:
    """Return true when path is a clean document text file."""
    if path.suffix != ".txt":
        return False
    if path.name.endswith(".drop.txt"):
        return False
    relative_parts = path.relative_to(clean_corpus).parts
    return not any(part in SKIP_DIRS for part in relative_parts)


def collect_clean_files(clean_corpus: Path) -> list[Path]:
    """Collect clean .txt files while excluding audit/log artifacts."""
    return sorted(
        path
        for path in clean_corpus.rglob("*.txt")
        if path.is_file() and is_clean_text_file(path, clean_corpus)
    )


def copy_clean_files(
    clean_corpus: Path,
    workspace_input: Path,
    *,
    clear: bool,
    flatten: bool,
) -> list[Path]:
    """Copy clean files to GraphRAG input and return destination paths."""
    if clear and workspace_input.exists():
        shutil.rmtree(workspace_input)
    workspace_input.mkdir(parents=True, exist_ok=True)

    copied: list[Path] = []
    for source in collect_clean_files(clean_corpus):
        relative = source.relative_to(clean_corpus)
        destination = workspace_input / source.name if flatten else workspace_input / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(destination)

    return copied


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare GraphRAG input/ from clean_corpus/ without audit logs.",
    )
    parser.add_argument("--clean-corpus", required=True, type=Path)
    parser.add_argument("--workspace-input", required=True, type=Path)
    parser.add_argument("--clear", action="store_true", help="Clear input directory first.")
    parser.add_argument(
        "--flatten",
        action="store_true",
        help="Copy all clean text files directly under input/ instead of preserving folders.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    clean_corpus = args.clean_corpus.resolve()
    workspace_input = args.workspace_input.resolve()

    if not clean_corpus.is_dir():
        raise FileNotFoundError(f"Clean corpus folder does not exist: {clean_corpus}")

    copied = copy_clean_files(
        clean_corpus,
        workspace_input,
        clear=args.clear,
        flatten=args.flatten,
    )
    print(f"Copied {len(copied)} clean file(s) to {workspace_input}")
    for path in copied:
        print(path)


if __name__ == "__main__":
    main()
