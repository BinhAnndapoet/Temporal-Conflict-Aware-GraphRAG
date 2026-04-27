"""
create_raw_corpus.py
====================
Đọc file .jsonl / .json chứa Earnings Call Transcripts (ECT-QA format)
và tổ chức nội dung thành cây thư mục raw_txt/:

    <workspace>/data/raw_txt/
    ├── Crocs_Inc/
    │   ├── CROX_consumer_discretionary_2024_q1.txt
    │   └── ...
    └── ...

Cách chạy (từ repo code chính):
    uv run python scripts/data_prep/create_raw_corpus.py \\
        --input ../my_workspace/data/ECT-QA/corpus_author/train.jsonl \\
        --output ../my_workspace/data/raw_txt/
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterator

# ---------------------------------------------------------------------------
# Hằng số
# ---------------------------------------------------------------------------

# Ký tự bị cấm / gây lỗi trên filesystem (Linux + cross-platform safe)
_UNSAFE_CHARS = re.compile(r'[,\.\'\"\\/\\\:*?<>|]')

# Nhiều dấu _ liên tiếp → rút gọn thành 1
_MULTI_UNDERSCORE = re.compile(r'_+')

# Default output folder (tương đối theo CWD — user nên luôn truyền --output)
DEFAULT_OUTPUT = Path.cwd() / "data" / "raw_txt"


# ---------------------------------------------------------------------------
# Hàm tiện ích
# ---------------------------------------------------------------------------

def normalize_company_name(name: str) -> str:
    """
    Chuẩn hóa tên công ty thành tên folder hợp lệ trên filesystem.

    Quy tắc:
      - Giữ nguyên casing gốc (không lowercase)
      - Xóa ký tự filesystem-unsafe: , . ' " / \\ : * ? < > |
      - Thay khoảng trắng bằng '_'
      - Thu gọn nhiều '_' liên tiếp thành 1
      - Strip '_' đầu / cuối

    Args:
        name: Giá trị raw của field "company_name" trong record.

    Returns:
        Tên folder đã được chuẩn hóa. Ví dụ:
            "Crocs, Inc."       → "Crocs_Inc"
            "AT&T Inc."         → "AT&T_Inc"
            "BJ's Wholesale"    → "BJs_Wholesale"

    Raises:
        ValueError: Nếu sau khi chuẩn hóa tên rỗng.
    """
    # Xóa ký tự không an toàn
    cleaned = _UNSAFE_CHARS.sub("", name)
    # Thay khoảng trắng → _
    cleaned = re.sub(r'\s+', '_', cleaned)
    # Thu gọn __ → _
    cleaned = _MULTI_UNDERSCORE.sub("_", cleaned)
    # Strip đầu/cuối
    cleaned = cleaned.strip("_")

    if not cleaned:
        raise ValueError(f"Tên công ty sau chuẩn hóa bị rỗng: {name!r}")

    return cleaned


def make_txt_filename(stock_code: str, sector: str, year: str, quarter: str) -> str:
    """
    Tạo tên file .txt theo format chuẩn của project.

    Args:
        stock_code: Mã cổ phiếu, ví dụ "CROX".
        sector:     Tên sector, ví dụ "consumer_discretionary".
        year:       Năm, ví dụ "2024".
        quarter:    Quý, ví dụ "q1".

    Returns:
        Chuỗi tên file dạng "{stock_code}_{sector}_{year}_{quarter}.txt".
        Ví dụ: "CROX_consumer_discretionary_2024_q1.txt"
    """
    return f"{stock_code}_{sector}_{year}_{quarter}.txt"


# ---------------------------------------------------------------------------
# Parser JSONL dạng multi-line (không có dấu phẩy giữa các object)
# ---------------------------------------------------------------------------

def iter_json_objects(file_path: Path) -> Iterator[dict]:
    """
    Generator: parse tuần tự từng JSON object từ file.

    Hỗ trợ hai định dạng:
      - .jsonl (hoặc .json multi-object): nhiều JSON object liền nhau,
        KHÔNG có dấu phẩy phân cách, mỗi object có thể trải dài nhiều dòng.
      - .json (single object hoặc JSON array [...]): đọc toàn bộ rồi parse.

    Args:
        file_path: Path tới file .jsonl hoặc .json cần đọc.

    Yields:
        Từng dict record đã được parse thành công.

    Raises:
        FileNotFoundError: Nếu file không tồn tại.
        json.JSONDecodeError: Nếu nội dung không hợp lệ JSON.
    """
    decoder = json.JSONDecoder()
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file: {file_path}")

    content = file_path.read_text(encoding="utf-8")

    # Thử parse .json chuẩn (single object hoặc list) trước
    stripped = content.strip()
    if stripped.startswith('['):
        data = json.loads(content)
        if isinstance(data, list):
            yield from data
            return
        yield data
        return

    # Streaming parse: tìm từng object bằng raw_decode
    pos = 0
    length = len(content)
    while pos < length:
        # Bỏ qua whitespace
        while pos < length and content[pos] in ' \t\n\r':
            pos += 1
        if pos >= length:
            break

        try:
            obj, end_pos = decoder.raw_decode(content, pos)
        except json.JSONDecodeError as exc:
            print(f"[WARN] JSONDecodeError tại pos={pos}: {exc}", file=sys.stderr)
            pos += 1
            continue

        if isinstance(obj, dict):
            yield obj

        pos = end_pos


# ---------------------------------------------------------------------------
# Xử lý từng record
# ---------------------------------------------------------------------------

def process_record(record: dict, output_dir: Path) -> Path:
    """
    Xử lý 1 record: tạo folder công ty + ghi file .txt.

    Args:
        record:     Dict chứa ít nhất các key: company_name, stock_code,
                    sector, year, quarter, cleaned_content.
        output_dir: Root output folder (ví dụ: Path("data/raw_txt")).

    Returns:
        Path tuyệt đối của file .txt vừa được ghi.

    Raises:
        KeyError:   Nếu record thiếu field bắt buộc.
        ValueError: Nếu company_name sau chuẩn hóa bị rỗng.
    """
    # Lấy metadata (raise KeyError rõ ràng nếu thiếu field)
    company_name    = record["company_name"]
    stock_code      = record["stock_code"]
    sector          = record["sector"]
    year            = record["year"]
    quarter         = record["quarter"]
    cleaned_content = record["cleaned_content"]

    # Chuẩn hóa tên folder công ty
    company_folder = normalize_company_name(company_name)

    # Tạo thư mục đích (mkdir -p)
    company_dir = output_dir / company_folder
    company_dir.mkdir(parents=True, exist_ok=True)

    # Đặt tên file và ghi nội dung
    filename = make_txt_filename(stock_code, sector, year, quarter)
    out_file = company_dir / filename
    out_file.write_text(cleaned_content, encoding="utf-8")

    return out_file


# ---------------------------------------------------------------------------
# Báo cáo chi tiết
# ---------------------------------------------------------------------------

def _print_company_summary(files_per_company: dict[str, int], total_files: int) -> None:
    """
    In bảng thống kê chi tiết số file .txt theo từng folder công ty.

    Args:
        files_per_company: Dict {tên_folder: số_file}, đã được tích lũy
                           trong quá trình xử lý.
        total_files:       Tổng số file .txt đã tạo thành công.
    """
    if not files_per_company:
        return

    # Sắp xếp theo tên folder (alphabetical)
    sorted_companies = sorted(files_per_company.items(), key=lambda x: x[0].lower())

    # Tính độ rộng cột cho căn chỉnh đẹp
    max_name_len = max(len(name) for name in files_per_company)
    col_width    = max(max_name_len, len("Company Folder")) + 2

    sep = "=" * (col_width + 14)
    print()
    print(sep)
    print(f"  {'Company Folder':<{col_width}}  Files .txt")
    print(sep)

    for folder_name, count in sorted_companies:
        print(f"  {folder_name:<{col_width}}  {count}")

    print("-" * (col_width + 14))
    print(f"  {'TOTAL':<{col_width}}  {total_files}")
    print(sep)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def create_raw_corpus(input_file: Path, output_dir: Path) -> None:
    """
    Orchestrator chính: đọc toàn bộ file input và xử lý từng record.

    Args:
        input_file: Path tới file .jsonl hoặc .json đầu vào.
        output_dir: Root folder chứa kết quả raw_txt/.

    Raises:
        FileNotFoundError: Nếu input_file không tồn tại.
    """
    input_file = Path(input_file).resolve()
    output_dir = Path(output_dir).resolve()

    print(f"[INFO] Input  : {input_file}")
    print(f"[INFO] Output : {output_dir}")
    print("-" * 60)

    # Tạo root output folder
    output_dir.mkdir(parents=True, exist_ok=True)

    total_records  = 0
    total_files    = 0
    total_errors   = 0
    # key = tên folder công ty, value = số file .txt đã tạo
    files_per_company: dict[str, int] = {}

    for record in iter_json_objects(input_file):
        total_records += 1

        try:
            out_file = process_record(record, output_dir)
            total_files += 1
            folder_name = out_file.parent.name
            files_per_company[folder_name] = files_per_company.get(folder_name, 0) + 1
        except (KeyError, ValueError) as exc:
            total_errors += 1
            print(
                f"[WARN] Bỏ qua record #{total_records} "
                f"(company={record.get('company_name', '?')}): {exc}",
                file=sys.stderr,
            )
            continue

        # In tiến độ mỗi 50 records
        if total_records % 50 == 0:
            print(f"[INFO] Đã xử lý {total_records} records ...")

    # Thống kê tổng kết
    print("-" * 60)
    print(f"[DONE] Tổng records đọc được : {total_records}")
    print(f"[DONE] Files .txt đã tạo     : {total_files}")
    print(f"[DONE] Folders công ty        : {len(files_per_company)}")
    if total_errors:
        print(f"[WARN] Records bị lỗi / bỏ qua: {total_errors}", file=sys.stderr)
    print(f"[DONE] Output nằm tại        : {output_dir}")

    # In bảng chi tiết per-company
    _print_company_summary(files_per_company, total_files)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    """Tạo ArgumentParser cho CLI."""
    parser = argparse.ArgumentParser(
        prog="create_raw_corpus",
        description=(
            "Đọc file .jsonl/.json ECT-QA và tạo cây thư mục raw_txt/\n"
            "Mỗi công ty → 1 folder; mỗi transcript → 1 file .txt."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ví dụ:\n"
            "  uv run python scripts/data_prep/create_raw_corpus.py \\\n"
            "      --input ../my_workspace/data/ECT-QA/corpus_author/train.jsonl \\\n"
            "      --output ../my_workspace/data/raw_txt/\n"
        ),
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        type=Path,
        metavar="FILE",
        help="Đường dẫn tới file .jsonl hoặc .json đầu vào (bắt buộc).",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        metavar="DIR",
        help=(
            f"Thư mục output chứa kết quả. "
            f"Mặc định: {DEFAULT_OUTPUT}"
        ),
    )
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    create_raw_corpus(input_file=args.input, output_dir=args.output)
