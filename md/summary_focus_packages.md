# GraphRAG core (packages/graphrag/graphrag) — kiến trúc lõi & luồng gọi CLI/API -> index/query

Tài liệu này chỉ tập trung vào **`packages/graphrag/graphrag/**`** để bạn đọc nhanh phần lõi của GraphRAG Microsoft.

---

## 1) Bức tranh tổng thể: GraphRAG làm gì?

GraphRAG có 2 khối chính:

1. **Indexing**: biến corpus thô thành knowledge artifacts (entities, relationships, communities, community reports, embeddings).
2. **Query**: dùng các artifacts đó để trả lời theo nhiều chiến lược: `global`, `local`, `drift`, `basic`.

Kiến trúc trong code được chia như sau:

- `cli/`: điểm vào dòng lệnh.
- `api/`: public API Python cho app/service gọi trực tiếp.
- `config/`: nạp + validate settings.
- `index/`: pipeline workflow để xây index.
- `query/`: engine truy vấn + context builder.
- `data_model/`: schema/object model + typed dataframe adapters.
- `prompts/`: prompt templates mặc định.
- `callbacks/`, `logger/`, `cache/`: hạ tầng observability và cache.

---

## 2) Entry point thực thi: bắt đầu từ đâu?

## 2.1 Từ CLI

- **File**: `packages/graphrag/graphrag/__main__.py`
  - Gọi `app(prog_name="graphrag")` từ Typer.
- **File**: `packages/graphrag/graphrag/cli/main.py`
  - Khai báo command:
    - `graphrag init`
    - `graphrag index`
    - `graphrag update`
    - `graphrag query`
    - `graphrag prompt-tune`

### Vai trò

CLI là lớp orchestration user-facing: parse options, load config, rồi dispatch về `cli/index.py`, `cli/query.py`, `cli/initialize.py`, ...

## 2.2 Từ Python API

- **File**: `packages/graphrag/graphrag/api/__init__.py`
  - Export API chính:
    - `build_index`
    - `global_search`, `local_search`, `drift_search`, `basic_search` (+ streaming variants)
    - `generate_indexing_prompts`

### Vai trò

Nếu bạn làm service (FastAPI, Flask, notebook), dùng API layer thay vì shell command.

---

## 3) Nạp config và chuẩn bị môi trường

- **File**: `config/load_config.py`
  - Hàm chính: `load_config(root_dir, cli_overrides)`
  - Dùng `graphrag_common.config.load_config` để đọc `settings.yaml|yml|json`.

- **File**: `config/models/graph_rag_config.py`
  - Class: `GraphRagConfig`.
  - Chứa tất cả group config:
    - models (`completion_models`, `embedding_models`)
    - storage (`input_storage`, `output_storage`, `update_output_storage`)
    - workflow knobs (`extract_graph`, `community_reports`, ...)
    - query knobs (`local_search`, `global_search`, `drift_search`, `basic_search`)
  - Hàm quan trọng:
    - `get_completion_model_config(model_id)`
    - `get_embedding_model_config(model_id)`
  - `model_validator` chạy kiểm tra base_dir, vector store schema, ...

- **File**: `config/defaults.py`
  - Mặc định chunking, token budget, top-k, model id, ...

- **File**: `cli/initialize.py` + `config/init_content.py`
  - `graphrag init` sinh:
    - `settings.yaml`
    - `.env`
    - thư mục `prompts/*.txt`

### Vì sao quan trọng?

Đây là “control plane” của GraphRAG: đổi hành vi pipeline/query gần như chủ yếu bằng config thay vì sửa code.

---

## 4) Luồng gọi Indexing: CLI/API -> Pipeline -> Tables

## 4.1 Đường đi từ lệnh

- `cli/main.py` command `index` gọi `cli/index.py:index_cli(...)`
- `cli/index.py`:
  1. `load_config(...)`
  2. (optional) tắt cache
  3. validate config names
  4. gọi `api.build_index(...)`

- `api/index.py:build_index(...)`
  1. `init_loggers(...)`
  2. tạo callback chain
  3. chọn method (`standard|fast|...-update`) qua `_get_method`
  4. `pipeline = PipelineFactory.create_pipeline(config, method)`
  5. chạy `run_pipeline(...)` và yield `PipelineRunResult` cho từng workflow

- `index/run/run_pipeline.py`
  - tạo `input_storage`, `output_storage`, `table_provider`, `cache`
  - nạp state cũ (`context.json`) nếu có
  - chạy tuần tự workflow trong pipeline
  - dump `stats.json` + `context.json`

## 4.2 Cấu trúc pipeline (factory)

- **File**: `index/workflows/factory.py`
  - `PipelineFactory.register_pipeline(...)` đăng ký 4 mode:

### Standard

```text
load_input_documents
-> create_base_text_units
-> create_final_documents
-> extract_graph
-> finalize_graph
-> extract_covariates
-> create_communities
-> create_final_text_units
-> create_community_reports
-> generate_text_embeddings
```

### Fast

```text
load_input_documents
-> create_base_text_units
-> create_final_documents
-> extract_graph_nlp
-> prune_graph
-> finalize_graph
-> create_communities
-> create_final_text_units
-> create_community_reports_text
-> generate_text_embeddings
```

### StandardUpdate / FastUpdate

- bắt đầu bằng `load_update_documents`
- chạy pipeline chuẩn/fast trên delta
- rồi chạy chuỗi merge/update:
  - `update_final_documents`
  - `update_entities_relationships`
  - `update_text_units`
  - `update_covariates`
  - `update_communities`
  - `update_community_reports`
  - `update_text_embeddings`
  - `update_clean_state`

---

## 5) Giải phẫu từng workflow chuẩn (standard) — input, output, tác dụng

## 5.1 `load_input_documents`

- **File**: `index/workflows/load_input_documents.py`
- **Input**: `input_storage` qua `create_input_reader(config.input, ...)`
- **Output table**: `documents`
- **Core**:
  - parse tài liệu từ txt/csv/json
  - thêm `human_readable_id`
  - fail nếu total_count = 0

### Vì sao cần?

Chuẩn hóa đầu vào thành một bảng `documents` để mọi bước sau dùng chung schema.

## 5.2 `create_base_text_units`

- **File**: `index/workflows/create_base_text_units.py`
- **Input table**: `documents`
- **Output table**: `text_units`
- **Core**:
  - dùng `chunker` (`graphrag_chunking`) cắt text thành chunk
  - optional prepend metadata
  - tạo `id` theo hash (`gen_sha512_hash`)
  - tính `n_tokens`

### Vì sao cần?

Text unit là đơn vị hạt mịn cho extraction và provenance.

## 5.3 `create_final_documents`

- **File**: `index/workflows/create_final_documents.py`
- **Input**: `documents`, `text_units`
- **Output**: overwrite `documents` với schema final (có `text_unit_ids`)

### Vì sao cần?

Map ngược từ document sang text units để truy vết nguồn.

## 5.4 `extract_graph` (LLM extraction)

- **File**: `index/workflows/extract_graph.py`
- **Input**: `text_units`
- **Output tables**: `entities`, `relationships` (+ optional `raw_entities`, `raw_relationships`)
- **Core**:
  - tạo completion model cho extraction prompt
  - tạo completion model cho summarize descriptions
  - `extract_graph(...)` tách entity/relationship theo text unit
  - kiểm tra rỗng (nếu không có entity/relationship -> error)
  - summarize descriptions để có mô tả cô đọng cuối cùng

### Vì sao cần?

Đây là bước biến text thành knowledge graph primitives.

## 5.5 `finalize_graph`

- **File**: `index/workflows/finalize_graph.py`
- **Input**: `entities`, `relationships`
- **Output**: entities/relationships đã finalize (degree/rank fields)
- **Core**:
  - build degree map từ edges
  - finalize entities + relationships
  - optional snapshot graphml

### Vì sao cần?

Chuẩn hóa graph features (độ kết nối, rank) để clustering và retrieval tốt hơn.

## 5.6 `extract_covariates` (optional claims)

- **File**: `index/workflows/extract_covariates.py`
- **Input**: `text_units`
- **Output**: `covariates` (nếu `extract_claims.enabled = true`)
- **Core**:
  - LLM claim extraction
  - gán UUID cho covariate rows

### Vì sao cần?

Bổ sung lớp facts/claims (time-bound/status) cho phân tích sâu hơn.

## 5.7 `create_communities`

- **File**: `index/workflows/create_communities.py`
- **Input**: `entities`, `relationships`
- **Output**: `communities`
- **Core**:
  - chạy hierarchical Leiden (`cluster_graph`)
  - aggregate `entity_ids`, `relationship_ids`, `text_unit_ids`
  - build parent/children tree

### Vì sao cần?

Tạo cấu trúc phân cấp semantic communities — nền tảng cho Global Search.

## 5.8 `create_final_text_units`

- **File**: `index/workflows/create_final_text_units.py`
- **Input**: `text_units`, `entities`, `relationships`, optional `covariates`
- **Output**: final `text_units`
- **Core**:
  - reverse lookup maps:
    - text_unit -> entity_ids
    - text_unit -> relationship_ids
    - text_unit -> covariate_ids

### Vì sao cần?

Giúp query/retrieval có provenance và context assembly nhanh.

## 5.9 `create_community_reports`

- **File**: `index/workflows/create_community_reports.py`
- **Input**: `relationships`, `entities`, `communities`, optional `claims`
- **Output**: `community_reports`
- **Core**:
  - explode communities -> node membership
  - build local context per community
  - LLM summarize community
  - finalize report

### Vì sao cần?

Community report là tài liệu tóm tắt semantic dùng trực tiếp cho Global Search.

## 5.10 `generate_text_embeddings`

- **File**: `index/workflows/generate_text_embeddings.py`
- **Input tables**: `text_units`, `entities`, `community_reports`
- **Output**:
  - vector store indexes cho
    - `text_unit_text`
    - `entity_description`
    - `community_full_content`
  - optional snapshots `embeddings.*`

### Vì sao cần?

Cung cấp vector retrieval cho Basic/Local/DRIFT và hỗ trợ ranking.

---

## 6) Fast mode khác Standard ở đâu?

## 6.1 `extract_graph_nlp`

- **File**: `index/workflows/extract_graph_nlp.py`
- Dùng NLP noun phrase extraction (`build_noun_graph`) thay vì LLM graph extraction.
- Nhanh hơn, rẻ hơn, nhưng thường ít semantic richness hơn.

## 6.2 `prune_graph`

- **File**: `index/workflows/prune_graph.py`
- Cắt node/edge nhiễu theo threshold (freq, degree, edge weight percentile, ego node, LCC).

## 6.3 `create_community_reports_text`

- **File**: `index/workflows/create_community_reports_text.py`
- Report được summarize từ **text units context** (không dựa sâu vào graph descriptions như standard graph report).

---

## 7) Incremental update: dữ liệu mới đi như thế nào?

## 7.1 Bắt đầu bằng delta detection

- **File**: `index/workflows/load_update_documents.py`
  - đọc input hiện tại
  - so sánh với output cũ (`previous_table_provider`) qua `get_delta_docs`
  - chỉ lấy `new_inputs`

## 7.2 Chạy pipeline trên delta output

`run_pipeline` (update mode) tạo storage timestamped:

- `delta/` (index mới cho dữ liệu mới)
- `previous/` (backup index cũ)

## 7.3 Merge sang output chính

Các workflow update merge dữ liệu:

- `update_final_documents.py`: concat documents cũ + mới
- `update_entities_relationships.py`: group/resolve entities, merge relationships, re-summarize descriptions
- `update_communities.py`: merge community hierarchy
- `update_community_reports.py`: merge reports theo mapping community id
- `update_text_embeddings.py`: cập nhật embeddings
- `update_clean_state.py`: dọn keys `incremental_update_*`

### Ý nghĩa

Bạn không cần full re-index mỗi lần có tài liệu mới.

---

## 8) Luồng Query: CLI/API -> adapters -> search engine

## 8.1 Từ CLI

- **File**: `cli/query.py`
- Với từng method (`global/local/drift/basic`):
  1. load config
  2. đọc output tables qua `DataReader`
  3. gọi API tương ứng (streaming hoặc non-streaming)

## 8.2 Từ API

- **File**: `api/query.py`
- Quy trình chung:
  1. typed adapters (`read_indexer_*`) chuyển dataframe -> object model
  2. load prompt file từ config (nếu có override)
  3. tạo search engine qua `query/factory.py`
  4. gọi `search()` hoặc `stream_search()`

## 8.3 Factory tạo engine

- **File**: `query/factory.py`
- Hàm:
  - `get_global_search_engine(...)`
  - `get_local_search_engine(...)`
  - `get_drift_search_engine(...)`
  - `get_basic_search_engine(...)`

Mỗi engine dựng:

- completion model
- embedding model (nếu cần)
- context builder tương ứng
- tokenizer + model params + callback

---

## 9) Bản chất từng mode query (khác nhau ở context builder)

## 9.1 Global Search

- **Engine**: `query/structured_search/global_search/search.py`
- **Context builder**: `global_search/community_context.py`
- Mô hình map-reduce:
  1. build nhiều context chunks từ community reports
  2. map: LLM trả các `points` có `description` + `score`
  3. reduce: gom điểm cao thành câu trả lời cuối

### Hợp với câu hỏi

- “Top 5 themes trong toàn corpus là gì?”
- câu hỏi tổng quan/dataset-level sensemaking.

## 9.2 Local Search

- **Engine**: `query/structured_search/local_search/search.py`
- **Context builder**: `local_search/mixed_context.py`
- Flow:
  1. map query -> entities (vector lookup trên entity description embeddings)
  2. ghép context theo tỷ lệ:
     - community context (`community_prop`)
     - local graph context (entity/relationship/covariate)
     - text unit context (`text_unit_prop`)
  3. LLM trả lời trong một context window

### Hợp với câu hỏi

- “Entity X liên quan gì đến Y?”
- câu hỏi cụ thể quanh thực thể.

## 9.3 DRIFT Search

- **Engine**: `query/structured_search/drift_search/search.py`
- **Context builder**: `drift_search/drift_context.py`
- Ý tưởng:
  1. primer tìm top cộng đồng liên quan bằng embedding similarity
  2. sinh follow-up queries (drift actions)
  3. chạy lặp local-search theo depth (`n_depth`)
  4. reduce kết quả thành câu trả lời cuối

### Hợp với câu hỏi

- cần vừa local vừa mở rộng khám phá nhiều hướng liên quan.

## 9.4 Basic Search

- **Engine**: `query/structured_search/basic_search/search.py`
- baseline vector RAG thuần trên text units.

### Hợp với câu hỏi

- câu hỏi fact retrieval đơn giản, không cần reasoning graph-level.

---

## 10) Ví dụ thực tế theo code path

## Ví dụ A — chạy index chuẩn

1. User chạy `graphrag index --method standard`.
2. `cli/main.py` -> `cli/index.py:index_cli` -> `api.build_index`.
3. `PipelineFactory` chọn chuỗi `standard` workflows.
4. `run_pipeline` chạy tuần tự từng workflow, ghi:
   - `documents`, `text_units`, `entities`, `relationships`, `communities`, `community_reports`
   - embeddings vào vector store.
5. Output stats/context lưu `output/stats.json`, `output/context.json`.

## Ví dụ B — query global

1. User chạy `graphrag query "Top 5 themes" --method global`.
2. `cli/query.py:run_global_search` đọc `entities`, `communities`, `community_reports`.
3. `api.global_search_streaming`:
   - adapter dataframe -> objects
   - load map/reduce prompts
   - `get_global_search_engine` -> `GlobalSearch`.
4. `GlobalSearch.stream_search` map từng batch reports rồi reduce thành câu trả lời.

## Ví dụ C — query local

1. User hỏi: “Novorossiya đã làm gì?” (entity-centric).
2. `LocalSearchMixedContext` map query -> entity candidates.
3. Context builder trộn:
   - community snippets
   - relationships/covariates liên quan
   - source text units có độ liên quan cao.
4. `LocalSearch` gọi LLM trả lời + provenance context.

---

## 11) Các file nên đọc đầu tiên (nếu học codebase)

Theo thứ tự “hiểu hệ thống nhanh”:

1. `graphrag/cli/main.py`
2. `graphrag/api/index.py`
3. `graphrag/index/workflows/factory.py`
4. `graphrag/index/run/run_pipeline.py`
5. `graphrag/index/workflows/*.py` (10 workflow chuẩn)
6. `graphrag/api/query.py`
7. `graphrag/query/factory.py`
8. `graphrag/query/structured_search/{global,local,drift,basic}/search.py`
9. `graphrag/query/structured_search/local_search/mixed_context.py`
10. `graphrag/query/structured_search/global_search/community_context.py`

---

## 12) Tại sao kiến trúc này đáng dùng?

- Tách rõ **orchestration** (CLI/API) và **business pipeline** (index/query engines).
- Pipeline dạng workflow giúp dễ thay custom step.
- Config-driven: đổi model/prompt/storage mà ít sửa code.
- Có cả standard (chất lượng cao) và fast (chi phí thấp).
- Có incremental update cho production.
- Query engine đa chiến lược, phù hợp nhiều kiểu câu hỏi.

---

## 13) Gợi ý thực hành để hiểu sâu hơn

1. Chạy cùng một query với cả 4 mode (`global/local/drift/basic`) và so output/context.
2. Chỉnh `community_prop`, `text_unit_prop`, `top_k_entities` trong `local_search` để xem chất lượng thay đổi.
3. Bật/tắt `dynamic_community_selection` ở `global_search` để thấy trade-off tốc độ/chất lượng.
4. So sánh `standard` vs `fast` trên cùng dataset về:
   - thời gian index
   - độ phong phú entities/relationships
   - chất lượng answer ở global/local queries.

Nếu bạn muốn, mình có thể làm tiếp một bản **`summary_callgraph_focus.md`** chỉ gồm call graph dạng mũi tên (function-level) cho 2 tuyến chính:

- `index`: command -> API -> pipeline runner -> từng workflow
- `query`: command -> API -> factory -> context builder -> search

để bạn dùng như “bản đồ debug” khi đọc code.