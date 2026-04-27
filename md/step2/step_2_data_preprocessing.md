# Step 2: Data Preprocessing cho Temporal GraphRAG

Tài liệu này mô tả chi tiết quy trình Tiền xử lý dữ liệu (Data Preprocessing) từ dữ liệu thô ban đầu (ECT-QA dataset trên HuggingFace) cho đến khi tạo ra `clean_corpus` chứa các sự kiện kinh doanh sạch, sẵn sàng cho GraphRAG `index`.

Toàn bộ các script xử lý nằm trong thư mục `scripts/data_prep/` của repository chính.

---

## Mục Tiêu Của Step 2

GraphRAG tiêu chuẩn hoạt động rất tốt trên văn bản đã được làm sạch. Tuy nhiên, các văn bản như Earnings Call Transcripts (ECT-QA) chứa một lượng khổng lồ "transcript noise" (ví dụ: chào hỏi, giới thiệu thành viên, thủ tục chuyển lời, và thông báo pháp lý an toàn - safe harbor). 

Nếu đưa toàn bộ vào GraphRAG:
1. **Tốn chi phí LLM (Tokens):** Các token rác làm tăng chi phí xây dựng đồ thị một cách vô ích.
2. **Nhiễu đồ thị (Graph Noise):** Các câu rác có thể tạo ra các Entity/Relationship sai lệch (ví dụ: "Operator" introduces "CEO" không mang lại giá trị tri thức kinh doanh).

**Giải pháp:** Sử dụng pipeline 3 bước để lọc và làm sạch dữ liệu trước khi đưa vào thư mục `input/` của workspace.

---

## Pipeline Cấu Trúc File

```
scripts/data_prep/
├── download_data.py              # (1) Tải dataset từ HuggingFace Hub
├── create_raw_corpus.py          # (2) Chuyển đổi JSONL thành cây thư mục .txt (raw)
└── preprocess_corpus/            # (3) Lọc LLM để tạo clean corpus
    ├── __main__.py               
    ├── constants.py              
    ├── parsing.py                
    ├── ollama.py                 
    ├── processing.py             
    └── writers.py                
```

---

## Chi Tiết Từng Bước (Cách Chạy)

> **Lưu ý quan trọng:** Luôn luôn đứng ở thư mục gốc của repository code (`Temporal-Conflict-Aware-GraphRAG`) để chạy các lệnh `uv run`, KHÔNG đứng ở bên trong `my_workspace`.

Giả định workspace của bạn nằm ở `../my_workspace`.

### Bước 2.1: Tải dữ liệu từ HuggingFace (`download_data.py`)

Script này sẽ tải bộ dataset ECT-QA từ Hugging Face Hub (mặc định: `austinmyc/ECT-QA`). Chúng ta sẽ tải cấu hình `corpus_author` để lấy file `train.jsonl` nguyên bản.

**Lệnh chạy:**
```bash
uv run python scripts/data_prep/download_data.py \
    --output-dir ../my_workspace/data
```

**Kết quả:**
- File `train.jsonl` chứa toàn bộ transcript được lưu tại `../my_workspace/data/ECT-QA/corpus_author/train.jsonl`.

### Bước 2.2: Phân tách Raw Corpus (`create_raw_corpus.py`)

File `.jsonl` tải về chứa tất cả transcripts của mọi công ty trong cùng một file. Script này sẽ đọc JSONL, phân tách nội dung và ghi ra thành từng file `.txt` độc lập, được gom nhóm gọn gàng theo từng thư mục công ty. Tên folder sẽ được chuẩn hóa (xóa ký tự đặc biệt, dấu phẩy...).

**Lệnh chạy:**
```bash
uv run python scripts/data_prep/create_raw_corpus.py \
    --input ../my_workspace/data/ECT-QA/corpus_author/train.jsonl \
    --output ../my_workspace/data/raw_txt/
```

**Kết quả:**
Hệ thống sẽ tạo ra cây thư mục `raw_txt/` chứa khoảng ~120 folders công ty và ~480 files `.txt`.
```text
../my_workspace/data/raw_txt/
├── Crocs_Inc/
│   ├── CROX_consumer_discretionary_2024_q1.txt
│   ├── CROX_consumer_discretionary_2024_q2.txt
│   └── ...
├── Apple_Inc/
└── ...
```

### Bước 2.3: Lọc dữ liệu thô bằng LLM (`preprocess_corpus`)

Đây là khâu quan trọng nhất. Script này đọc các file trong `raw_txt/`, sử dụng local LLM (Ollama - ví dụ `qwen3:14b` hoặc `llama3`) để phân tích từng câu một (sentence unit).

LLM sẽ gắn nhãn từng câu bằng các quyết định:
- `KEEP_FACT`: Giữ lại vì chứa sự kiện kinh doanh, tài chính, biến động thị trường.
- `KEEP_CONTEXT`: Giữ lại vì làm ngữ cảnh neo cho các câu xung quanh.
- `DISCARD`: Xóa bỏ vì là câu rác, thủ tục, pháp lý.
- `MOVE_TO_METADATA`: Lưu làm metadata quy ước tính toán, không đưa vào văn bản sạch.

*Lưu ý: Để chạy bước này, bạn phải đang bật Ollama và đã tải model.*

**Lệnh chạy (Batch cho toàn bộ thư mục):**
```bash
uv run python -m scripts.data_prep.preprocess_corpus \
    --input ../my_workspace/data/raw_txt/ \
    --output ../my_workspace/data/clean_corpus/ \
    --mode batch \
    --model qwen3:14b
```

*(Bạn có thể chạy thử nghiệm trên 1 file duy nhất bằng cách đổi `--mode file` và truyền file vào `--input`)*

**Kết quả (`clean_corpus/`):**
Sau quá trình này, script sẽ trả về một bộ corpus sạch tại `../my_workspace/data/clean_corpus/`.
```text
../my_workspace/data/clean_corpus/
├── Crocs_Inc/
│   └── CROX_consumer_discretionary_2024_q1.txt (Văn bản ĐÃ ĐƯỢC LÀM SẠCH)
├── drop_logs/
│   └── Crocs_Inc/
│       ├── CROX_consumer_discretionary_2024_q1.drop.txt    (Nhật ký những câu bị xóa/giữ)
│       └── CROX_consumer_discretionary_2024_q1.quality.md  (Báo cáo chất lượng Markdown)
└── metadata/
    └── Crocs_Inc/
        └── CROX_consumer_discretionary_2024_q1.metadata.json
```

---

## Bước Tiếp Theo (Chuyển tiếp sang Step 3 - Indexing)

Sau khi Bước 2 hoàn thành, bạn đã có các file `.txt` sạch tinh tươm trong thư mục `my_workspace/data/clean_corpus/Tên_Công_Ty/`.

Để tiến hành khởi chạy GraphRAG (`index`), bạn chỉ việc copy các file `.txt` sạch này vào thư mục `input/` của workspace GraphRAG.

**Ví dụ:**
```bash
# Copy các transcript sạch của công ty Crocs vào input
cp ../my_workspace/data/clean_corpus/Crocs_Inc/*.txt ../my_workspace/input/
```
Sau đó bạn có thể tự tin tiến hành chạy `uv run python -m graphrag index ...` trên thư mục workspace đó. Dữ liệu lúc này đã được khử nhiễu tối đa.
