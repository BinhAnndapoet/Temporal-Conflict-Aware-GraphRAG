# task_extraction.md

## Mục tiêu tài liệu

Tài liệu này chuyển trạng thái hiện tại của bạn (**đã chạy index mẫu thành công**) sang kế hoạch triển khai cụ thể cho bài toán **Document_Extraction** theo hướng **Temporal Conflict-Aware GraphRAG**.

Nó bám theo:
- Kiến trúc và flow GraphRAG hiện có trong repo.
- Yêu cầu từ `Document_Extraction.pdf` + `GraphRAG - Proposal.docx`.
- Các ý tưởng từ paper/docs: GraphRAG, TG-RAG, T-GRAG (temporal extraction, temporal consistency, incremental update).

---

## Trạng thái hiện tại (đã xác minh)

Bạn đã có workspace chạy được index ở `my_workspace_openai`, với output chuẩn:
- `documents.parquet`
- `text_units.parquet`
- `entities.parquet`
- `relationships.parquet`
- `communities.parquet`
- `community_reports.parquet`
- `context.json`, `stats.json`

=> Nghĩa là baseline GraphRAG chạy ổn, và giờ nên đi theo chiến lược **mở rộng workflow** thay vì “viết lại từ đầu”.

---

## Nguyên tắc triển khai để không làm ảnh hưởng baseline (rất quan trọng)

Bạn chốt đúng hướng: **thêm mới (add-only) thay vì overwrite baseline**.

### Vì sao bắt buộc theo hướng add-only ở giai đoạn này

1. Baseline hiện tại đã chạy ổn (`entities`, `relationships`, `community_reports` đã có).
2. MVP cần chứng minh phần đóng góp temporal là một layer mới, tách biệt với baseline.
3. Dễ debug, dễ rollback, dễ so sánh trước/sau trong báo cáo.
4. Tránh làm vỡ query/index flow mặc định của Microsoft GraphRAG.

### Quy tắc thao tác code

- **Ưu tiên tạo file mới** cho workflow/operation/config/prompt temporal.
- **Không sửa sâu** vào logic lõi `extract_graph` ở Sprint 1.
- Chỉ sửa file baseline ở mức “đăng ký workflow/config mới” (small integration points).
- Mọi output temporal ghi ra bảng mới, không ghi đè bảng baseline.

### Danh sách file baseline nên giữ nguyên (trừ khi cực kỳ cần)

- `packages/graphrag/graphrag/index/workflows/extract_graph.py`
- `packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py`
- `packages/graphrag/graphrag/index/workflows/finalize_graph.py`
- `packages/graphrag/graphrag/query/**` (không đụng trong MVP)

### Danh sách file baseline được phép sửa tối thiểu để tích hợp

- `packages/graphrag/graphrag/index/workflows/__init__.py`  
  (đăng ký tên workflow mới)
- `packages/graphrag/graphrag/index/workflows/factory.py`  
  (chèn workflow mới vào pipeline, hoặc dùng `workflows:` override trong settings)
- `packages/graphrag/graphrag/config/models/graph_rag_config.py`  
  (add field config temporal)

---

## Cây file/module nên tạo mới (add-only blueprint)

```text
packages/graphrag/graphrag/
  config/models/
    temporal_extraction_config.py                # NEW

  prompts/index/
    extract_temporal_facts.py                    # NEW (hoặc .txt theo convention bạn chọn)

  index/workflows/
    extract_temporal_facts.py                    # NEW
    resolve_temporal_conflicts.py                # NEW

  index/operations/extract_temporal/
    __init__.py                                  # NEW
    temporal_extractor.py                        # NEW
    temporal_normalizer.py                       # NEW
    conflict_detector.py                         # NEW
    lifecycle_manager.py                         # NEW

  # (Tùy chọn cho cost tracking stage-level)
  callbacks/
    stage_cost_workflow_callback.py              # NEW (optional, theo cost_callback_llm_api.md)
    stage_metrics_registry.py                    # NEW (optional)
```

---

## Thứ tự code từ dễ đến khó (khuyến nghị thực chiến)

### Giai đoạn 0 — Khóa baseline để so sánh

1. Chạy baseline index với data mẫu.
2. Lưu artifacts + log làm mốc.
3. Chốt “không sửa logic extract_graph lõi” trong Sprint 1.

### Giai đoạn 1 — Dựng khung temporal (không gọi LLM trước)

1. Tạo `temporal_extraction_config.py`.
2. Add field vào `GraphRagConfig`.
3. Tạo skeleton 2 workflow mới (chưa xử lý sâu):
   - `extract_temporal_facts.run_workflow`
   - `resolve_temporal_conflicts.run_workflow`
4. Register workflow names ở `workflows/__init__.py`.
5. Chèn workflow vào thứ tự pipeline (hoặc override bằng `workflows:`).

**Mục tiêu pass**: pipeline chạy qua workflow mới mà chưa crash.

### Giai đoạn 2 — Temporal extraction + normalization

1. Code `temporal_extractor.py` với output JSON schema chặt.
2. Code `temporal_normalizer.py`.
3. Ghi `temporal_facts` ra output table mới.

**Mục tiêu pass**: `temporal_facts` không rỗng với file mẫu pháp lý.

### Giai đoạn 3 — Conflict + lifecycle

1. Code `conflict_detector.py`.
2. Code `lifecycle_manager.py`.
3. Workflow `resolve_temporal_conflicts` ghi:
   - `temporal_conflicts`
   - `entity_lifecycle`
   - `temporal_relationships`

**Mục tiêu pass**: có state `ACTIVE/OUTDATED/INVALID` hợp lý.

### Giai đoạn 4 — Quan sát chi phí theo stage (optional trong MVP)

Làm theo tài liệu `cost_callback_llm_api.md`:
- bật model metrics file,
- snapshot delta theo workflow,
- xuất `stage_token_usage.json/csv`.

---

## Mapping theo hướng dẫn Notion (diễn giải ngắn gọn để bám quy trình)

Bạn có thể bám check-flow sau để tránh rối:

1. **Ingest & normalize input**  
   PDF -> text sạch + metadata.
2. **Baseline graph extraction**  
   Dùng flow gốc để lấy entities/relationships.
3. **Temporal augmentation (NEW)**  
   Extract temporal facts + normalize time.
4. **Consistency layer (NEW)**  
   Detect conflict + update lifecycle.
5. **Validation & reporting**  
   So sánh với baseline, đo chất lượng + chi phí.

Nếu làm đúng flow này, bạn luôn chỉ “đắp thêm layer” lên baseline thay vì làm vỡ lõi.

---

## Tính chi phí call OpenAI API (cho pipeline này)

Bạn đang dùng trong `my_workspace_openai/settings.yaml`:
- Completion: `gpt-4.1`
- Embedding: `text-embedding-3-large`

### Công thức tổng quát

Gọi:
- $T_{in,m}$: tổng input tokens của model $m$
- $T_{out,m}$: tổng output tokens của model $m$
- $P_{in,m}$: giá input tokens của model $m$ (USD / 1M tokens)
- $P_{out,m}$: giá output tokens của model $m$ (USD / 1M tokens)
- $T_{emb,e}$: tổng embedding tokens của model embedding $e$
- $P_{emb,e}$: giá embedding tokens (USD / 1M tokens)

Chi phí completion:

$$
Cost_{completion} = \sum_m \left(\frac{T_{in,m}}{10^6} \cdot P_{in,m} + \frac{T_{out,m}}{10^6} \cdot P_{out,m}\right)
$$

Chi phí embedding:

$$
Cost_{embedding} = \sum_e \left(\frac{T_{emb,e}}{10^6} \cdot P_{emb,e}\right)
$$

Tổng:

$$
Cost_{total} = Cost_{completion} + Cost_{embedding}
$$

### Cách đo thực tế trong GraphRAG workflow

1. Chạy index với cache bật (bạn đang bật `cache.type: json`).
2. Lấy token usage từ log/callback hoặc response usage (nên thêm callback tổng hợp usage theo workflow).
3. Tách theo nhóm bước:
  - `extract_graph` (completion lớn nhất)
  - `summarize_descriptions`
  - `create_community_reports`
  - `generate_text_embeddings`
  - các module temporal mới (`extract_temporal_facts`, `resolve_temporal_conflicts`)
4. Áp công thức trên với bảng giá OpenAI tại thời điểm chạy.

> Lưu ý: không hard-code giá vào codebase. Nên để `pricing.yaml` hoặc biến môi trường để cập nhật khi OpenAI đổi giá.

### Cách ước lượng nhanh trước khi chạy thật

Giả sử:
- Có $N$ text units
- Trung bình mỗi text unit là $\bar{t}$ tokens
- Mỗi unit gọi extraction $g$ lần (phụ thuộc `max_gleanings`)

Xấp xỉ:

$$
T_{in,extract} \approx N \cdot g \cdot (t_{prompt} + \bar{t})
$$

$$
T_{out,extract} \approx N \cdot g \cdot t_{resp}
$$

Embedding xấp xỉ:

$$
T_{emb} \approx \sum_{records} tokens(record)
$$

Dùng công thức này để dự trù ngân sách trước khi index full dữ liệu.

### Template đã tạo sẵn để bạn điền ngay

Mình đã tạo file: `pricing.yaml` ở root repo:
- `Temporal-Conflict-Aware-GraphRAG/pricing.yaml`

Bạn chỉ cần điền:
- `input_price_per_1m_tokens`
- `output_price_per_1m_tokens`
- `average_tokens_per_pdf_page` phù hợp dữ liệu của bạn

### Bảng ước lượng cost theo số trang PDF (template điền nhanh)

Giả sử dùng profile `normal_text` trong `pricing.yaml`:
- $avg\_tokens\_per\_page = A$
- $pages = P$
- $raw\_tokens = P \cdot A$

Các hệ số stage lấy từ `pricing.yaml`:
- $M_{in}$: tổng input multipliers của completion stages
- $M_{out}$: tổng output multipliers của completion stages
- $M_{emb}$: embedding input multiplier

Khi đó:

$$
T_{in} = raw\_tokens \cdot M_{in}, \quad
T_{out} = raw\_tokens \cdot M_{out}, \quad
T_{emb} = raw\_tokens \cdot M_{emb}
$$

| Pages ($P$) | Raw tokens ($P\cdot A$) | Completion in tokens ($T_{in}$) | Completion out tokens ($T_{out}$) | Embedding tokens ($T_{emb}$) | Total cost (USD) |
|---:|---:|---:|---:|---:|---:|
| 5 | $5A$ | $5A\cdot M_{in}$ | $5A\cdot M_{out}$ | $5A\cdot M_{emb}$ | Điền theo công thức |
| 10 | $10A$ | $10A\cdot M_{in}$ | $10A\cdot M_{out}$ | $10A\cdot M_{emb}$ | Điền theo công thức |
| 25 | $25A$ | $25A\cdot M_{in}$ | $25A\cdot M_{out}$ | $25A\cdot M_{emb}$ | Điền theo công thức |
| 50 | $50A$ | $50A\cdot M_{in}$ | $50A\cdot M_{out}$ | $50A\cdot M_{emb}$ | Điền theo công thức |
| 100 | $100A$ | $100A\cdot M_{in}$ | $100A\cdot M_{out}$ | $100A\cdot M_{emb}$ | Điền theo công thức |

> Mẹo thực tế: chạy thử với 5-10 trang đầu, đo usage thật, update lại multiplier trong `pricing.yaml`, rồi mới forecast cho toàn bộ tài liệu.

---

## Nên dùng những file nào từ các summary trước

Đọc theo thứ tự này trước khi code:

1. `summary_focus_packages.md`
   - Bản đồ kiến trúc lõi package `graphrag`.
2. `summary_callgraph_focus.md`
   - Call graph function-level cho index/query.
3. `summary_trace_entity_query.md`
   - Runtime trace thực tế từ CLI tới streaming output.
4. `summary.md`
   - Toàn cảnh repo để tránh sửa sai vùng.

Các file code gốc cần bám sát:
- `packages/graphrag/graphrag/index/workflows/factory.py`
- `packages/graphrag/graphrag/index/workflows/__init__.py`
- `packages/graphrag/graphrag/index/workflows/extract_graph.py`
- `packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py`
- `packages/graphrag/graphrag/config/models/graph_rag_config.py`
- `packages/graphrag/graphrag/config/models/extract_graph_config.py`

### Nên đọc kỹ thêm file `.md` nào để “hình dung task” rõ ràng

Đây là lộ trình đọc theo thứ tự tư duy (đi từ bài toán -> luồng chạy -> điểm can thiệp code):

1. `task_extraction.md` (file này)  
  - **Mục đích**: hiểu mục tiêu task của bạn, output cần có, roadmap triển khai.
2. `summary_focus_packages.md`  
  - **Mục đích**: hiểu kiến trúc package `graphrag`, pipeline index/query gồm những khối nào.
3. `summary_callgraph_focus.md`  
  - **Mục đích**: hiểu hàm gọi hàm ra sao để biết nên hook ở đâu.
4. `summary_trace_entity_query.md`  
  - **Mục đích**: thấy runtime trace thật để liên hệ từ lý thuyết sang log thực tế.
5. `summary.md`  
  - **Mục đích**: toàn cảnh repo, tránh sửa nhầm khu vực ngoài phạm vi task.

### Đi từ đâu, tại sao đi như vậy

- **Bắt đầu từ workflow index** vì task của bạn là extraction pipeline (không phải query-first).
- **Ưu tiên Pha 1 (MVP temporal artifacts)** để có kết quả đo được (`temporal_facts`, `conflicts`, `lifecycle`) trước.
- **Chưa đụng query ngay** để giảm biến số và tránh debug chồng tầng.

### Kiến thức workflow cần có để build đúng

1. **Workflow orchestration**: mỗi bước đọc table nào, ghi table nào.
2. **Operation contract**: input/output schema rõ ràng, idempotent, fail-safe.
3. **Prompt-structured extraction**: bắt buộc JSON schema để parse ổn định.
4. **Temporal normalization**: đổi time text -> interval để so sánh được.
5. **Conflict reasoning**: phát hiện mâu thuẫn và cập nhật lifecycle.

### Giai đoạn/hàm giải quyết bài toán gì

- `extract_temporal_facts`: giải bài toán “lôi thời gian ra khỏi relation hiện có”.
- `temporal_normalizer`: giải bài toán “đưa thời gian về format so sánh được”.
- `conflict_detector`: giải bài toán “fact nào mâu thuẫn fact nào”.
- `lifecycle_manager`: giải bài toán “trạng thái tri thức hiện tại là gì”.
- `resolve_temporal_conflicts` (workflow): nối 3 bài toán trên thành luồng hoàn chỉnh.

---

## Task của bạn được diễn giải rõ (để dễ giải thích với team)

Bạn đang làm **Temporal Document Extraction trên GraphRAG**, tức là:

1. Giữ nguyên backbone GraphRAG để extract entity/relationship như hiện tại.
2. Bổ sung temporal layer để biết **quan hệ đúng ở thời điểm nào**.
3. Khi có facts mâu thuẫn, phân loại conflict và gán lifecycle (`ACTIVE/OUTDATED/INVALID`).
4. Kết quả cuối không chỉ là graph tĩnh, mà là graph có tính thời gian và nhất quán hơn để query.

Output kỳ vọng tối thiểu cho task đầu:
- index chạy xong không lỗi,
- có `temporal_facts`, `temporal_conflicts`, `entity_lifecycle`,
- có thể chứng minh bằng file mẫu `172-qd-dhcntt...pdf` rằng pipeline temporal đang hoạt động.

---

## Chiến lược triển khai: 2 pha để giảm rủi ro

### Pha 1 (MVP, bắt buộc)

Mục tiêu: tạo temporal artifacts từ kết quả `extract_graph` hiện tại.

- Không thay đổi query engine ngay.
- Chèn workflow temporal sau `extract_graph` và trước/tại `finalize_graph`.
- Sinh thêm các bảng:
  - `temporal_facts`
  - `temporal_relationships`
  - `temporal_conflicts`
  - `entity_lifecycle`

Lợi ích:
- Dễ test.
- Không làm vỡ pipeline mặc định.
- Có dữ liệu temporal để debug và đánh giá chất lượng extraction.

### Pha 2 (Nâng cao)

Mục tiêu: temporal-aware retrieval và update.

- Mở rộng query context builder để ưu tiên fact hợp lệ theo thời điểm hỏi.
- Kết hợp incremental update: khi dữ liệu mới tới, cập nhật lifecycle/conflict thay vì overwrite phẳng.

---

## Đề xuất tổ chức file custom (cụ thể)

Tạo các module mới trong repo fork này:

- `packages/graphrag/graphrag/index/workflows/extract_temporal_facts.py`
  - Workflow orchestration cho temporal extraction.
- `packages/graphrag/graphrag/index/workflows/resolve_temporal_conflicts.py`
  - Workflow chuẩn hóa thời gian + phát hiện conflict + cập nhật lifecycle.

- `packages/graphrag/graphrag/index/operations/extract_temporal/temporal_extractor.py`
  - LLM/NLP extraction từ text units + relationships hiện có.
- `packages/graphrag/graphrag/index/operations/extract_temporal/temporal_normalizer.py`
  - Chuẩn hóa time expression về ISO/date-range.
- `packages/graphrag/graphrag/index/operations/extract_temporal/conflict_detector.py`
  - Phân loại conflict (hard/soft/source ambiguity).
- `packages/graphrag/graphrag/index/operations/extract_temporal/lifecycle_manager.py`
  - Cập nhật trạng thái ACTIVE/OUTDATED/INVALID.

- `packages/graphrag/graphrag/config/models/temporal_extraction_config.py`
  - Config block riêng cho temporal extraction.

- `packages/graphrag/graphrag/prompts/index/extract_temporal_facts.py`
  - Prompt mặc định cho temporal relation extraction.

- `packages/graphrag/graphrag/query/structured_search/local_search/temporal_mixed_context.py` (Pha 2)
  - Context builder temporal-aware.

---

## Cách code cụ thể cho từng module mới (logic thuật toán)

Phần này mô tả “viết như thế nào” thay vì chỉ nêu tên module.

### 1) `extract_temporal_facts.py` (workflow)

**Luồng xử lý chuẩn**:
1. Đọc `text_units`, `relationships` từ `DataReader`.
2. Join nhẹ để lấy evidence text theo `text_unit_ids`.
3. Gọi `temporal_extractor.extract_temporal_facts(...)` (LLM extraction).
4. Gọi `temporal_normalizer.normalize_temporal_facts(...)`.
5. Lọc theo `min_confidence`.
6. Ghi `temporal_facts`.

**Thuật toán chính**:
- Chunk-level candidate generation -> LLM structured extraction -> normalization -> confidence filter.

### 2) `temporal_extractor.py` (operation)

**Input**: `(text_unit_text, source, target, relation_description)`

**Prompt output bắt buộc JSON schema** (một hoặc nhiều facts):
- subject, predicate, object
- time_text, start_time, end_time, granularity
- confidence, rationale ngắn

**Thuật toán**:
1. Build candidate pairs từ `relationships`.
2. Với mỗi pair, lấy top evidence text units.
3. Gọi LLM theo batch async (`derive_from_rows` pattern giống `extract_graph`).
4. Parse JSON cứng (fail-safe: record lỗi + skip).
5. Chuẩn hóa field names và trả DataFrame.

### 3) `temporal_normalizer.py` (operation)

**Thuật toán normalize**:
1. Nếu có `start_time/end_time` chuẩn -> parse trực tiếp.
2. Nếu chỉ có `time_text`:
  - regex rule cho `dd/mm/yyyy`, `mm/yyyy`, `yyyy`, `Qx yyyy`.
  - map về interval `[valid_from, valid_to]` theo granularity.
3. Nếu mơ hồ (“đầu năm ngoái”):
  - dùng `reference_time` để quy chiếu,
  - gắn `time_parse_quality` thấp hơn.
4. Trả facts với `valid_from`, `valid_to`, `time_parse_quality`.

### 4) `conflict_detector.py` (operation)

**Thuật toán phát hiện conflict**:
1. Group theo key `(subject, predicate, object)` hoặc `(subject, predicate)` tùy nghiệp vụ.
2. So interval overlap:
  - overlap lớn + giá trị đối nghịch -> `hard`.
  - overlap nhỏ / thiếu bằng chứng -> `soft`.
  - khác nguồn, confidence gần nhau -> `source_ambiguity`.
3. Xuất `temporal_conflicts` kèm `facts_involved`.

### 5) `lifecycle_manager.py` (operation)

**Thuật toán lifecycle**:
1. Sắp xếp facts theo thời gian + confidence.
2. Chọn fact “effective” hiện tại cho mỗi thực thể/quan hệ.
3. Gán state:
  - `ACTIVE`: đang còn hiệu lực.
  - `OUTDATED`: từng đúng nhưng đã hết hiệu lực.
  - `INVALID`: bị phủ định bởi evidence mạnh hơn hoặc hard conflict đã resolve.
4. Xuất `entity_lifecycle` + `temporal_relationships`.

### 6) `resolve_temporal_conflicts.py` (workflow)

**Luồng xử lý**:
1. Đọc `temporal_facts`.
2. Gọi `detect_temporal_conflicts`.
3. Gọi `update_lifecycle`.
4. Ghi `temporal_conflicts`, `entity_lifecycle`, `temporal_relationships`.

---

## Xử lý file mẫu PDF `172-qd-dhcntt...pdf` để chạy CLI đúng quy trình

Với config hiện tại `input.type: text`, GraphRAG kỳ vọng text file. Vì vậy PDF nên đi qua bước tiền xử lý.

### Đặt file ở đâu

Trong workspace `my_workspace_openai`:
- Đặt PDF gốc tại: `input/raw/172-qd-dhcntt_08-3-2023_quy_che_van_bang_chung_chi.pdf`
- Sinh file text chuẩn để index tại: `input/172-qd-dhcntt_08-3-2023_quy_che_van_bang_chung_chi.txt`

### Vì sao không index PDF trực tiếp ở task đầu

- `input.type: text` tối ưu cho pipeline hiện tại.
- Tránh sai lệch parser khi PDF có layout phức tạp.
- Dễ debug temporal extraction vì text đã “phẳng hóa”.

### Chuẩn hóa text trước khi index

Checklist tiền xử lý:
1. Tách text từ PDF (UTF-8).
2. Chuẩn hóa khoảng trắng, xuống dòng, bỏ header/footer lặp.
3. Giữ cấu trúc mục/điều/khoản nếu có (rất quan trọng cho legal docs).
4. (Khuyến nghị) prepend metadata đầu file:
  - `document_id`
  - `source_file`
  - `issued_date`
  - `document_type`

### Quy trình chạy cho task đầu (single-document)

1. Đặt PDF vào `input/raw/`.
2. Convert + clean -> tạo `.txt` trong `input/`.
3. Đảm bảo `settings.yaml` có `input.type: text` và `input_storage.base_dir: input`.
4. Chạy indexing bằng CLI như hiện tại.
5. Kiểm tra output chuẩn (`entities`, `relationships`, `community_reports`) trước.
6. Sau khi thêm temporal workflow, kiểm tra thêm:
  - `temporal_facts`
  - `temporal_conflicts`
  - `entity_lifecycle`

### Tiêu chí pass cho file mẫu 172-qd-dhcntt

- Index chạy thành công, không crash ở `extract_graph`.
- Có temporal facts hợp lệ (không rỗng) cho các điều khoản chứa thời điểm hiệu lực.
- Conflict detector không tạo lỗi parse thời gian.
- Lifecycle tạo được state cho các thực thể/chủ thể chính trong văn bản.

---

## Cách cắm vào pipeline hiện tại

### 1) Register workflow name

Trong `index/workflows/__init__.py`, thêm đăng ký:
- `extract_temporal_facts`
- `resolve_temporal_conflicts`

### 2) Chèn workflow vào pipeline

Trong `index/workflows/factory.py`, tạo pipeline temporal (hoặc override qua `settings.yaml`):

Gợi ý thứ tự an toàn:
1. `load_input_documents`
2. `create_base_text_units`
3. `create_final_documents`
4. `extract_graph`
5. `extract_temporal_facts`
6. `resolve_temporal_conflicts`
7. `finalize_graph`
8. `extract_covariates`
9. `create_communities`
10. `create_final_text_units`
11. `create_community_reports`
12. `generate_text_embeddings`

> Nếu muốn ít đụng code core: dùng `workflows:` trong `settings.yaml` để override danh sách thay vì sửa built-in `IndexingMethod`.

---

## Contract chi tiết cho từng hàm custom

Dưới đây là contract đề xuất (typing + docstring scope) để đội dev code đồng nhất.

### A. Workflow: `extract_temporal_facts.run_workflow`

**File**: `index/workflows/extract_temporal_facts.py`

**Signature đề xuất**
- `async def run_workflow(config: GraphRagConfig, context: PipelineRunContext) -> WorkflowFunctionOutput`

**Input**
- `text_units: pd.DataFrame` (đọc từ `DataReader`)
- `entities: pd.DataFrame`
- `relationships: pd.DataFrame`
- prompt + model config từ `config.temporal_extraction`

**Output tables**
- `temporal_facts`
- `temporal_relationships` (nếu tách riêng)

**Docstring mục tiêu**
- Trích xuất temporal quadruples từ text và graph sơ cấp.
- Mỗi fact gồm `(subject, relation, object, valid_time, source)`.

**Bài toán giải quyết**
- Biến relation “không thời gian” thành relation có ngữ cảnh thời gian.

---

### B. Operation: `temporal_extractor.extract_temporal_facts`

**File**: `index/operations/extract_temporal/temporal_extractor.py`

**Signature đề xuất**
- `async def extract_temporal_facts(text_units: pd.DataFrame, relationships: pd.DataFrame, model: LLMCompletion, prompt: str, num_threads: int, async_type: AsyncType) -> pd.DataFrame`

**Input type**
- `text_units`: chứa `id`, `text`
- `relationships`: chứa `source`, `target`, `description`, `text_unit_ids`

**Output type**
- `pd.DataFrame` cột gợi ý:
  - `fact_id: str`
  - `subject: str`
  - `predicate: str`
  - `object: str`
  - `time_text: str`
  - `start_time: str | None`
  - `end_time: str | None`
  - `time_granularity: Literal['year','month','day','interval','unknown']`
  - `confidence: float`
  - `source_doc_id: str | None`
  - `source_text_unit_id: str`

**Docstring mục tiêu**
- Trích temporal facts từ evidence text theo từng text unit/relationship pair.

**Bài toán giải quyết**
- Lấy “thời điểm hiệu lực” cho các quan hệ thực thể.

---

### C. Operation: `temporal_normalizer.normalize_temporal_facts`

**File**: `index/operations/extract_temporal/temporal_normalizer.py`

**Signature đề xuất**
- `def normalize_temporal_facts(facts_df: pd.DataFrame, reference_time: str | None = None) -> pd.DataFrame`

**Input**
- facts có `time_text`, có thể mơ hồ (“đầu năm ngoái”, “Q2 2023”)

**Output**
- facts đã normalize về ISO-like interval:
  - `valid_from: datetime | None`
  - `valid_to: datetime | None`
  - `time_parse_quality: float`

**Docstring mục tiêu**
- Chuẩn hóa temporal expressions để phục vụ so sánh và conflict detection.

**Bài toán giải quyết**
- Đồng nhất định dạng thời gian cho toàn pipeline.

---

### D. Workflow/Operation: `resolve_temporal_conflicts`

**File workflow**: `index/workflows/resolve_temporal_conflicts.py`  
**File operations**:
- `conflict_detector.py`
- `lifecycle_manager.py`

#### D1. `conflict_detector.detect_temporal_conflicts`

**Signature đề xuất**
- `def detect_temporal_conflicts(facts_df: pd.DataFrame) -> pd.DataFrame`

**Input**
- facts đã normalize.

**Output**
- `temporal_conflicts` với cột gợi ý:
  - `conflict_id: str`
  - `entity_pair_key: str`
  - `conflict_type: Literal['hard','soft','source_ambiguity']`
  - `facts_involved: list[str]`
  - `resolution_hint: str`

**Docstring mục tiêu**
- Phát hiện conflict theo chồng lấn interval + mâu thuẫn ngữ nghĩa quan hệ.

#### D2. `lifecycle_manager.update_lifecycle`

**Signature đề xuất**
- `def update_lifecycle(facts_df: pd.DataFrame, conflicts_df: pd.DataFrame, now: datetime | None = None) -> tuple[pd.DataFrame, pd.DataFrame]`

**Input**
- facts + conflicts.

**Output**
- `entity_lifecycle`:
  - `entity_id`
  - `state: Literal['ACTIVE','OUTDATED','INVALID']`
  - `valid_from`
  - `valid_to`
  - `last_updated`
- `temporal_relationships` đã gắn trạng thái/lifecycle.

**Docstring mục tiêu**
- Cập nhật trạng thái vòng đời tri thức theo temporal consistency.

---

### E. Config model: `TemporalExtractionConfig`

**File**: `config/models/temporal_extraction_config.py`

**Signature đề xuất**
- `class TemporalExtractionConfig(BaseModel): ...`

**Fields tối thiểu**
- `enabled: bool = False`
- `completion_model_id: str`
- `model_instance_name: str = 'temporal_extraction'`
- `prompt: str | None`
- `max_gleanings: int = 1`
- `conflict_overlap_threshold_days: int = 0`
- `min_confidence: float = 0.5`
- `default_reference_timezone: str = 'UTC'`

**Tích hợp vào config tổng**
- Add field trong `GraphRagConfig`:
  - `temporal_extraction: TemporalExtractionConfig = Field(default=TemporalExtractionConfig())`

---

## Luồng gọi liên file (Document_Extraction end-to-end)

Dưới đây là call flow mục tiêu sau khi thêm temporal workflows:

1. CLI/API index gọi pipeline runner như cũ.
2. `extract_graph.run_workflow` sinh `entities`, `relationships`.
3. `extract_temporal_facts.run_workflow`:
   - đọc `text_units`, `relationships`
   - gọi `temporal_extractor.extract_temporal_facts`
   - gọi `temporal_normalizer.normalize_temporal_facts`
   - ghi `temporal_facts`
4. `resolve_temporal_conflicts.run_workflow`:
   - đọc `temporal_facts`
   - gọi `conflict_detector.detect_temporal_conflicts`
   - gọi `lifecycle_manager.update_lifecycle`
   - ghi `temporal_conflicts`, `entity_lifecycle`, `temporal_relationships`
5. Các workflow sau (`create_communities`, `create_community_reports`, `generate_text_embeddings`) tiếp tục chạy, có thể mở rộng để đọc temporal tables ở Pha 2.

---

## Mapping trực tiếp với 10 bước Document_Extraction

1. Metadata handling  
   -> dùng `load_input_documents` + enrich metadata sớm tại `create_base_text_units`.

2. Coreference resolution  
   -> tạm MVP: dựa entity merge/groupby; nâng cao: thêm pre-op coref trước `extract_graph`.

3. Chunking  
   -> `create_base_text_units` (đã có).

4. NER  
   -> `extract_graph` (LLM graph extraction hiện tại).

5. Relation candidate generation  
   -> đầu ra `relationships` từ `extract_graph`.

6. LLM relation reasoning  
   -> đang nằm trong extractor + summarize relation descriptions.

7. Temporal extraction  
   -> workflow mới `extract_temporal_facts`.

8. Normalization  
   -> `temporal_normalizer.normalize_temporal_facts`.

9. Temporal conflict detection  
   -> `resolve_temporal_conflicts` + `conflict_detector`.

10. Temporal KG assembly  
   -> `temporal_relationships` + `entity_lifecycle` + optional integration vào query.

---

## Đề xuất schema bảng temporal (MVP)

### `temporal_facts`
- `fact_id: str`
- `subject: str`
- `predicate: str`
- `object: str`
- `valid_from: datetime | None`
- `valid_to: datetime | None`
- `confidence: float`
- `source_text_unit_id: str`
- `source_doc_id: str | None`

### `temporal_conflicts`
- `conflict_id: str`
- `entity_pair_key: str`
- `conflict_type: str`
- `facts_involved: list[str]`
- `resolution_hint: str`

### `entity_lifecycle`
- `entity_id: str`
- `state: str` (`ACTIVE|OUTDATED|INVALID`)
- `valid_from: datetime | None`
- `valid_to: datetime | None`
- `last_updated: datetime`

---

## Kế hoạch triển khai theo sprint

### Sprint 1 (2-3 ngày)
- Tạo config `TemporalExtractionConfig`.
- Tạo workflow `extract_temporal_facts`.
- Tạo operations `temporal_extractor` + `temporal_normalizer`.
- Ghi bảng `temporal_facts`.
- Test smoke: pipeline chạy end-to-end không vỡ.

### Sprint 2 (2-3 ngày)
- Tạo `resolve_temporal_conflicts` + `conflict_detector` + `lifecycle_manager`.
- Ghi `temporal_conflicts`, `entity_lifecycle`, `temporal_relationships`.
- Viết unit test cho overlap/conflict cases.

### Sprint 3 (3-5 ngày)
- Temporal-aware query context (local mode trước).
- Thêm scoring ưu tiên fact hợp lệ theo thời điểm hỏi:
  - $score = \alpha \cdot relevance + \beta \cdot temporal\_validity - \gamma \cdot conflict\_penalty$
- Đánh giá chất lượng trên tập câu hỏi có mốc thời gian.

---

## Checklist test bắt buộc

1. **Schema test**: mọi bảng temporal có đúng cột và kiểu.
2. **Determinism test**: cùng input -> cùng normalization output (trong ngưỡng chấp nhận).
3. **Conflict test**:
   - interval chồng lấn + relation đối nghịch -> `hard`.
   - khác nguồn nhưng không đối nghịch mạnh -> `source_ambiguity`.
4. **Lifecycle test**:
   - fact mới phủ định fact cũ -> cũ chuyển `OUTDATED` hoặc `INVALID`.
5. **Pipeline compatibility**:
   - bật/tắt `temporal_extraction.enabled` đều index được.

---

## Rủi ro và cách giảm rủi ro

- **Rủi ro 1: Prompt temporal extraction không ổn định**
  - Giảm thiểu: bắt buộc JSON schema output + post-parse validator.

- **Rủi ro 2: Time normalization sai với biểu thức mơ hồ**
  - Giảm thiểu: giữ `time_text` gốc + `time_parse_quality` để fallback.

- **Rủi ro 3: Conflict false positive**
  - Giảm thiểu: phân tầng `hard/soft/source_ambiguity` thay vì nhị phân.

- **Rủi ro 4: làm chậm index**
  - Giảm thiểu: chỉ bật temporal cho tập dữ liệu cần, và tối ưu `concurrent_requests`.

---

## Liên hệ với paper/docs (định hướng học thuật)

- **GraphRAG**: giữ backbone community + report + mixed retrieval.
- **TG-RAG**: học cách biểu diễn temporal quadruples + incremental temporal update.
- **T-GRAG**: nhấn mạnh temporal conflict-aware retrieval và conflict-driven graph maintenance.

Kết luận: bạn nên giữ GraphRAG làm khung chính, thêm temporal layer theo dạng modular workflow để vừa đúng đề tài vừa dễ bảo trì.

---

## Việc nên làm ngay sau tài liệu này

1. Tạo branch mới: `feature/temporal-extraction-mvp`.
2. Implement Sprint 1 trước, không đụng query.
3. Chạy index trên tập nhỏ đã biết ground truth thời gian.
4. So sánh output temporal tables bằng script đánh giá đơn giản.
5. Khi Sprint 1 ổn mới qua conflict/lifecycle và query.

---

## Kết luận ngắn

Bạn không cần “đập đi làm lại” GraphRAG. Đường đi đúng là:
- mở rộng có kiểm soát tại `workflows` + `operations` + `config`,
- thêm temporal artifacts độc lập,
- rồi mới nâng query thành temporal-aware.

Đi theo lộ trình này sẽ cân bằng được 3 mục tiêu: **đúng đề tài**, **ít rủi ro kỹ thuật**, **ra kết quả sớm để demo/đánh giá**.
