# Copyright (c) 2025 Microsoft Corporation.
# Licensed under the MIT License

"""Convert parquet files in a selected GraphRAG workspace output folder to CSV.

The script keeps the original parquet files and writes CSV files next to them.

Run from repository root (recommended):

    uv run python scripts/convert_parquet_to_csv.py

Or specify a folder directly:

    uv run python scripts/convert_parquet_to_csv.py \
      --output-dir /home/<user>/Projects/ban/my_workspace_openai/output

If CSV files already exist and you want to replace them:

    uv run python scripts/convert_parquet_to_csv.py --overwrite
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def find_workspace_output_dirs(repo_root: Path) -> list[Path]:
    """Find candidate my_workspace_*/output directories near the repository."""
    parent_dir = repo_root.parent
    candidates: list[Path] = []

    for workspace_dir in sorted(parent_dir.glob("my_workspace*")):
        output_dir = workspace_dir / "output"
        if output_dir.is_dir():
            candidates.append(output_dir)

    return candidates


def choose_output_dir(candidates: list[Path], provided_path: str | None) -> Path:
    """Resolve output directory either from argument or interactive selection."""
    if provided_path:
        selected = Path(provided_path).expanduser().resolve()
        if not selected.is_dir():
            raise FileNotFoundError(f"Folder does not exist: {selected}")
        return selected

    print("\n=== Select output folder containing parquet files ===")
    if candidates:
        for idx, folder in enumerate(candidates, start=1):
            print(f"{idx}. {folder}")
        print("0. Enter a custom path")
    else:
        print("No my_workspace*/output folder found automatically.")
        print("Please enter a custom path.")

    while True:
        choice = input("Choose an option: ").strip()

        if candidates and choice.isdigit():
            selected_idx = int(choice)
            if 1 <= selected_idx <= len(candidates):
                return candidates[selected_idx - 1]
            if selected_idx == 0:
                custom_path = input("Enter folder path: ").strip()
                selected = Path(custom_path).expanduser().resolve()
                if selected.is_dir():
                    return selected
                print(f"[Error] Folder does not exist: {selected}")
                continue

        if not candidates:
            selected = Path(choice).expanduser().resolve()
            if selected.is_dir():
                return selected
            print(f"[Error] Folder does not exist: {selected}")
            continue

        print("[Error] Invalid choice. Please try again.")


def collect_parquet_files(root_dir: Path, recursive: bool) -> list[Path]:
    """Collect parquet files from the selected directory."""
    pattern = "**/*.parquet" if recursive else "*.parquet"
    return sorted(root_dir.glob(pattern))


def convert_parquet_to_csv(
    parquet_path: Path,
    overwrite: bool,
    sep: str,
    encoding: str,
    include_index: bool,
) -> tuple[bool, Path]:
    """Convert one parquet file to CSV and return (converted, csv_path)."""
    try:
        import pandas as pd  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "pandas is required.\n"
            "Please run from repository root:\n"
            "  uv sync --all-packages\n"
            "  uv run python scripts/convert_parquet_to_csv.py"
        ) from exc

    csv_path = parquet_path.with_suffix(".csv")
    if csv_path.exists() and not overwrite:
        return (False, csv_path)

    df = pd.read_parquet(parquet_path)
    df.to_csv(csv_path, index=include_index, sep=sep, encoding=encoding)
    return (True, csv_path)


def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Convert .parquet files in a selected GraphRAG workspace output folder "
            "to .csv files without deleting parquet files."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Path to folder containing parquet files (e.g. /path/to/my_workspace/output).",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Also scan parquet files in nested subfolders.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .csv files if they already exist.",
    )
    parser.add_argument(
        "--sep",
        type=str,
        default=",",
        help="CSV separator character (default: ',').",
    )
    parser.add_argument(
        "--encoding",
        type=str,
        default="utf-8",
        help="Output CSV encoding (default: utf-8).",
    )
    parser.add_argument(
        "--include-index",
        action="store_true",
        help="Include DataFrame index in CSV output (default: false).",
    )
    return parser


def main() -> int:
    """Run conversion process."""
    parser = build_parser()
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    candidates = find_workspace_output_dirs(repo_root)

    try:
        selected_output_dir = choose_output_dir(candidates, args.output_dir)
    except FileNotFoundError as exc:
        print(f"[Error] {exc}")
        return 1

    parquet_files = collect_parquet_files(selected_output_dir, recursive=args.recursive)
    if not parquet_files:
        print(f"No .parquet files found in: {selected_output_dir}")
        return 0

    print(f"\nSelected folder: {selected_output_dir}")
    print(f"Found {len(parquet_files)} parquet file(s).")

    converted_count = 0
    skipped_count = 0

    for parquet_file in parquet_files:
        try:
            converted, csv_path = convert_parquet_to_csv(
                parquet_path=parquet_file,
                overwrite=args.overwrite,
                sep=args.sep,
                encoding=args.encoding,
                include_index=args.include_index,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"[Error] Failed: {parquet_file} -> {exc}")
            continue

        if converted:
            converted_count += 1
            print(f"[OK] {parquet_file.name} -> {csv_path.name}")
        else:
            skipped_count += 1
            print(f"[Skip] {csv_path.name} already exists (use --overwrite to replace)")

    print("\n=== Summary ===")
    print(f"Converted: {converted_count}")
    print(f"Skipped:   {skipped_count}")
    print("Original .parquet files were kept unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
