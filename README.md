# Temporal-Conflict-Aware-GraphRAG

Hướng dẫn chuẩn để chạy **baseline GraphRAG** với **workspace nằm ngoài repo code**, tối ưu cho việc bạn tiếp tục custom logic trong repo mà không làm bẩn source.

> Mục tiêu của README này: chạy được pipeline tới bước `index` (xây dựng graph) một cách ổn định.

---

## 1) Vì sao nên để workspace ở ngoài repo?

- **An toàn bảo mật**: `.env` (API key) và dữ liệu thật trong `input/` nằm ngoài repo, tránh commit nhầm.
- **Repo code luôn sạch**: các thư mục sinh ra như `output/`, `cache/`, `prompts/`, `logs/` không tràn vào source.
- **Dễ mở rộng**: một codebase dùng cho nhiều workspace dữ liệu khác nhau (`my_workspace`, `project_luat`, `project_y_te`, ...).

---

## 2) Nguyên tắc sống còn khi custom code

Nếu bạn sửa code trong `Temporal-Conflict-Aware-GraphRAG`, hãy luôn chạy lệnh từ **thư mục repo code** (không chạy trong thư mục workspace).

Luồng chuẩn:

1. Đứng tại repo code.
2. `uv sync --all-packages` (hoặc `uv sync`) để đồng bộ môi trường.
3. Chạy CLI qua `uv run ...` + `--root <đường_dẫn_workspace_ngoài_repo>`.

### `uv sync --all-packages` có tác dụng gì?

- Đọc `pyproject.toml` + `uv.lock`.
- Tạo/cập nhật `.venv`.
- Cài dependencies đúng phiên bản đã khóa.
- Sync toàn bộ workspace members (phù hợp monorepo nhiều package).
- Cài project theo chế độ editable, nên sửa code là chạy lại thấy hiệu lực ngay.

### Khi nào cần chạy lại `uv sync`?

- Vừa pull code mới có thay đổi dependency.
- `pyproject.toml` thay đổi.
- `uv.lock` thay đổi.
- `.venv` lỗi hoặc muốn làm sạch môi trường.

> Không cần sync lại chỉ vì bạn sửa vài file Python.

---

## 3) Quy trình baseline: từ setup tới `index`

### Bước 0 — Setup repo lần đầu (chạy 1 lần)

Đứng trong thư mục repo code:

```bash
uv sync --all-packages
```

### Bước 1 — Tạo workspace bên ngoài repo

Ví dụ tạo `my_workspace` nằm ngoài `Temporal-Conflict-Aware-GraphRAG`.

**Ubuntu/Linux:**

```bash
mkdir -p /home/user_name/path/my_workspace/input
```

**Windows (PowerShell/CMD):**

```bash
mkdir D:\RAG\my_workspace
mkdir D:\RAG\my_workspace\input
```

### Bước 2 — Khởi tạo workspace bằng `init`

Đứng trong repo code `Temporal-Conflict-Aware-GraphRAG`:

**Ubuntu/Linux:**

```bash
uv run python -m graphrag init --root /home/user_name/path/my_workspace
```

**Windows:**

```bash
uv run python -m graphrag init --root D:\RAG\my_workspace
```

Sau bước này workspace sẽ có các file/thư mục quan trọng như:

- `settings.yaml`
- `.env`
- `input/`

### Trường hợp dùng OpenAI API (rất hay gặp)

Khi bạn chạy `init`, CLI có thể hỏi nhanh phần cấu hình model/provider. Với flow OpenAI, sau khi bạn gắn key vào `.env` (hoặc cung cấp key theo cách CLI yêu cầu), hệ thống thường scaffold sẵn cấu hình cần thiết trong workspace, bao gồm cả `settings.yaml` với model mặc định.

Mặc định thường thấy:

- LLM: `gpt-4.1`
- Embedding: `text-embedding-3-large`

> Vì vậy với case OpenAI, bạn có thể hiểu theo thứ tự thực tế: **init workspace → gắn OpenAI key vào `.env` → kiểm tra/lưu `settings.yaml` đã được tạo sẵn → chạy `index`**.

> Nếu `settings.yaml` đã được scaffold đúng theo mặc định bạn muốn, không bắt buộc chỉnh tay thêm.

> `init` chỉ chạy 1 lần cho mỗi workspace. Nếu thấy `Project already initialized at ...` thì không phải lỗi, chỉ cần chuyển sang bước kế tiếp.

### Bước 3 — Cấu hình `.env`, `settings.yaml`, và dữ liệu input

1. Mở `<workspace>/.env` và điền API key.
2. Mở `<workspace>/settings.yaml` để chỉnh model/chunk/pipeline.
3. Đưa dữ liệu vào `<workspace>/input/` (ví dụ `data.txt`).

Gợi ý nhanh:

- **Dùng OpenAI**: thường chỉ cần xác nhận `OPENAI_API_KEY` + kiểm tra model mặc định (`gpt-4.1`, `text-embedding-3-large`) là đủ để chạy baseline.
- **Dùng Ollama/local**: bắt buộc đối chiếu đúng tên model thực tế trong máy.

### Kiểm tra model backend trước khi `index` (đặc biệt khi dùng Ollama)

```bash
ollama list
curl http://localhost:11434/api/tags
```

Đảm bảo `model:` trong `settings.yaml` **khớp chính xác** với tên model thật trong máy.

Nếu không khớp, thường gặp lỗi:

```text
model '...' not found
```

### Bước 4 — Chạy `index` để build baseline graph

Đứng trong repo code `Temporal-Conflict-Aware-GraphRAG`:

**Ubuntu/Linux:**

```bash
uv run python -m graphrag index --root /home/user_name/path/my_workspace
```

**Windows:**

```bash
uv run python -m graphrag index --root D:\RAG\my_workspace
```

Kết quả sinh ra sẽ nằm trong workspace ngoài repo (`output/`, `cache/`, `prompts/`, `logs/`), giúp source code luôn gọn sạch.

---

## 4) Checklist trước khi chạy `init` / `index`

- [ ] Đang đứng đúng thư mục repo code `Temporal-Conflict-Aware-GraphRAG`
- [ ] Đã chạy `uv sync --all-packages` (hoặc `uv sync`)
- [ ] Workspace nằm ngoài repo code
- [ ] Sau `init`, workspace có `settings.yaml`, `.env`, `input/`
- [ ] Nếu dùng OpenAI: `.env` đã có key hợp lệ (ví dụ `OPENAI_API_KEY=...`)
- [ ] Nếu dùng Ollama: `ollama list` hiển thị đúng model
- [ ] `settings.yaml` dùng đúng model name thực tế
- [ ] `input/data.txt` đã có dữ liệu đầu vào
- [ ] Dữ liệu có câu hoàn chỉnh, có ngữ cảnh và mô tả quan hệ thực thể

---

## 5) Kiểm tra log/output sau khi `index`

### Ubuntu/Linux

```bash
tail -n 100 /tmp/graphrag_index.log
tail -n 100 /home/user_name/path/my_workspace/logs/indexing-engine.log
find /home/user_name/path/my_workspace/output -maxdepth 3 -type f | sort
```

### Windows

- Mở `my_workspace\logs\indexing-engine.log`
- Kiểm tra file sinh ra trong `my_workspace\output`

---

## 6) Lỗi thường gặp và cách xử lý nhanh

### 1. `Project already initialized at ...`

**Ý nghĩa**: Workspace đã `init` rồi.  
**Xử lý**: Không chạy lại `init`, chuyển sang `index`.

### 2. `No module named graphrag`

**Ý nghĩa**: Môi trường `uv` chưa sync đúng.  
**Xử lý**: Chạy lại:

```bash
uv sync --all-packages
```

### 3. `model '...' not found`

**Ý nghĩa**: `settings.yaml` dùng sai tên model.  
**Xử lý**:

1. `ollama list`
2. `curl http://localhost:11434/api/tags`
3. Sửa `settings.yaml` để `model:` khớp đúng tên model thật

### 4. `Graph Extraction failed. No relationships detected during extraction`

**Ý nghĩa**:

- Môi trường đang chạy được.
- Pipeline đã tới bước extract graph.
- Nhưng dữ liệu đầu vào chưa đủ thông tin quan hệ.

**Xử lý**:

- Cải thiện nội dung trong `input/`.
- Dùng câu hoàn chỉnh thay vì bullet rời rạc.
- Mô tả rõ thực thể + sự kiện + quan hệ + thời gian/địa điểm.

---

## 7) (Tham khảo) Các lệnh CLI khác

```bash
uv run python -m graphrag query --root /home/user_name/path/my_workspace --method global "Câu hỏi của bạn"
```

Tóm tắt:

- `init`: Tạo workspace (1 lần)
- `prompt-tune`: Tinh chỉnh prompt mồi (thường trước `index`)
- `index`: Build đồ thị tri thức
- `query`: Truy vấn hỏi đáp
- `update`: Cập nhật graph khi có dữ liệu mới theo thời gian

---

## 8) Data Preprocessing Scripts

Repo bao gồm pipeline chuẩn bị dữ liệu ECT-QA (earnings call transcripts) nằm trong `scripts/data_prep/`. Tất cả lệnh chạy từ **thư mục repo code**.

### Cấu trúc

```
scripts/data_prep/
├── download_data.py              # Tải ECT-QA dataset từ HuggingFace
├── create_raw_corpus.py          # JSONL → raw_txt/ (cây thư mục theo công ty)
└── preprocess_corpus/            # LLM filter → clean_corpus/
    ├── __main__.py               # CLI entry point
    ├── constants.py              # Prompts, decision sets
    ├── parsing.py                # Transcript parsing
    ├── ollama.py                 # Ollama API interaction
    ├── processing.py             # Batch processing, retry logic
    └── writers.py                # File I/O, reports
```

### Pipeline E2E (Step 0 → 4)

```bash
# Đứng tại repo code
cd /path/to/Temporal-Conflict-Aware-GraphRAG

# Step 0: Sync dependencies (1 lần)
uv sync --all-packages

# Step 1: Init workspace (1 lần)
mkdir -p ../my_workspace/input
uv run python -m graphrag init --root ../my_workspace

# Step 2: Download ECT-QA dataset (1 lần)
uv run python scripts/data_prep/download_data.py \
    --output-dir ../my_workspace/data

# Step 3: Tạo raw corpus
uv run python scripts/data_prep/create_raw_corpus.py \
    --input ../my_workspace/data/ECT-QA/corpus_author/train.jsonl \
    --output ../my_workspace/data/raw_txt/

# Step 4: Preprocess → clean corpus (cần Ollama đang chạy)
uv run python -m scripts.data_prep.preprocess_corpus \
    --input ../my_workspace/data/raw_txt/ \
    --output ../my_workspace/data/clean_corpus/ \
    --mode batch --model qwen3:14b
```

### Workspace data sau pipeline

```
my_workspace/data/
├── ECT-QA/corpus_author/train.jsonl   ← download_data.py
├── raw_txt/                           ← create_raw_corpus.py
│   ├── Crocs_Inc/
│   └── ...(~120 folders, ~480 files)
└── clean_corpus/                      ← preprocess_corpus
    ├── Crocs_Inc/*.txt
    ├── drop_logs/                     ← audit logs
    └── metadata/                      ← document metadata
```

---

## 9) Kết luận

Để chạy baseline ổn định tới `index`, chỉ cần nhớ 3 điểm:

1. Workspace đặt ngoài repo.
2. Luôn chạy lệnh từ repo code bằng `uv run ... --root <workspace>`.
3. Đảm bảo model trong `settings.yaml` khớp model thật và input có chất lượng quan hệ tốt.