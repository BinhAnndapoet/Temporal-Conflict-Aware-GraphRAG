from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from datasets import (
    Dataset,
    DatasetDict,
    IterableDataset,
    IterableDatasetDict,
    get_dataset_config_names,
    load_dataset,
)
from huggingface_hub import HfApi, hf_hub_download


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a Hugging Face dataset and save it to a workspace data directory.",
        epilog=(
            "Example:\n"
            "  uv run python scripts/data_prep/download_data.py \\\n"
            "      --output-dir ../my_workspace/data\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dataset",
        default="austinmyc/ECT-QA",
        help="Hugging Face dataset ID (default: austinmyc/ECT-QA)",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to store downloaded dataset artifacts (workspace data dir).",
    )
    parser.add_argument(
        "--subset",
        default="all",
        choices=["all", "questions", "corpus"],
        help="Dataset subset/config to download (default: all).",
    )
    parser.add_argument(
        "--mode",
        default="readme",
        choices=["readme", "hf-dataset"],
        help=(
            "Download mode: 'readme' preserves raw JSON layout from dataset README; "
            "'hf-dataset' saves Hugging Face dataset objects to disk."
        ),
    )
    parser.add_argument(
        "--no-author-corpus",
        action="store_true",
        help=(
            "Skip exporting author corpus train split (JSONL) in readme mode. "
            "By default, corpus is exported to ECT-QA/corpus_author/train.jsonl."
        ),
    )
    return parser.parse_args()


def _is_streaming_dataset(obj: object) -> bool:
    return isinstance(obj, IterableDataset | IterableDatasetDict)


def _print_dataset_summary(
    ds: Dataset | DatasetDict | IterableDataset | IterableDatasetDict,
) -> None:
    if isinstance(ds, DatasetDict):
        print("Loaded splits:")
        for split_name, split_ds in ds.items():
            print(f"- {split_name}: {split_ds.num_rows} rows")
        return
    if isinstance(ds, Dataset):
        print(f"Loaded dataset rows: {ds.num_rows}")
        return
    if isinstance(ds, IterableDatasetDict):
        print("Loaded iterable dataset splits:")
        for split_name in ds:
            print(f"- {split_name}")
        return
    print("Loaded iterable dataset (row count unavailable in streaming mode).")


def _save_non_streaming_dataset(
    ds: Dataset | DatasetDict | IterableDataset | IterableDatasetDict,
    target_path: Path,
) -> None:
    if _is_streaming_dataset(ds):
        raise ValueError(
            "Streaming dataset cannot be saved with save_to_disk. "
            "Please rerun without streaming mode."
        )

    print(f"Saving dataset to: {target_path}")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    ds.save_to_disk(str(target_path))


def _download_raw_config_files(
    dataset_id: str, config_name: str, target_path: Path
) -> None:
    """Fallback method when dataset builder fails due schema issues."""
    api = HfApi()
    repo_files = api.list_repo_files(repo_id=dataset_id, repo_type="dataset")
    config_prefix = f"{config_name}/"
    config_files = [
        filename for filename in repo_files if filename.startswith(config_prefix)
    ]

    if not config_files:
        raise ValueError(
            f"Could not find raw files for config '{config_name}' in dataset '{dataset_id}'."
        )

    raw_dir = target_path / "raw_files"
    raw_dir.mkdir(parents=True, exist_ok=True)

    for filename in config_files:
        cached_file = hf_hub_download(
            repo_id=dataset_id,
            repo_type="dataset",
            filename=filename,
        )
        destination = raw_dir / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cached_file, destination)

    print(f"Saved raw config files to: {raw_dir}")


def _dataset_root_dir(output_dir: Path, dataset_id: str) -> Path:
    return output_dir / dataset_id.split("/", maxsplit=1)[1]


def _download_readme_layout(
    dataset_id: str,
    subset: str,
    output_dir: Path,
) -> None:
    api = HfApi()
    repo_files = api.list_repo_files(repo_id=dataset_id, repo_type="dataset")

    prefixes: list[str]
    if subset == "all":
        prefixes = ["data/", "questions/"]
    elif subset == "corpus":
        prefixes = ["data/"]
    else:
        prefixes = ["questions/"]

    selected_files = [
        filename
        for filename in repo_files
        if any(filename.startswith(prefix) for prefix in prefixes)
    ]

    if not selected_files:
        raise ValueError(
            f"No files found for subset '{subset}' in dataset '{dataset_id}'."
        )

    target_root = _dataset_root_dir(output_dir, dataset_id)
    target_root.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {len(selected_files)} file(s) in README layout...")
    for filename in selected_files:
        cached_file = hf_hub_download(
            repo_id=dataset_id,
            repo_type="dataset",
            filename=filename,
        )
        destination = target_root / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cached_file, destination)

    print(f"Saved files to: {target_root}")


def _export_author_corpus_train_jsonl(dataset_id: str, output_dir: Path) -> None:
    """Export author corpus/train split as JSONL for immediate downstream use."""
    ds = load_dataset(dataset_id, "corpus")

    if isinstance(ds, DatasetDict):
        if "train" not in ds:
            raise ValueError("Expected 'train' split in corpus config but none found.")
        train_ds = ds["train"]
    elif isinstance(ds, Dataset):
        train_ds = ds
    else:
        raise ValueError("Corpus config returned an unsupported dataset type.")

    target_root = _dataset_root_dir(output_dir, dataset_id) / "corpus_author"
    target_root.mkdir(parents=True, exist_ok=True)
    jsonl_path = target_root / "train.jsonl"

    print(f"Exporting author corpus train split to: {jsonl_path}")
    train_ds.to_json(str(jsonl_path))
    print(f"Exported {train_ds.num_rows} rows.")


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset: {args.dataset}")
    print(f"Mode: {args.mode}")
    print(f"Subset: {args.subset}")

    if args.mode == "readme":
        _download_readme_layout(args.dataset, args.subset, output_dir)
        if not args.no_author_corpus and args.subset in {"all", "corpus"}:
            _export_author_corpus_train_jsonl(args.dataset, output_dir)
        print("Done.")
        return

    dataset_slug = args.dataset.replace("/", "__")
    target_path = output_dir / dataset_slug

    if args.subset == "all":
        configs = get_dataset_config_names(args.dataset)
        if not configs:
            ds = load_dataset(args.dataset)
            _print_dataset_summary(ds)
            _save_non_streaming_dataset(ds, target_path)
            print("Done.")
            return

        print(f"Found configs: {', '.join(configs)}")
        for config_name in configs:
            print(f"\nDownloading config: {config_name}")
            config_target = target_path / config_name
            try:
                ds = load_dataset(args.dataset, config_name)
                _print_dataset_summary(ds)
                _save_non_streaming_dataset(ds, config_target)
            except Exception as exc:  # noqa: BLE001
                print(
                    "Warning: standard load failed for "
                    f"'{config_name}'. Falling back to raw file download."
                )
                print(f"Reason: {exc}")
                _download_raw_config_files(args.dataset, config_name, config_target)
    else:
        config_target = target_path / args.subset
        try:
            ds = load_dataset(args.dataset, args.subset)
            _print_dataset_summary(ds)
            _save_non_streaming_dataset(ds, config_target)
        except Exception as exc:  # noqa: BLE001
            print(
                "Warning: standard load failed for "
                f"'{args.subset}'. Falling back to raw file download."
            )
            print(f"Reason: {exc}")
            _download_raw_config_files(args.dataset, args.subset, config_target)

    print("Done.")


if __name__ == "__main__":
    main()
