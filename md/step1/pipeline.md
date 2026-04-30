# Pipeline Setup Guide: OpenAI → Ollama Local

Hướng dẫn chi tiết từng bước để chuyển từ **OpenAI API** sang **Ollama local** — bao gồm cả nguyên nhân root cause tại sao Ollama crash và cách fix.

**Đọc trước:** `step_1_overview.md` → rồi đọc file này để setup thành công.

---

## Mục lục

1. [So sánh nhanh: OpenAI vs Ollama](#1-so-sánh-nhanh-openai-vs-ollama)
2. [Root Cause: Tại sao Ollama crash khi index?](#2-root-cause-tại-sao-ollama-crash-khi-index)
3. [Bước 0 — Kiểm tra Ollama đang chạy](#3-bước-0--kiểm-tra-ollama-đang-chạy)
4. [Bước 1 — Init workspace cho Ollama](#4-bước-1--init-workspace-cho-ollama)
5. [Bước 2 — Sửa `.env` cho Ollama](#5-bước-2--sửa-env-cho-ollama)
6. [Bước 3 — Sửa `settings.yaml` — 5 nhóm cần thay đổi](#6-bước-3--sửa-settingsyaml--5-nhóm-cần-thay-đổi)
7. [Bước 4 — Sửa `settings.yaml` — Vector Store (quan trọng nhất)](#7-bước-4--sửa-settingsyaml--vector-store-quan-trọng-nhất)
8. [Bước 5 — Thêm dữ liệu đầu vào](#8-bước-5--thêm-dữ-liệu-đầu-vào)
9. [Bước 6 — Chạy Index](#9-bước-6--chạy-index)
10. [Bước 7 — Query](#10-bước-7--query)
11. [Troubleshooting](#11-troubleshooting)
12. [Tóm tắt: 6 thứ cần thay đổi khi chuyển sang Ollama](#12-tóm-tắt-6-thứ-cần-thay-đổi-khi-chuyển-sang-ollama)

---

## 1. So sánh nhanh: OpenAI vs Ollama

| | OpenAI | Ollama Local |
|---|---|---|
| **API Key** | Cần `OPENAI_API_KEY` thật | Chỉ cần dummy key |
| **Sau `init`** | Gần như hoàn chỉnh, chỉ cần điền key | **Cần sửa tay nhiều thứ** |
| **Completion model** | `gpt-4.1` | `${OLLAMA_CHAT_MODEL}` |
| **Embedding model** | `text-embedding-3-large` (**3072 chiều**) | `${OLLAMA_EMBED_MODEL}` |
| **Index crash** | ✅ Không | ⚠️ **Có — dimension mismatch** |

### Điều cần nhớ

- **OpenAI:** sau `init`, chỉ cần điền API key vào `.env` → chạy `index` ngay được.
- **Ollama:** sau `init`, **bắt buộc phải sửa tay 5-6 chỗ** trong `settings.yaml` và `.env` — nếu không sẽ crash.

---

## 2. Root Cause: Tại sao Ollama crash khi index?

### Bug chain — theo dõi từ source code

```
graphrag init
  → scaffold settings.yaml từ INIT_YAML (init_content.py)
  → vector_store: CHỈ có type + db_uri, KHÔNG có vector_size, KHÔNG có index_schema

graphrag index
  → gọi validate_config_names(config) (cli/index.py:109)
  → tạo embedding LLM, gọi thực tế
  → _sync_vector_store_dimensions() ← GHI ĐÈ vector_size TỰ ĐỘNG theo embedding thực tế!
  → ⚠️ NHƯNG: nếu index schema đã tồn tại (từ lần chạy trước), nó vẫn giữ vector_size CŨ (3072)
  → LanceDB create_index(): tạo schema với vector_size cũ
  → nomic-embed-text sinh vector 768 chiều → MISMATCH → crash

THÊM NỮA:
  → _validate_vector_store() (graph_rag_config.py:253)
  → nếu index_schema rỗng → TỰ ĐỘNG tạo 3 schemas với default_vector_size = 3072
  → tạo vector 3072 chiều
  → Ollama gửi vector 768 chiều → MISMATCH → RuntimeError
```

### Hai nơi code gây crash

**Nơi 1:** `packages/graphrag/graphrag/index/validate_config.py`

```python
# _sync_vector_store_dimensions() — chỉ override khi vector_size CHƯA KHỚP
# NHƯNG: nếu workspace đã chạy OpenAI trước, index_schema cũ còn đó (3072)
# → không override → crash khi Ollama gửi vector 768
```

**Nơi 2:** `packages/graphrag/graphrag/config/models/graph_rag_config.py`

```python
# _validate_vector_store() — tự tạo 3 schemas nếu index_schema rỗng
# MẶC ĐỊNH: vector_size = DEFAULT_VECTOR_SIZE = 3072
# → tạo schema 3072 chiều
# → Ollama gửi vector 768 → MISMATCH → crash
```

**Nơi 3:** `packages/graphrag-vectors/graphrag_vectors/index_schema.py`

```python
DEFAULT_VECTOR_SIZE: int = 3072  # ← giá trị cố định
# Cả INIT_YAML lẫn VectorStoreDefaults đều KHÔNG ghi đè giá trị này
```

### Mấu chốt nằm ở đâu?

Sau `init`, `settings.yaml` có:

```yaml
vector_store:
  type: lancedb
  db_uri: output/lancedb
  # vector_size: ??? (không có → dùng default 3072)
  # index_schema: ??? (không có → _validate_vector_store tự tạo 3 schemas 3072)
```

→ GraphRAG tự tạo schemas với **3072 chiều** (OpenAI mặc định).
→ Ollama `nomic-embed-text` sinh vector **768 chiều** → crash.

### Cách fix

Sau `init`, **bắt buộc** thêm vào `settings.yaml`:

```yaml
vector_store:
  type: lancedb
  vector_size: 768              # ← phải khớp với nomic-embed-text
  db_uri: output/lancedb
  index_schema:
    text_unit_text:
      index_name: text_unit_text
      vector_size: 768          # ← cả 3 đều phải 768
    entity_description:
      index_name: entity_description
      vector_size: 768
    community_full_content:
      index_name: community_full_content
      vector_size: 768
```

---

## 3. Bước 0 — Kiểm tra Ollama đang chạy

**Rất quan trọng:** phải chạy trước khi làm mọi thứ khác.

```bash
ollama list
curl http://localhost:11434/api/tags
```

Kết quả mong đợi:

```
NAME                       ID              SIZE      MODIFIED
nomic-embed-text:latest    0a109f422b47    274 MB    ...
llama3.1:latest            46e0c10c039e    4.9 GB    ...
```

**Lưu ý:** Tên model **phải khớp chính xác** kể cả suffix `:latest`.
- ✅ `llama3.1:latest`
- ❌ `llama3.1` (thiếu `:latest`)

Chọn model một lần bằng biến môi trường, rồi dùng lại cho Step 1 và Step 2:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_CHAT_MODEL=llama3.1:latest
export OLLAMA_EMBED_MODEL=nomic-embed-text:latest
export OLLAMA_EMBED_DIM=768
```

`OLLAMA_CHAT_MODEL` là model completion dùng cho GraphRAG `index/query` và cũng là model mặc định cho `scripts.data_prep.preprocess_corpus` nếu bạn không truyền `--model`. `OLLAMA_EMBED_MODEL` là model embedding riêng; không dùng nó cho preprocessing.

---

## 4. Bước 1 — Init workspace cho Ollama

### Cách chạy đúng

```bash
# Ubuntu/Linux
mkdir -p /home/manh/Projects/ban/my_workspace_ollama/input
uv run python -m graphrag init --root /home/manh/Projects/ban/my_workspace_ollama \
  --model "$OLLAMA_CHAT_MODEL" --embedding "$OLLAMA_EMBED_MODEL"
```

### Tại sao phải truyền `--model` và `--embedding`?

```
Không có flags
  → Typer prompt tương tác
  → Mặc định = gpt-4.1 (OpenAI)
  → settings.yaml scaffold cho OpenAI → sau này phải sửa lại tất cả

Có flags --model và --embedding
  → Typer không prompt
  → settings.yaml scaffold đúng model → giảm bớt chỗ phải sửa
```

> ⚠️ **Bắt buộc truyền cả hai flags** khi dùng Ollama. Không có flags, Typer sẽ prompt tương tác và mặc định là `gpt-4.1`.

### Nếu workspace đã init rồi (cho OpenAI)?

```bash
# Không cần chạy lại init
# Chỉ cần sửa .env và settings.yaml (các bước 2, 3, 4 bên dưới)
```

Thông báo `Project already initialized at ...` **không phải lỗi** — workspace đã có `settings.yaml`. Bỏ qua init, sang bước 2.

---

## 5. Bước 2 — Sửa `.env` cho Ollama

Mở file `.env` trong workspace, thay đổi:

```bash
# Trước đây (OpenAI)
GRAPHRAG_API_KEY=sk-proj-...your-real-key...

# Bây giờ (Ollama)
GRAPHRAG_API_KEY=OLLAMA_DUMMY_KEY
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_CHAT_MODEL=llama3.1:latest
OLLAMA_EMBED_MODEL=nomic-embed-text:latest
OLLAMA_EMBED_DIM=768
```

Với Ollama, API key không dùng thật — chỉ cần giá trị placeholder để qua validation. Các biến `OLLAMA_*` giúp GraphRAG settings và Step 2 preprocessing dùng cùng một model chat/base URL.

---

## 6. Bước 3 — Sửa `settings.yaml` — 5 nhóm cần thay đổi

### Nhóm 1: Completion Models

Tìm block `completion_models` trong `settings.yaml`, sửa thành:

```yaml
completion_models:
  default_completion_model:
    model_provider: ollama
    model: ${OLLAMA_CHAT_MODEL}      # ← phải khớp chính xác với ollama list
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: ${OLLAMA_BASE_URL}     # ← THÊM dòng này
    retry:
      type: exponential_backoff
```

### Nhóm 2: Embedding Models

Tìm block `embedding_models`, sửa thành:

```yaml
embedding_models:
  default_embedding_model:
    model_provider: ollama
    model: ${OLLAMA_EMBED_MODEL}     # ← phải khớp chính xác với ollama list
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: ${OLLAMA_BASE_URL}     # ← THÊM dòng này
    retry:
      type: exponential_backoff
```

### Nhóm 3: Chunking (tùy chọn — khuyến nghị)

```yaml
chunking:
  size: 500      # ← giảm từ 1200 xuống 500 cho Ollama local (model nhỏ hơn)
  overlap: 80
  encoding_model: o200k_base
```

### Nhóm 4: Embed Text (tùy chọn — khuyến nghị)

```yaml
embed_text:
  embedding_model_id: default_embedding_model
  batch_size: 1     # ← giảm từ 16 xuống 1 cho Ollama local
  batch_max_tokens: 1024
  names: [entity_description, community_full_content, text_unit_text]
```

### Nhóm 5: Performance (quan trọng — khuyến nghị thêm nếu chưa có)

```yaml
# Thêm vào cuối settings.yaml hoặc chỗ phù hợp
concurrent_requests: 1   # ← giữ thấp, Ollama local không chịu được concurrent cao
```

---

## 7. Bước 4 — Sửa `settings.yaml` — Vector Store (quan trọng nhất)

### Tìm block `vector_store`, THAY THẾ hoàn toàn bằng:

```yaml
vector_store:
  type: lancedb
  db_uri: output/lancedb
  vector_size: ${OLLAMA_EMBED_DIM}   # ← BẮT BUỘC: khớp embedding model
  index_schema:
    text_unit_text:
      index_name: text_unit_text
      vector_size: ${OLLAMA_EMBED_DIM}
    entity_description:
      index_name: entity_description
      vector_size: ${OLLAMA_EMBED_DIM}
    community_full_content:
      index_name: community_full_content
      vector_size: ${OLLAMA_EMBED_DIM}
```

### Lưu ý quan trọng

- **`vector_size`**: phải là `768` — không phải `3072` (OpenAI), không phải giá trị khác.
- **`index_name`**: phải khớp chính xác với tên trong `embed_text.names`:
  - `text_unit_text`
  - `entity_description`
  - `community_full_content`
- Nếu thiếu `vector_size` hoặc `index_schema` → crash với lỗi `Expected vector dimension 3072, got 768`.

### Mẹo: kiểm tra nhanh

Sau khi sửa, chạy:

```bash
grep -A5 "vector_store:" /home/manh/Projects/ban/my_workspace_ollama/settings.yaml
```

Kết quả đúng phải có cả `vector_size: 768` và `index_schema` với 3 entries.

---

## 8. Bước 5 — Thêm dữ liệu đầu vào

```bash
cp your_document.txt /home/manh/Projects/ban/my_workspace_ollama/input/
```

### Lưu ý về dữ liệu

- Dùng **câu hoàn chỉnh**, có **ngữ cảnh**, có **mô tả quan hệ** giữa các thực thể.
- **Không nên** dùng bullet rời rạc, từ khóa đơn lẻ, text quá ngắn.
- Nếu pipeline chạy đến `extract_graph` nhưng báo `No relationships detected` → dữ liệu đầu vào chưa đủ tốt, **không phải lỗi môi trường**.

Repo hiện giữ prompt Microsoft GraphRAG baseline 5-field cho relationship và parser đã tương thích cả 5-field baseline lẫn 6-field có `relation_type` cho extension sau này. Vì vậy khi chạy baseline, không cần sửa prompt `prompts/extract_graph.txt` chỉ để thêm `relation_type`.

---

## 9. Bước 6 — Chạy Index

```bash
# Ubuntu/Linux
uv run python -m graphrag index --root /home/manh/Projects/ban/my_workspace_ollama

# Windows
uv run python -m graphrag index --root D:\RAG\my_workspace_ollama
```

### Kiểm tra kết quả

```bash
# Ubuntu/Linux
tail -n 100 /home/manh/Projects/ban/my_workspace_ollama/logs/indexing-engine.log
find /home/manh/Projects/ban/my_workspace_ollama/output -maxdepth 3 -type f | sort
```

Output đúng phải có:
- `output/documents.parquet`
- `output/text_units.parquet`
- `output/entities.parquet`
- `output/relationships.parquet`
- `output/communities.parquet`
- `output/community_reports.parquet`
- `output/lancedb/` (vector store)

---

## 10. Bước 7 — Query

```bash
# Ubuntu/Linux
uv run python -m graphrag query \
  --root /home/manh/Projects/ban/my_workspace_ollama \
  --method global "Câu hỏi của bạn"

# Windows
uv run python -m graphrag query ^
  --root D:\RAG\my_workspace_ollama ^
  --method global "Câu hỏi của bạn"
```

Các mode query:
- `global` — câu hỏi tổng quan, toàn bộ corpus
- `local` — câu hỏi về thực thể cụ thể
- `drift` — kết hợp global + local
- `basic` — vector similarity cơ bản

---

## 11. Troubleshooting

### `Project already initialized at ...`

**Ý nghĩa:** Workspace đã có `settings.yaml`. **Không phải lỗi.**

**Cách xử lý:** Bỏ qua bước `init`, tiếp tục bước 2 trở đi.

---

### `No module named graphrag`

**Ý nghĩa:** Môi trường `uv` chưa sync.

**Cách xử lý:**

```bash
uv sync --all-packages
```

---

### `model 'llama3.1' not found`

**Ý nghĩa:** Tên model trong `settings.yaml` không khớp Ollama.

**Cách xử lý:**

1. Chạy `ollama list` để xem tên chính xác
2. Sửa `settings.yaml` để `model:` khớp đúng tên + version

---

### `RuntimeError: LanceDB: Expected vector dimension 3072, got 768`

**Ý nghĩa:** `vector_size` và `index_schema` trong `settings.yaml` chưa được sửa.

**Cách xử lý:** Làm đúng **Bước 4** — thêm `vector_size: 768` và `index_schema` đầy đủ.

---

### `Graph Extraction failed. No relationships detected during extraction`

**Ý nghĩa:** Pipeline chạy được đến bước `extract_graph`, nhưng dữ liệu đầu vào không sinh ra relationship nào.

**Cách xử lý:**
- Kiểm tra lại `input/data.txt`
- Dùng dữ liệu có câu hoàn chỉnh, có mô tả quan hệ rõ ràng giữa các thực thể

---

## 12. Tóm tắt: 6 thứ cần thay đổi khi chuyển sang Ollama

| # | Thứ cần thay đổi | OpenAI (mặc định) | Ollama (cần sửa) |
|---|---|---|---|
| 1 | `.env` | `GRAPHRAG_API_KEY=sk-...` | `GRAPHRAG_API_KEY=OLLAMA_DUMMY_KEY` |
| 2 | `completion_models[].model_provider` | `openai` | `ollama` |
| 3 | `completion_models[].model` | `gpt-4.1` | `${OLLAMA_CHAT_MODEL}` |
| 4 | `embedding_models[].model_provider` | `openai` | `ollama` |
| 5 | `embedding_models[].model` | `text-embedding-3-large` | `${OLLAMA_EMBED_MODEL}` |
| 6 | `vector_store` | **Không cần sửa** | ⚠️ **Bắt buộc** thêm `vector_size: ${OLLAMA_EMBED_DIM}` + `index_schema` đầy đủ |

**Đã test ✅:** Index + Query 100% thành công với Ollama local sau khi áp dụng đầy đủ 6 thay đổi trên.
