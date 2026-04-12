# GraphRAG Debug Trace theo 1 truy vấn entity cụ thể

Tài liệu này mô phỏng **một phiên query thực tế** theo kiểu debug trace, đi từ CLI đến token stream output.

Mục tiêu:
- Nhìn được đường đi hàm gọi hàm theo thứ tự runtime.
- Hiểu vì sao mỗi stage tồn tại, và vì sao stage phải chạy đúng thứ tự đó.
- Map được giữa lý thuyết GraphRAG (paper + docs Microsoft) và code hiện có trong repo.

---

## 1) Ví dụ truy vấn dùng để trace

Giả sử câu hỏi người dùng:

> **"Entity `NeoChip` có vai trò gì trong hệ sinh thái và liên hệ với các tổ chức nào?"**

Đây là câu hỏi **entity-centric** (tập trung vào một thực thể), nên mode phù hợp nhất là **Local Search**.

Ta chạy dạng streaming:

- `graphrag query --method local --streaming --community-level 2 "Entity NeoChip ..."`

---

## 2) Nền tảng lý thuyết (paper + docs) dùng để giải thích flow

### 2.1 Từ paper GraphRAG (From Local to Global)

Paper nêu pipeline logic:
1. Text -> chunks.
2. Chunks -> entities/relationships/claims.
3. Tạo knowledge graph.
4. Community detection theo hierarchy.
5. Community summaries.
6. Query-time tổng hợp bằng query-focused summarization.

Ý chính cho câu hỏi local:
- Truy vấn không nên chỉ dựa semantic chunk gần nhất như vector RAG.
- Cần **đi qua thực thể và quan hệ** để giữ ngữ cảnh cấu trúc.

### 2.2 Từ docs Microsoft GraphRAG

- Local Search: truy vấn theo thực thể, trộn dữ liệu structured + unstructured.
- Global Search: map-reduce trên community reports cho câu hỏi toàn cục.
- DRIFT: kết hợp global primer + local follow-up.

=> Với query về một entity cụ thể, thứ tự tốt nhất là:

**query -> entity mapping -> relationship/covariate/community/text unit -> LLM response**.

---

## 3) Trace runtime thật: CLI -> token stream (LOCAL)

## 3.1 Entry từ command line

1) `graphrag`
- File: `packages/graphrag/graphrag/__main__.py`
- Hàm: `app(prog_name="graphrag")`
- Vai trò: vào Typer app.

2) Parse subcommand `query`
- File: `packages/graphrag/graphrag/cli/main.py`
- Hàm: `_query_cli(...)`
- Match `SearchMethod.LOCAL` -> gọi `run_local_search(...)`.

**Vì sao tách stage này:**
- CLI chỉ làm nhiệm vụ UX/argument parsing.
- Không gắn business retrieval logic vào CLI để API có thể tái sử dụng.

---

## 3.2 Orchestration ở CLI layer

3) Chuẩn bị config
- File: `packages/graphrag/graphrag/cli/query.py`
- Hàm: `run_local_search(...)`
- Gọi `load_config(...)`.

4) Nạp artifact index từ output storage
- Hàm: `_resolve_output_files(...)`
- Dùng `DataReader` đọc các bảng:
  - `communities`
  - `community_reports`
  - `text_units`
  - `relationships`
  - `entities`
  - optional: `covariates`

5) Chạy streaming API
- Trong `run_local_search(...)`, nếu `streaming=True`:
  - tạo callback (`NoopQueryCallbacks`)
  - override `on_context` để giữ context_data
  - `async for stream_chunk in api.local_search_streaming(...):`
    - `print(stream_chunk, end="")`

**Điểm quan trọng:** token được in ra terminal **ngay khi chunk về**, không đợi full answer.

---

## 3.3 API layer: adapter dữ liệu + build engine

6) API entry
- File: `packages/graphrag/graphrag/api/query.py`
- Hàm: `local_search_streaming(...)`

7) Chuẩn bị embedding store cho entity description
- Gọi `get_embedding_store(..., embedding_name=entity_description_embedding)`.

8) Chuyển bảng thành data model objects
- `read_indexer_entities(...)`
- `read_indexer_reports(...)`
- `read_indexer_text_units(...)`
- `read_indexer_relationships(...)`
- `read_indexer_covariates(...)`

9) Nạp prompt
- `load_search_prompt(config.local_search.prompt)`

10) Tạo LocalSearch engine
- File: `packages/graphrag/graphrag/query/factory.py`
- Hàm: `get_local_search_engine(...)`
- Khởi tạo:
  - completion model
  - embedding model
  - context builder `LocalSearchMixedContext(...)`
  - `context_builder_params` (token split, top_k, ...)

11) Trả async generator
- `return search_engine.stream_search(query=query)`

---

## 3.4 Search engine layer: nơi token stream được phát

12) Thực thi local stream
- File: `packages/graphrag/graphrag/query/structured_search/local_search/search.py`
- Hàm: `LocalSearch.stream_search(...)`

13) Build context trước khi gọi LLM
- `context_result = self.context_builder.build_context(...)`
- callback `on_context(context_result.context_records)`

14) Gọi LLM streaming
- `response = await self.model.completion_async(..., stream=True, ...)`
- `async for chunk in response:`
  - `response_text = chunk.choices[0].delta.content or ""`
  - callback `on_llm_new_token(response_text)`
  - `yield response_text`

15) Quay lại CLI
- `run_local_search(...)` nhận từng chunk, in ra màn hình.

✅ Đây chính là đường **CLI -> token stream output**.

---

## 4) Nội bộ Local context builder (trọng tâm entity query)

File: `packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py`
Hàm: `LocalSearchMixedContext.build_context(...)`

Flow nội bộ:

1. (Optional) nối conversation history vào query.
2. `map_query_to_entities(...)` để lấy các entity gần query nhất trong embedding space.
3. Build community context (`_build_community_context`).
4. Build local graph context (`_build_local_context`): entities -> relationships -> covariates.
5. Build source text context (`_build_text_unit_context`).
6. Ghép tất cả thành `context_chunks` cho prompt.

### Vì sao thứ tự này?

- **Entity trước:** nếu chưa biết query ám chỉ entity nào thì không thể truy quan hệ đúng.
- **Community + local graph sau:** thêm semantic structure trước khi thêm text thô để giữ “khung nhận thức”.
- **Text units cuối:** dùng như evidence/provenance, tránh prompt tràn token quá sớm.

### Nếu đảo thứ tự thì sao?

- Nhét text unit trước: dễ tốn token vào chi tiết không liên quan.
- Lấy relationship trước entity: mất neo ngữ nghĩa, ranking kém ổn định.

---

## 5) Debug trace dạng timeline (bạn có thể đọc như log)

## 5.1 Timeline rút gọn

- `__main__.py: app(...)`
- `cli/main.py: _query_cli(method=LOCAL)`
- `cli/query.py: run_local_search(...)`
- `cli/query.py: _resolve_output_files(...)`
- `api/query.py: local_search_streaming(...)`
- `query/factory.py: get_local_search_engine(...)`
- `local_search/search.py: LocalSearch.stream_search(...)`
- `local_search/mixed_context.py: build_context(...)`
- `entity_extraction.py: map_query_to_entities(...)`
- back to `LocalSearch.stream_search(...)`
- `model.completion_async(stream=True)`
- `yield token chunk`
- `cli/query.py: print(stream_chunk)`

## 5.2 Pseudo debug output

- `[CLI] method=local streaming=true`
- `[CLI] loaded tables: entities, relationships, text_units, reports...`
- `[API] initialized description embedding store`
- `[Factory] LocalSearch engine created`
- `[Context] map_query_to_entities -> top_k entities selected`
- `[Context] build community/local/text context done`
- `[LLM] stream started`
- `[LLM] chunk="NeoChip "`
- `[LLM] chunk="is linked to ..."`
- `[CLI stdout] print each chunk`
- `[LLM] stream completed`

---

## 6) Vì sao stage design như vậy (góc kiến trúc)

## 6.1 Tách CLI / API / Engine

- CLI thay đổi nhanh theo UX.
- API cần ổn định để app khác gọi.
- Engine chứa thuật toán search.

=> Giảm coupling, dễ test độc lập.

## 6.2 Tách ContextBuilder khỏi Search engine

- Builder lo “lấy dữ liệu gì, thứ tự nào, token budget”.
- Engine lo “gọi model ra câu trả lời”.

=> Dễ thay chiến lược context mà không sửa core stream.

## 6.3 Streaming callback riêng

- `on_context`: lấy snapshot context.
- `on_llm_new_token`: hook realtime UI/telemetry.

=> Phục vụ debug, observability, và interactive UX.

---

## 7) Các vấn đề bạn cần nắm để hiểu đúng từng stage

1. **Community level ảnh hưởng độ trừu tượng**
   - level thấp: cụ thể hơn, token nhiều hơn.
   - level cao: khái quát hơn, rẻ hơn.

2. **Top-K entity mapping quyết định recall ban đầu**
   - thấp quá: miss entity liên quan.
   - cao quá: nhiễu + tốn token.

3. **Token budget split (`community_prop`, `text_unit_prop`) là đòn tuning chính**
   - tăng `text_unit_prop`: nhiều bằng chứng nguồn.
   - tăng `community_prop`: nhiều bức tranh cấu trúc.

4. **Embedding quality quyết định “entry point” của local search**
   - Nếu entity description embeddings yếu, cả flow đi sai hướng ngay bước 1.

5. **Prompt form của local search ảnh hưởng output format + factuality**
   - prompt mơ hồ -> stream dài nhưng ít trọng tâm.

---

## 8) Nếu cùng câu hỏi nhưng chạy DRIFT thì flow khác gì?

DRIFT thêm 3 pha:

1. **Primer** (global-ish):
   - `DRIFTSearchContextBuilder.build_context` chọn top reports theo similarity.
   - `DRIFTPrimer.search` sinh intermediate answer + follow-up queries.

2. **Follow-up loop**:
   - mỗi follow-up chạy `DriftAction.search(...)` -> gọi LocalSearch.
   - lặp đến `n_depth` hoặc hết action.

3. **Reduce**:
   - gom cây kết quả trong `QueryState` rồi reduce thành final answer stream.

**Vì sao hữu ích:**
- Query local nhưng ngữ cảnh rộng/đa nhánh vẫn lấy được nhờ primer.
- Chính là triết lý “global guidance, local refinement”.

---

## 9) Mapping nhanh tới file cần mở khi debug

- CLI entry: `packages/graphrag/graphrag/cli/main.py`
- CLI query orchestration: `packages/graphrag/graphrag/cli/query.py`
- API query: `packages/graphrag/graphrag/api/query.py`
- Factory: `packages/graphrag/graphrag/query/factory.py`
- Local stream engine: `packages/graphrag/graphrag/query/structured_search/local_search/search.py`
- Local context internals: `packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py`
- Entity mapping: `packages/graphrag/graphrag/query/context_builder/entity_extraction.py`
- DRIFT core (nếu mở rộng):
  - `query/structured_search/drift_search/search.py`
  - `query/structured_search/drift_search/drift_context.py`
  - `query/structured_search/drift_search/primer.py`
  - `query/structured_search/drift_search/action.py`
  - `query/structured_search/drift_search/state.py`

---

## 10) Kết luận thực chiến

- Với câu hỏi về một entity, Local Search là baseline đúng vì nó đi từ entity anchors tới relationship/text evidence.
- Đường token stream thực tế nằm ở:
  - `LocalSearch.stream_search` (yield chunk)
  - `cli/query.py` (print chunk).
- Design stage theo thứ tự hiện tại không phải ngẫu nhiên; nó bám cả lý thuyết GraphRAG (structure-first reasoning) lẫn tối ưu token-cost trong docs Microsoft.

Nếu bạn muốn, bước tiếp theo mình có thể làm thêm bản **"trace có gắn line number + logpoint gợi ý"** (kiểu breakpoint checklist) để bạn debug trực tiếp trong VS Code cực nhanh.