# Temporal-Conflict-Aware-GraphRAG

Hướng dẫn chuẩn để chạy **baseline GraphRAG** với **workspace nằm ngoài repo code**, tối ưu cho việc bạn tiếp tục custom logic trong repo mà không làm bẩn source.

> Mục tiêu của README này: chạy được **Microsoft GraphRAG baseline** tới bước `index` một cách ổn định trước, sau đó mới phát triển các bước Temporal Document Extraction/custom research pipeline.

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

> Quan trọng: `init` chỉ tạo skeleton workspace, `settings.yaml`, `.env`, và prompt files. Với OpenAI default, file sinh ra thường dùng được gần như ngay. Với Ollama/local, **không được hiểu rằng chọn model trong CLI là đã đủ cấu hình**.

### Trường hợp dùng OpenAI API (rất hay gặp)

Khi bạn chạy `init`, CLI có thể hỏi nhanh phần cấu hình model/provider. Với flow OpenAI, sau khi bạn gắn key vào `.env` (hoặc cung cấp key theo cách CLI yêu cầu), hệ thống thường scaffold sẵn cấu hình cần thiết trong workspace, bao gồm cả `settings.yaml` với model mặc định.

Mặc định thường thấy:

- LLM: `gpt-4.1`
- Embedding: `text-embedding-3-large`

> Vì vậy với case OpenAI, bạn có thể hiểu theo thứ tự thực tế: **init workspace → gắn OpenAI key vào `.env` → kiểm tra/lưu `settings.yaml` đã được tạo sẵn → chạy `index`**.

> Nếu `settings.yaml` đã được scaffold đúng theo mặc định bạn muốn, không bắt buộc chỉnh tay thêm.

> `init` chỉ chạy 1 lần cho mỗi workspace. Nếu thấy `Project already initialized at ...` thì không phải lỗi, chỉ cần chuyển sang bước kế tiếp.

### Trường hợp dùng Ollama/local baseline

GraphRAG `init` hiện chỉ thay tên `--model` và `--embedding` vào template mặc định. Template mặc định vẫn có thể là `model_provider: openai`, không tự thêm `api_base`, không tự cấu hình LanceDB vector dimension, và cũng không biết embedding model local có vector size bao nhiêu.

Vì vậy flow đúng cho Ollama là:

```text
kiểm tra Ollama backend/model thật
→ init workspace một lần
→ sửa settings.yaml sang Ollama preset đúng model + vector size
→ chạy preprocessing bằng preprocessing model
→ đưa clean .txt vào input
→ chạy index bằng GraphRAG completion model + embedding model
```

Không tạo sẵn `settings.yaml` trước khi chạy `init`. Nếu `settings.yaml` đã tồn tại, `init` sẽ báo `Project already initialized...`; nếu dùng `--force`, file cấu hình bạn sửa thủ công có thể bị ghi đè.

Trước khi init/index, kiểm tra backend:

**Ubuntu/Linux:**

```bash
ollama list
curl http://localhost:11434/api/tags
```

**Windows (PowerShell):**

```powershell
ollama list
curl.exe http://localhost:11434/api/tags
```

Chọn các giá trị thật từ máy của bạn:

```text
OLLAMA_CHAT_MODEL            model dùng chung cho GraphRAG completion và Step 2 preprocessing, ví dụ llama3.1:latest
OLLAMA_EMBED_MODEL           model embedding riêng, ví dụ nomic-embed-text:latest
OLLAMA_BASE_URL              thường là http://localhost:11434
OLLAMA_EMBED_DIM             phụ thuộc embedding model, ví dụ nomic-embed-text = 768
```

Nếu model mặc định chưa có, pull explicit:

```bash
ollama pull llama3.1:latest
ollama pull nomic-embed-text:latest
```

Ví dụ cấu hình chung cho workspace:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_CHAT_MODEL=llama3.1:latest
export OLLAMA_EMBED_MODEL=nomic-embed-text:latest
export OLLAMA_EMBED_DIM=768
```

> `OLLAMA_CHAT_MODEL` là model chat/completion dùng chung cho GraphRAG và preprocessing. `OLLAMA_EMBED_MODEL` không dùng cho preprocessing vì đó là model vector embedding.

Ví dụ init skeleton sau khi đã chọn model:

**Ubuntu/Linux:**

```bash
uv run python -m graphrag init \
    --root /home/user_name/path/my_workspace \
    --model "$OLLAMA_CHAT_MODEL" \
    --embedding "$OLLAMA_EMBED_MODEL"
```

**Windows (PowerShell):**

```powershell
uv run python -m graphrag init `
    --root D:\RAG\my_workspace `
    --model $env:OLLAMA_CHAT_MODEL `
    --embedding $env:OLLAMA_EMBED_MODEL
```

Sau đó mở `<workspace>/settings.yaml` và đảm bảo có các cấu hình quan trọng sau:

```yaml
concurrent_requests: 1

completion_models:
  default_completion_model:
    model_provider: ollama
    model: ${OLLAMA_CHAT_MODEL}
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: ${OLLAMA_BASE_URL}
    call_args:
      temperature: 0
      top_p: 0.9
      timeout: 900
    retry:
      type: exponential_backoff

embedding_models:
  default_embedding_model:
    model_provider: ollama
    model: ${OLLAMA_EMBED_MODEL}
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: ${OLLAMA_BASE_URL}
    retry:
      type: exponential_backoff

vector_store:
  type: lancedb
  db_uri: output/lancedb
  vector_size: ${OLLAMA_EMBED_DIM}
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

Với `nomic-embed-text:latest`, `OLLAMA_EMBED_DIM` là `768`. Nếu đổi embedding model hoặc vector size, hãy tạo workspace mới hoặc xóa output/cache/vector store cũ trước khi chạy lại `index`.

```bash
rm -rf /home/user_name/path/my_workspace/output
rm -rf /home/user_name/path/my_workspace/cache
```

**Lưu ý baseline:** repo giữ prompt Microsoft GraphRAG dạng relationship 5-field và parser hiện tương thích cả 5-field baseline lẫn 6-field có `relation_type` để phục vụ extension sau này. Khi smoke test local, có thể set tạm:

```yaml
extract_graph:
  max_gleanings: 0
```

Khi model/prompt ổn rồi mới cân nhắc tăng lại `max_gleanings: 1`.

### Bước 3 — Cấu hình `.env`, `settings.yaml`, và dữ liệu input

1. Mở `<workspace>/.env` và điền API key.
2. Mở `<workspace>/settings.yaml` để chỉnh model/chunk/pipeline.
3. Đưa dữ liệu vào `<workspace>/input/` (ví dụ `data.txt`).

Gợi ý nhanh:

- **Dùng OpenAI**: thường chỉ cần xác nhận `OPENAI_API_KEY` + kiểm tra model mặc định (`gpt-4.1`, `text-embedding-3-large`) là đủ để chạy baseline.
- **Dùng Ollama/local**: bắt buộc đối chiếu đúng tên model thực tế trong máy và kiểm tra `model_provider`, `api_base`, `embedding model`, `vector_size`.

### Kiểm tra model backend trước khi `index` (đặc biệt khi dùng Ollama)

```bash
ollama list
curl http://localhost:11434/api/tags
```

Đảm bảo `model:` trong `settings.yaml` **khớp chính xác** với tên model thật trong máy.

Baseline Ollama đã test trong workspace mẫu:

- Completion LLM: `llama3.1:latest`
- Embedding model: `nomic-embed-text:latest`
- Vector size: `768`
- Preprocessing filter model: cùng `OLLAMA_CHAT_MODEL`

Lưu ý: Step 2 preprocessing mặc định đọc `OLLAMA_CHAT_MODEL` nếu bạn dùng `--env-file <workspace>/.env` hoặc đã `source` file `.env`. Nếu đổi sang Qwen cho GraphRAG index, cần kiểm tra kỹ chat template/thinking mode vì parser vẫn yêu cầu tuple output rõ ràng.

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
- [ ] Nếu dùng Ollama: `ollama list` hiển thị đúng completion model, embedding model, và preprocessing model
- [ ] Nếu dùng Ollama: `settings.yaml` đã chuyển sang `model_provider: ollama`, có `api_base`, và `vector_size` khớp embedding model
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
- Nhưng GraphRAG không thu được relationship hợp lệ sau khi parse output LLM.

**Xử lý**:

- Kiểm tra dữ liệu trong `input/` có đủ câu hoàn chỉnh, thực thể, sự kiện, quan hệ, thời gian/địa điểm.
- Kiểm tra `<workspace>/prompts/extract_graph.txt` nếu đang dùng local model như Qwen/Llama.
- Với model local, tránh để model trả Markdown, JSON, bullet list, giải thích từng bước, hoặc `<think>...</think>` trong output extract graph.
- Output nên là tuple records thuần như:

```text
("entity"<|>AON<|>ORGANIZATION<|>Aon is the company discussed in the earnings call)
##
("relationship"<|>GREG CASE<|>AON<|>CEO_OF<|>Greg Case is Aon's CEO<|>10)
<|COMPLETE|>
```

Nếu model trả kiểu sau thì GraphRAG parser dễ fail hoặc drop relationship:

```text
### Entities
- AON

### Relationships
1. AON is related to COVID-19
```

hoặc:

```json
{"entities": [...], "relationships": [...]}
```

> Benchmark script của repo tự patch `prompts/extract_graph.txt` sang prompt strict có `/no_think` và tuple-only output để giảm lỗi này.

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

### Pipeline E2E: Ollama baseline + ECT-QA preprocessing

Pipeline này dùng **cùng một workspace** từ `init` tới preprocessing và `index`. Step preprocessing không chạy `graphrag init` lại.

```bash
# Đứng tại repo code
cd /home/guest/Projects/Research/GraphRAG/Temporal-Conflict-Aware-GraphRAG

# Step 0: Sync dependencies (1 lần)
uv sync --all-packages

# Step 1: Tạo workspace ngoài repo
mkdir -p ../my_workspace/input

# Step 1.1: Chọn model dùng chung cho GraphRAG completion và preprocessing
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_CHAT_MODEL=llama3.1:latest
export OLLAMA_EMBED_MODEL=nomic-embed-text:latest
export OLLAMA_EMBED_DIM=768

# Step 2: Init skeleton workspace (1 lần)
uv run python -m graphrag init \
    --root ../my_workspace \
    --model "$OLLAMA_CHAT_MODEL" \
    --embedding "$OLLAMA_EMBED_MODEL"

# Step 2.1: Ghi các biến Ollama vào workspace .env để index/preprocess dùng lại
cat > ../my_workspace/.env <<EOF
GRAPHRAG_API_KEY=OLLAMA_DUMMY_KEY
OLLAMA_BASE_URL=${OLLAMA_BASE_URL}
OLLAMA_CHAT_MODEL=${OLLAMA_CHAT_MODEL}
OLLAMA_EMBED_MODEL=${OLLAMA_EMBED_MODEL}
OLLAMA_EMBED_DIM=${OLLAMA_EMBED_DIM}
EOF

# Step 3: Kiểm tra Ollama model thật trong máy
ollama list
curl http://localhost:11434/api/tags

# Step 4: Sửa ../my_workspace/settings.yaml sang Ollama preset chuẩn
# Bắt buộc kiểm tra:
# - completion model: ${OLLAMA_CHAT_MODEL}
# - embedding model: ${OLLAMA_EMBED_MODEL}
# - model_provider: ollama
# - api_base: http://localhost:11434
# - vector_size: 768

# Step 5: Download ECT-QA dataset (1 lần)
uv run python scripts/data_prep/download_data.py \
    --output-dir ../my_workspace/data

# Step 6: Tạo raw corpus
uv run python scripts/data_prep/create_raw_corpus.py \
    --input ../my_workspace/data/ECT-QA/corpus_author/train.jsonl \
    --output ../my_workspace/data/raw_txt/

# Step 7: Preprocess raw corpus → clean corpus
uv run python -m scripts.data_prep.preprocess_corpus \
    --env-file ../my_workspace/.env \
    --input ../my_workspace/data/raw_txt/ \
    --output ../my_workspace/data/clean_corpus/ \
    --mode batch \
    --batch-size 20 \
    --review-batch-size 20 \
    --context-window 1 \
    --review-window 1 \
    --fallback-policy abort
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

### Chuẩn bị `input/` cho GraphRAG index

Không copy toàn bộ `clean_corpus/` vào `input/`, vì GraphRAG đọc đệ quy các file `.txt`. Nếu copy nhầm `drop_logs/*.drop.txt`, baseline sẽ index cả log.

Chỉ đưa clean document `.txt` vào `input/`; bỏ qua:

- `drop_logs/`
- `metadata/`
- `*.drop.txt`
- `*.quality.md`
- `*.analysis.json`

Ví dụ chạy thử với một công ty:

```bash
cp ../my_workspace/data/clean_corpus/Crocs_Inc/*.txt ../my_workspace/input/
```

Sau đó chạy baseline index:

```bash
uv run python -m graphrag index --root ../my_workspace
```

Baseline pass khi workspace có các artifact:

```text
output/documents.parquet
output/text_units.parquet
output/entities.parquet
output/relationships.parquet
output/community_reports.parquet
```

---

## 9) Benchmark local: 2 files × 3 model flows

Repo có script benchmark E2E để đo cùng một flow:

```text
tạo workspace
→ init GraphRAG
→ ghi settings/.env
→ preprocess 1 raw transcript bằng preprocess model
→ copy clean .txt vào input/
→ chạy graphrag index bằng index model
→ lưu benchmark_report.json
```

Script liên quan:

```text
scripts/benchmark_e2e.sh
scripts/data_prep/prepare_graphrag_input.py
configs/settings.ollama.optimized.yaml
```

### Cách chạy benchmark

Đứng tại repo code:

```bash
cd /home/guest/Projects/Research/GraphRAG/Temporal-Conflict-Aware-GraphRAG
```

Kiểm tra model và GPU:

```bash
ollama list
ollama ps
nvidia-smi
```

Chọn 2 raw files:

```bash
AON=/home/guest/Projects/Research/GraphRAG/my_workspace/data/raw_txt/Aon_plc/AON_financials_2020_q1.txt
CROX=/home/guest/Projects/Research/GraphRAG/my_workspace/data/raw_txt/Crocs_Inc/CROX_consumer_discretionary_2020_q1.txt
```

Set Ollama tuning trước khi chạy:

```bash
export OLLAMA_NUM_PARALLEL=2
export OLLAMA_MAX_LOADED_MODELS=2
export OLLAMA_FLASH_ATTENTION=1
```

Chạy benchmark:

```bash
bash scripts/benchmark_e2e.sh "$AON" qwen3:14b optimized
bash scripts/benchmark_e2e.sh "$CROX" qwen3:14b optimized
bash scripts/benchmark_e2e.sh "$AON" llama3.1:latest optimized
bash scripts/benchmark_e2e.sh "$CROX" llama3.1:latest optimized

# Hybrid: Qwen preprocesses, Llama indexes.
bash scripts/benchmark_e2e.sh "$AON" qwen3:14b optimized llama3.1:latest
bash scripts/benchmark_e2e.sh "$CROX" qwen3:14b optimized llama3.1:latest
```

Tham số thứ 2 là **preprocessing model**. Tham số thứ 4, nếu có, là **GraphRAG index/completion model**. Nếu không truyền tham số thứ 4, script dùng cùng một model cho cả preprocessing và index.

Mỗi run tạo workspace riêng ở thư mục cha của repo, dạng:

```text
../bench_<file>_<model>_<timestamp>/
../bench_<file>_pre_<preprocess_model>__idx_<index_model>_<timestamp>/   # hybrid
```

### Benchmark pass khi có gì?

Một run được xem là pass khi workspace benchmark có:

```text
benchmark_report.json
preprocess.log
index.log
data/clean_corpus/
input/
output/documents.parquet
output/text_units.parquet
output/entities.parquet
output/relationships.parquet
output/communities.parquet
output/community_reports.parquet
output/lancedb/
```

### Metric Retention đo gì?

`Retention` là metric của **preprocessing**, không phải metric chất lượng knowledge graph.

Công thức trong code:

```text
Retention (%) = sentence_units_after / sentence_units_before * 100
```

Trong đó:

- `sentence_units_before`: tổng số sentence units được parser tách ra từ raw transcript.
- `sentence_units_after`: số sentence units cuối cùng được giữ trong `clean_corpus`.
- Sentence units được giữ thường có decision `KEEP_FACT` hoặc `KEEP_CONTEXT`.
- Sentence units không vào `clean_corpus` thường là `DISCARD` hoặc `MOVE_TO_METADATA`.

Ví dụ AON với Qwen preprocessing:

```text
sentence_units_before = 143
sentence_units_after  = 122
Retention             = 122 / 143 * 100 = 85.3%
```

Nghĩa là 85.3% sentence units ban đầu được giữ để đưa vào GraphRAG index. Retention cao hơn cho thấy preprocessing giữ nhiều nội dung hơn, nhưng **không tự động chứng minh model tốt hơn**. Nếu giữ cả boilerplate, disclaimer, lời chào, hoặc text không có quan hệ entity/event thì Retention cao vẫn có thể xấu.

Đọc Retention cùng các metric sau:

- `fallback_count`: số lần model output lỗi/không parse được và phải fallback.
- `final_discarded`: số sentence units bị loại.
- `moved_to_metadata`: số sentence units chuyển sang metadata, không đưa vào clean corpus.
- `rescued_by_review`: số sentence units ban đầu bị loại nhưng được review cứu lại.
- Số rows trong `output/entities.parquet` và `output/relationships.parquet`.

Xem Retention của một run:

```bash
# Các run mới sau khi script được cập nhật sẽ có block này:
jq '.preprocess_quality' <workspace>/benchmark_report.json

# Cách luôn đúng là đọc report gốc của preprocessing:
jq '.quality_report' <workspace>/data/clean_corpus/drop_logs/*/*.analysis.json
```

Xem nhanh kết quả:

```bash
find /home/guest/Projects/Research/GraphRAG \
  -maxdepth 2 \
  -path '*/benchmark_report.json' \
  -type f \
  | sort

cat /home/guest/Projects/Research/GraphRAG/bench_*/benchmark_report.json
```

### Kết quả benchmark hiện tại

Hardware:

```text
GPU: NVIDIA GeForce RTX 5070 Ti, 16GB VRAM
Embedding: nomic-embed-text:latest, vector size 768
Settings: optimized
concurrent_requests: 2
embed_text.batch_size: 16
embed_text.batch_max_tokens: 8192
extract_graph.max_gleanings: 0
```

Kết quả 2 files:

| Flow | File | Preprocess | Index | Total | Retention | Entities | Relationships | Reports |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Llama only: `llama3.1` → `llama3.1` | AON Q1 2020 | 2218s | 219s | 2442s | 75.5% | 9 | 1 | 1 |
| Llama only: `llama3.1` → `llama3.1` | CROX Q1 2020 | 3133s | 362s | 3500s | 75.3% | 14 | 12 | 2 |
| Qwen only: `qwen3:14b` → `qwen3:14b` | AON Q1 2020 | 290s | 359s | 653s | 85.3% | 18 | 18 | 2 |
| Qwen only: `qwen3:14b` → `qwen3:14b` | CROX Q1 2020 | 451s | 344s | 800s | 80.8% | 22 | 18 | 2 |
| Hybrid: `qwen3:14b` → `llama3.1` | AON Q1 2020 | 295s | 402s | 700s | 85.3% | 10 | 8 | 2 |
| Hybrid: `qwen3:14b` → `llama3.1` | CROX Q1 2020 | 452s | 217s | 674s | 80.8% | 19 | 23 | 1 |

`Entities`, `Relationships`, và `Reports` là số rows trong:

```text
output/entities.parquet
output/relationships.parquet
output/community_reports.parquet
```

Đọc kết quả:

- `qwen3:14b` nhanh hơn nhiều ở preprocessing trong pipeline JSON 3-pass hiện tại.
- `llama3.1:latest` nhanh hơn ở một số bước indexing như `extract_graph`, nhưng thua rất xa end-to-end vì preprocessing quá lâu.
- Hybrid giữ Retention giống Qwen-only vì cùng dùng Qwen cho preprocessing; khác biệt nằm ở graph extraction/community report của index model.
- Hybrid không thắng tuyệt đối: AON hybrid chậm hơn Qwen-only và sinh ít graph rows hơn; CROX hybrid nhanh hơn Qwen-only và sinh nhiều relationships hơn, nhưng ít community reports hơn.
- `qwen3:14b` giữ high-recall tốt hơn Llama-only trong 2 file test: retention cao hơn và fallback count bằng 0.
- Embedding tối ưu rõ rệt nhờ `batch_size: 16`, không còn là bottleneck chính như cấu hình `batch_size: 1`.

Khuyến nghị hiện tại:

```text
Baseline local thực dụng:
qwen3:14b cho preprocessing
→ clean_corpus
→ qwen3:14b cho GraphRAG indexing làm baseline mặc định
→ chỉ dùng hybrid qwen3:14b preprocessing + llama3.1 indexing nếu benchmark thêm cho thấy file/company cụ thể chạy nhanh hơn mà graph artifacts vẫn đủ tốt
```

Với 2 file hiện tại, Qwen-only là lựa chọn ổn định nhất để tiếp tục baseline. Hybrid đáng giữ lại như một biến thể benchmark, nhưng chưa đủ bằng chứng để thay thế Qwen-only cho full batch.

### Vì sao prompt `extract_graph.txt` phải strict?

GraphRAG baseline không đọc mọi kiểu output tự nhiên của LLM. Bước `extract_graph` parse response bằng delimiter cố định:

```text
tuple delimiter: <|>
record delimiter: ##
completion delimiter: <|COMPLETE|>
```

Vì vậy local LLM phải trả đúng tuple records. Benchmark script ghi đè `<workspace>/prompts/extract_graph.txt` bằng prompt strict:

```text
/no_think

Return ONLY tuple records.
Do NOT return Markdown headings, bullet lists, JSON, code fences, explanations, notes, or a final-answer section.
Every entity must use exactly:
("entity"<|><entity_name><|><entity_type><|><entity_description>)
Every relationship must use exactly:
("relationship"<|><source_entity><|><target_entity><|><relation_type><|><relationship_description><|><relationship_strength>)
Use ## between records.
End with <|COMPLETE|>.
```

Lý do cần `/no_think`:

- Qwen3 có thinking mode; nếu model sinh `<think>...</think>` hoặc phân tích trung gian, output có thể lẫn text ngoài tuple.
- Với GraphRAG parser, text ngoài tuple không phải chỉ “xấu format”; nó có thể làm record bị parse sai, entity/relationship bị bỏ qua, hoặc relationship bị drop vì source/target không match entity đã parse.
- Với indexing baseline, ưu tiên output máy đọc được hơn là câu trả lời tự nhiên đẹp.

Nếu bạn sửa prompt này, hãy test lại trên 1 file trước. Không chạy batch lớn khi chưa thấy đủ:

```text
output/entities.parquet
output/relationships.parquet
output/community_reports.parquet
```

### Cảnh báo khi chạy full batch

Không nên chạy thẳng 480 files ngay sau khi đổi model/prompt/settings. Lộ trình an toàn:

```text
1 file
→ 2 files
→ 1 company folder
→ vài company folders
→ full 480 files
```

Nếu đổi model, prompt, embedding dimension, hoặc vector store settings, nên dùng workspace mới hoặc xóa generated artifacts:

```bash
rm -rf <workspace>/output
rm -rf <workspace>/cache
```

Không xóa `data/raw_txt`, `data/clean_corpus`, hoặc source repo nếu chỉ muốn rerun index.

---

## 10) Kết luận

Để chạy baseline ổn định tới `index`, chỉ cần nhớ 3 điểm:

1. Workspace đặt ngoài repo.
2. Luôn chạy lệnh từ repo code bằng `uv run ... --root <workspace>`.
3. Đảm bảo model trong `settings.yaml` khớp model thật và input có chất lượng quan hệ tốt.
