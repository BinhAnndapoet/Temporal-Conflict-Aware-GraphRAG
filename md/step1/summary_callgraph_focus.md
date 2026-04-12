# GraphRAG Call Graph (function-level) — tuyến `index` và `query`

Tài liệu này tập trung vào **mũi tên hàm gọi hàm** trong `packages/graphrag/graphrag/**` để bạn:

- Debug nhanh (biết lỗi nằm ở chặng nào)
- Custom đúng điểm hook (không sửa nhầm lớp)
- Hiểu rõ *giai đoạn nào làm gì*, *file nào chịu trách nhiệm gì*, *vì sao flow đó cần thiết*

---

## Nguồn đối chiếu chính thống Microsoft (để map với code)

Mình đối chiếu code local với docs/repo Microsoft GraphRAG:

- `https://github.com/microsoft/graphrag`
- `https://microsoft.github.io/graphrag/get_started/`
- `https://microsoft.github.io/graphrag/index/architecture/`
- `https://microsoft.github.io/graphrag/index/default_dataflow/`
- `https://microsoft.github.io/graphrag/index/methods/`
- `https://microsoft.github.io/graphrag/query/overview/`
- `https://microsoft.github.io/graphrag/query/global_search/`
- `https://microsoft.github.io/graphrag/query/local_search/`
- `https://microsoft.github.io/graphrag/query/drift_search/`

> Tinh thần chung theo docs: Indexing là pipeline tạo knowledge artifacts; Query là retrieval engine chạy trên artifacts đã index.

---

## Cách đọc call graph

Mỗi node có dạng:

- `function_name(...)`
- `[folder]` = module folder
- `(phase)` = giai đoạn trong lifecycle

Ví dụ:

- `index_cli(...) [cli] (entry)`
- `build_index(...) [api] (orchestration)`
- `run_pipeline(...) [index/run] (execution)`
- `run_workflow(...) [index/workflows/*] (stage logic)`

---

## 1) Call graph tổng quát tuyến INDEX

## 1.1 Từ CLI (`graphrag index`)

```text
__main__.app()
  -> cli.main._index_cli(...)
    -> cli.index.index_cli(...)
      -> config.load_config.load_config(...)
      -> cli.index._run_index(...)
        -> api.index.build_index(...)
          -> index.workflows.factory.PipelineFactory.create_pipeline(...)
          -> index.run.run_pipeline.run_pipeline(...)
            -> index.run.run_pipeline._run_pipeline(...)
              -> (for each workflow) <workflow_module>.run_workflow(config, context)
```

## 1.2 Từ Python API

```text
import graphrag.api as api
api.build_index(...)
  -> PipelineFactory.create_pipeline(...)
  -> run_pipeline(...)
  -> _run_pipeline(...)
  -> workflow.run_workflow(...)
```

### Vì sao phải qua nhiều lớp?

- `cli/*`: UX + parse tham số
- `api/*`: interface ổn định cho app ngoài
- `factory`: chọn pipeline phù hợp method
- `run_pipeline`: runtime engine + storage/cache/state/callback
- `workflows/*`: nghiệp vụ từng bước

---

## 2) INDEX — pipeline Standard (function-level theo thứ tự chạy)

> Theo docs Microsoft, đây là flow “đủ chất lượng” (LLM-heavy) cho graph giàu ngữ nghĩa.

## 2.1 Sơ đồ mũi tên

```text
load_input_documents.run_workflow
  -> create_base_text_units.run_workflow
  -> create_final_documents.run_workflow
  -> extract_graph.run_workflow
  -> finalize_graph.run_workflow
  -> extract_covariates.run_workflow (optional)
  -> create_communities.run_workflow
  -> create_final_text_units.run_workflow
  -> create_community_reports.run_workflow
  -> generate_text_embeddings.run_workflow
```

## 2.2 Bảng chi tiết từng stage

| Giai đoạn | Hàm chính | File | Folder | Input chính | Output chính | Để làm gì | Vì sao cần |
|---|---|---|---|---|---|---|---|
| Ingest | `run_workflow`, `load_input_documents` | `index/workflows/load_input_documents.py` | `index/workflows` | `input_storage`, `config.input` | table `documents` | Đọc corpus txt/csv/json thành schema chuẩn | Nếu không chuẩn hóa từ đầu, các step sau không dùng chung được |
| Chunking | `run_workflow`, `create_base_text_units`, `chunk_document` | `index/workflows/create_base_text_units.py` | `index/workflows` | `documents` | table `text_units` | Cắt văn bản thành TextUnit + token count + hash id | TextUnit là đơn vị phân tích chính của GraphRAG |
| Document finalize | `run_workflow`, `create_final_documents` | `index/workflows/create_final_documents.py` | `index/workflows` | `documents`, `text_units` | `documents` (final) | Gắn `text_unit_ids` vào document | Bảo toàn provenance document -> chunks |
| Graph extraction | `run_workflow`, `extract_graph`, `get_summarized_entities_relationships` | `index/workflows/extract_graph.py` | `index/workflows` | `text_units`, LLM configs/prompts | `entities`, `relationships` (+ raw snapshots tùy config) | Trích entity/relationship bằng LLM, rồi tóm tắt descriptions | Là bước biến text thô thành graph primitives |
| Graph finalize | `run_workflow`, `finalize_graph`, `_build_degree_map` | `index/workflows/finalize_graph.py` | `index/workflows` | `entities`, `relationships` | entities/relationships enriched | Tính degree/rank và chuẩn hóa field graph | Dùng cho ranking/community detection/query quality |
| Claim extraction | `run_workflow`, `extract_covariates` | `index/workflows/extract_covariates.py` | `index/workflows` | `text_units`, claim prompt/model | `covariates` | Trích claims/covariates (optional) | Bổ sung lớp facts/time-bound cho reasoning |
| Community detection | `run_workflow`, `create_communities` | `index/workflows/create_communities.py` | `index/workflows` | `entities`, `relationships` | `communities` | Leiden hierarchy + parent/children + mappings | Nền tảng cho Global Search |
| Text unit finalize | `run_workflow`, `create_final_text_units` | `index/workflows/create_final_text_units.py` | `index/workflows` | `text_units`, `entities`, `relationships`, `covariates?` | final `text_units` | Reverse-map text_unit -> entity/relationship/covariate IDs | Cho provenance + context build nhanh khi query |
| Community report | `run_workflow`, `create_community_reports` | `index/workflows/create_community_reports.py` | `index/workflows` | entities/relationships/communities/claims | `community_reports` | Sinh report cho từng community bằng LLM | Context nòng cốt của Global Search |
| Embeddings | `run_workflow`, `generate_text_embeddings` | `index/workflows/generate_text_embeddings.py` | `index/workflows` | tables + embedding model | vector indexes (`text_unit_text`, `entity_description`, `community_full_content`) | Sinh vectors cho retrieval | Query modes cần vector search để map/rank |

---

## 3) INDEX — pipeline Fast (khác Standard ở đâu)

> Theo docs `index/methods`: FastGraphRAG hybird NLP + LLM, rẻ và nhanh hơn, đổi lại graph có thể nhiễu hơn.

## 3.1 Sơ đồ mũi tên

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

## 3.2 Điểm khác biệt chính

- `extract_graph_nlp` (`index/workflows/extract_graph_nlp.py`)
  - Dùng NLP noun phrase/co-occurrence thay cho LLM extraction đầy đủ.
- `prune_graph` (`index/workflows/prune_graph.py`)
  - Loại bớt node/edge nhiễu theo ngưỡng thống kê.
- `create_community_reports_text` (`index/workflows/create_community_reports_text.py`)
  - Report cộng đồng xây nhiều hơn từ text units context.

### Khi nào chọn Fast?

- Budget thấp
- Cần chạy nhanh vòng lặp thử nghiệm
- Ưu tiên dataset-level summary hơn graph fidelity chi tiết

---

## 4) INDEX — pipeline Update (incremental)

## 4.1 Sơ đồ mũi tên

```text
cli.main._update_cli
 -> cli.index.update_cli
 -> api.index.build_index(is_update_run=True)
 -> run_pipeline(update-mode)
    -> load_update_documents
    -> [standard hoặc fast core on delta]
    -> update_final_documents
    -> update_entities_relationships
    -> update_text_units
    -> update_covariates
    -> update_communities
    -> update_community_reports
    -> update_text_embeddings
    -> update_clean_state
```

## 4.2 Hàm then chốt update

| Hàm | File | Làm gì | Vì sao quan trọng |
|---|---|---|---|
| `load_update_documents` | `index/workflows/load_update_documents.py` | Diff input mới vs index cũ (`get_delta_docs`) | Tránh full re-index |
| `_update_entities_and_relationships` | `index/workflows/update_entities_relationships.py` | Merge entities/relationships cũ+mới và re-summarize | Giữ consistency semantic |
| `_update_communities` | `index/workflows/update_communities.py` | Merge hierarchy cộng đồng | Bảo toàn structure cho query |
| `_update_community_reports` | `index/workflows/update_community_reports.py` | Merge reports theo community mapping | Global search không mất continuity |
| `update_text_embeddings.run_workflow` | `index/workflows/update_text_embeddings.py` | Rebuild embeddings trên output cập nhật | Retrieval khớp với dữ liệu mới |
| `update_clean_state.run_workflow` | `index/workflows/update_clean_state.py` | Dọn runtime state keys | Tránh rò state giữa run |

---

## 5) Call graph tổng quát tuyến QUERY

## 5.1 Từ CLI (`graphrag query ...`)

```text
__main__.app()
  -> cli.main._query_cli(...)
    -> cli.query.run_<method>_search(...)
      -> config.load_config.load_config(...)
      -> cli.query._resolve_output_files(...)
        -> data_model.data_reader.DataReader.<table>()
      -> api.query.<method>_search(_streaming)
```

`<method>` là: `global`, `local`, `drift`, `basic`.

## 5.2 Từ API

```text
api.query.<method>_search_streaming(...)
  -> query.indexer_adapters.read_indexer_*(...)
  -> utils.api.load_search_prompt(...)
  -> query.factory.get_<method>_search_engine(...)
  -> query.structured_search.<method>.search.<Class>.stream_search(...)
```

---

## 6) QUERY theo từng mode (function-level + mục đích)

## 6.1 Global Search (dataset-level reasoning)

### Mũi tên chính

```text
api.query.global_search_streaming
 -> read_indexer_communities
 -> read_indexer_reports
 -> read_indexer_entities
 -> load_search_prompt(map/reduce/knowledge)
 -> query.factory.get_global_search_engine
 -> GlobalSearch.stream_search
    -> GlobalCommunityContext.build_context
    -> GlobalSearch._map_response_single_batch (parallel)
    -> GlobalSearch._stream_reduce_response
```

### File cốt lõi

- API: `api/query.py`
- Factory: `query/factory.py`
- Engine: `query/structured_search/global_search/search.py`
- Context builder: `query/structured_search/global_search/community_context.py`

### Làm gì & vì sao cần?

- **Map**: mỗi batch community reports -> list points + score
- **Reduce**: gom điểm quan trọng thành final answer
- Phù hợp câu hỏi kiểu “top themes / bức tranh toàn cục” (theo docs Microsoft).

---

## 6.2 Local Search (entity-centric reasoning)

### Mũi tên chính

```text
api.query.local_search_streaming
 -> get_embedding_store(entity_description)
 -> read_indexer_entities/reports/text_units/relationships/covariates
 -> load_search_prompt(local)
 -> query.factory.get_local_search_engine
 -> LocalSearch.stream_search
    -> LocalSearchMixedContext.build_context
       -> map_query_to_entities
       -> _build_community_context
       -> _build_local_context (entity/relationship/covariate)
       -> _build_text_unit_context
```

### File cốt lõi

- Engine: `query/structured_search/local_search/search.py`
- Context builder: `query/structured_search/local_search/mixed_context.py`

### Làm gì & vì sao cần?

- Trộn context có kiểm soát token budget giữa graph + reports + source text.
- Mạnh cho câu hỏi cụ thể quanh thực thể.

---

## 6.3 DRIFT Search (global + local hybrid traversal)

### Mũi tên chính

```text
api.query.drift_search_streaming
 -> get_embedding_store(entity_description)
 -> get_embedding_store(community_full_content)
 -> read_indexer_report_embeddings
 -> query.factory.get_drift_search_engine
 -> DRIFTSearch.stream_search
    -> DRIFTSearch.search(reduce=False)
       -> DRIFTSearchContextBuilder.build_context (primer context)
       -> DRIFTPrimer.search
       -> _process_primer_results -> DriftAction graph
       -> loop n_depth:
            _search_step -> action.search(LocalSearch)
       -> serialize query_state
    -> _reduce_response_streaming
```

### File cốt lõi

- Engine: `query/structured_search/drift_search/search.py`
- Context builder: `query/structured_search/drift_search/drift_context.py`
- Action/state: `query/structured_search/drift_search/action.py`, `state.py`, `primer.py`

### Làm gì & vì sao cần?

- Khởi đầu rộng bằng community-level signal, rồi drill-down local qua follow-up queries.
- Theo docs Microsoft: cân bằng chất lượng và chi phí tốt hơn cho nhiều câu hỏi khó.

---

## 6.4 Basic Search (baseline vector RAG)

### Mũi tên chính

```text
api.query.basic_search_streaming
 -> get_embedding_store(text_unit_text)
 -> read_indexer_text_units
 -> query.factory.get_basic_search_engine
 -> BasicSearch.stream_search
    -> BasicSearchContext.build_context
    -> LLM answer from selected text unit chunks
```

### File cốt lõi

- Engine: `query/structured_search/basic_search/search.py`

### Làm gì & vì sao cần?

- Baseline để so sánh với local/global/drift.
- Dùng tốt cho fact retrieval đơn giản.

---

## 7) Bảng “function -> folder -> phase -> nhiệm vụ” (cheat sheet)

| Function | Folder | Phase | File | Nhiệm vụ |
|---|---|---|---|---|
| `_index_cli` | `cli` | Entry | `cli/main.py` | Nhận lệnh index từ user |
| `index_cli` | `cli` | Orchestration | `cli/index.py` | Nạp config, gọi API build index |
| `build_index` | `api` | API orchestration | `api/index.py` | Chọn method, dựng pipeline, run |
| `create_pipeline` | `index/workflows` | Pipeline composition | `index/workflows/factory.py` | Lấy danh sách workflow theo method |
| `run_pipeline` | `index/run` | Runtime execution | `index/run/run_pipeline.py` | Tạo context/storage/cache và chạy workflow |
| `load_input_documents` | `index/workflows` | Ingest | `load_input_documents.py` | Đọc input vào bảng documents |
| `create_base_text_units` | `index/workflows` | Chunking | `create_base_text_units.py` | Tạo text units |
| `extract_graph` | `index/workflows` | Graph extraction | `extract_graph.py` | Trích entities/relationships bằng LLM |
| `create_communities` | `index/workflows` | Graph augmentation | `create_communities.py` | Leiden community hierarchy |
| `create_community_reports` | `index/workflows` | Summarization | `create_community_reports.py` | Sinh report cho community |
| `generate_text_embeddings` | `index/workflows` | Vectorization | `generate_text_embeddings.py` | Ghi embeddings vào vector store |
| `_query_cli` | `cli` | Entry | `cli/main.py` | Nhận lệnh query từ user |
| `run_global_search` | `cli` | Query orchestration | `cli/query.py` | Đọc bảng output + gọi API global |
| `global_search_streaming` | `api` | API query | `api/query.py` | Adapter dữ liệu + create engine + stream |
| `get_global_search_engine` | `query` | Engine factory | `query/factory.py` | Cấu hình model/context cho Global |
| `GlobalSearch.stream_search` | `query/structured_search` | Query execution | `global_search/search.py` | Map-reduce inference |
| `LocalSearchMixedContext.build_context` | `query/structured_search` | Context building | `local_search/mixed_context.py` | Trộn context graph/text |
| `DRIFTSearch.search` | `query/structured_search` | Iterative search | `drift_search/search.py` | Primer + follow-up + reduce |

---

## 8) Debug nhanh theo call graph (thực chiến)

## 8.1 Lỗi ở index stage nào?

- Nếu lỗi “không có entities”: soi `extract_graph.run_workflow` hoặc `extract_graph_nlp.run_workflow`.
- Nếu lỗi report rỗng: soi `create_community_reports*` + input `communities`.
- Nếu query không tìm thấy gì dù index xong: soi `generate_text_embeddings` + `vector_store` config.

## 8.2 Lỗi query mode nào?

- Global ra câu chung chung: kiểm tra `community_level`, `max_context_tokens`, map/reduce prompts.
- Local thiếu chi tiết: tăng `top_k_entities`, `top_k_relationships`, kiểm tra entity embeddings.
- DRIFT quá dài/đắt: giảm `n_depth`, `drift_k_followups`, `primer_folds`.

---

## 9) Điểm hook để custom an toàn

## 9.1 Custom workflow/pipeline

- File: `index/workflows/factory.py`
- Hook:
  - `PipelineFactory.register(name, workflow_fn)`
  - `PipelineFactory.register_pipeline(name, workflows)`

## 9.2 Custom prompt

- Cách nhẹ: chỉnh `prompts/*.txt` + trỏ đường dẫn trong `settings.yaml`
- Đi qua API helper `load_search_prompt(...)` trong `utils/api.py`

## 9.3 Custom storage/vector/model

- Theo docs architecture “Providers & Factories”: có thể thay implementation qua factory pattern.

---

## 10) Vì sao phải có từng flow?

- **Index flow** tồn tại để chuyển text thô thành graph + summaries + embeddings (mới có retrieval chất lượng).
- **Query flow** tách thành 4 mode vì mỗi loại câu hỏi cần chiến lược context khác nhau:
  - Global: tổng quan dataset
  - Local: thực thể cụ thể
  - DRIFT: khám phá đa nhánh vừa rộng vừa sâu
  - Basic: baseline nhanh

Nếu gộp tất cả vào một flow duy nhất, chất lượng/chi phí khó tối ưu theo từng loại câu hỏi.

---

## 11) Mini map “file nào đọc trước” để nắm flow cực nhanh

1. `graphrag/cli/main.py`
2. `graphrag/cli/index.py`
3. `graphrag/api/index.py`
4. `graphrag/index/workflows/factory.py`
5. `graphrag/index/run/run_pipeline.py`
6. `graphrag/index/workflows/*.py` (theo order standard)
7. `graphrag/cli/query.py`
8. `graphrag/api/query.py`
9. `graphrag/query/factory.py`
10. `graphrag/query/structured_search/*/search.py`

---

## 12) Kết luận ngắn

- Bạn có thể xem GraphRAG như một kiến trúc 2 tầng:
  - **Indexing runtime** (ETL + graph building + summaries + vectors)
  - **Query runtime** (context builder + search engine + LLM response)
- Call graph function-level giúp bạn thấy “đường đi thật” để:
  - debug chính xác,
  - custom đúng điểm,
  - tránh sửa nhầm layer.

Nếu bạn muốn, mình có thể tạo thêm bản `summary_callgraph_matrix.md` dạng **ma trận 2 chiều**:

- Trục dọc: giai đoạn (ingest/chunk/extract/cluster/report/embed/query)
- Trục ngang: file + function + input/output + config knob ảnh hưởng trực tiếp

để bạn dùng như checklist khi tuning hệ thống.