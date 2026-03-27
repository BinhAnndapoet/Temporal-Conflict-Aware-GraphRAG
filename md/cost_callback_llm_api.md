# cost_callback_llm_api.md

## Mục tiêu tài liệu

Tài liệu này mô tả **thiết kế triển khai Cách B** (stage-level cost tracking) cho GraphRAG repo hiện tại, theo hướng:
- đo được token/cost **chi tiết theo từng workflow stage**,
- vẫn giữ tương thích với metrics mặc định của `graphrag-llm`,
- có output file để đọc máy (`json/csv`) và dễ visualize thành dashboard.

> Đây là tài liệu thiết kế + pseudo-code để bạn hình dung và phân tích. Chưa phải commit code thật.

---

## Vấn đề thực tế hiện tại

Bạn đang xem usage trên OpenAI platform thì thường thấy theo request/model tổng quát.  
Nhưng với GraphRAG, bạn cần biết cụ thể:
- stage nào tốn nhất (`extract_graph`, `community_reports`, `generate_text_embeddings`, `extract_temporal_facts`, ...),
- completion vs embedding stage nào chiếm cost,
- sau khi tối ưu prompt/chunking có giảm stage-cost không.

Mặc định GraphRAG/LLM có metrics store theo model, nhưng chưa tự xuất breakdown chuẩn theo workflow stage.

---

## Kiến trúc đo cost theo stage (đề xuất)

## 1) Hai lớp metrics

1. **Model-level metrics (đã có sẵn)**
   - Từ `graphrag_llm` metrics store (`prompt_tokens`, `completion_tokens`, `total_cost`, ...).
2. **Stage-level ledger (mình thêm)**
   - Snapshot metrics đầu/cuối mỗi workflow.
   - Lấy **delta** để ra token/cost của từng stage.

Công thức delta cho stage $s$:

$$
\Delta_s(metric) = metric_{after\_stage} - metric_{before\_stage}
$$

Ví dụ:
- $\Delta_s(prompt\_tokens)$
- $\Delta_s(completion\_tokens)$
- $\Delta_s(total\_cost)$

---

## 2) Điểm chèn trong repo (file-level)

### A. Callback chain & pipeline lifecycle

- `packages/graphrag/graphrag/api/index.py`
  - `build_index(...)` đang nhận `callbacks` list.
- `packages/graphrag/graphrag/index/run/run_pipeline.py`
  - gọi `context.callbacks.workflow_start(...)` / `workflow_end(...)`.

=> Đây là nơi hook callback stage-level tự nhiên nhất.

### B. Nơi tạo model LLM/Embedding

Các workflow tạo model cục bộ bằng:
- `create_completion(...)`
- `create_embedding(...)`

Ví dụ điển hình:
- `index/workflows/extract_graph.py`
- `index/workflows/create_community_reports.py`
- `index/workflows/generate_text_embeddings.py`
- (sau này) `extract_temporal_facts.py`

=> Muốn stage-level chính xác thì cần đăng ký model/metrics_store vào registry theo stage.

---

## Quy trình triển khai (step-by-step)

## Bước 1 — Bật model metrics writer dạng file

Trong `settings.yaml`, cho model completion/embedding thêm block `metrics`:

```yaml
completion_models:
  default_completion_model:
    model_provider: openai
    model: gpt-4.1
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    metrics:
      type: default
      store: memory
      writer: file
      base_dir: logs/metrics

embedding_models:
  default_embedding_model:
    model_provider: openai
    model: text-embedding-3-large
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    metrics:
      type: default
      store: memory
      writer: file
      base_dir: logs/metrics
```

Kết quả:
- Có JSONL model-level metrics khi process kết thúc.
- Đây là nền để stage-ledger lấy snapshot delta.

---

## Bước 2 — Tạo stage metrics registry (module mới)

**File đề xuất**:  
`packages/graphrag/graphrag/callbacks/stage_metrics_registry.py`

### Vai trò
- Lưu map `workflow_name -> list[metrics_store_handle]`.
- Cho phép workflow đăng ký metrics store của model đang dùng.
- Cung cấp API `snapshot(workflow_name)` trả metrics tổng hợp hiện tại.

### Pseudo-code

```python
class StageMetricsRegistry:
    def register_store(self, workflow_name: str, store_id: str, store: MetricsStore):
        ...

    def snapshot(self, workflow_name: str) -> dict:
        # gộp metrics từ các stores của workflow
        # keys: prompt_tokens, completion_tokens, total_tokens, input_cost, output_cost, total_cost
        ...
```

---

## Bước 3 — Tạo callback stage cost

**File đề xuất**:  
`packages/graphrag/graphrag/callbacks/stage_cost_workflow_callback.py`

### Vai trò
- `workflow_start(name, ...)`: lấy snapshot before.
- `workflow_end(name, ...)`: snapshot after, tính delta, append vào ledger.
- `pipeline_end(...)`: ghi file
  - `logs/stage_token_usage.json`
  - `logs/stage_token_usage.csv`

### Pseudo-code

```python
class StageCostWorkflowCallback(NoopWorkflowCallbacks):
    def __init__(self, registry, output_dir: str = "logs"):
        self.registry = registry
        self.before = {}
        self.rows = []

    def workflow_start(self, name, instance):
        self.before[name] = self.registry.snapshot(name)

    def workflow_end(self, name, instance):
        after = self.registry.snapshot(name)
        before = self.before.get(name, {})
        row = compute_delta_row(name=name, before=before, after=after)
        self.rows.append(row)

    def pipeline_end(self, results):
        write_json(self.rows, "logs/stage_token_usage.json")
        write_csv(self.rows, "logs/stage_token_usage.csv")
```

---

## Bước 4 — Đăng ký stores trong từng workflow

Ý tưởng: ở nơi tạo model, lấy `model.metrics_store` rồi register vào workflow hiện tại.

### Ví dụ trong `extract_graph.run_workflow`

Pseudo-code (ý tưởng):

```python
workflow_name = "extract_graph"

extraction_model = create_completion(...)
registry.register_store(workflow_name, "extract_graph.extraction", extraction_model.metrics_store)

summarization_model = create_completion(...)
registry.register_store(workflow_name, "extract_graph.summarization", summarization_model.metrics_store)
```

### Ví dụ trong `generate_text_embeddings.run_workflow`

```python
workflow_name = "generate_text_embeddings"
embedding_model = create_embedding(...)
registry.register_store(workflow_name, "generate_text_embeddings.embedding", embedding_model.metrics_store)
```

### Với workflow temporal mới

Trong `extract_temporal_facts.run_workflow`:

```python
registry.register_store("extract_temporal_facts", "temporal_extractor", temporal_model.metrics_store)
```

---

## Bước 5 — Gắn callback vào CLI index

**Điểm chèn**: `packages/graphrag/graphrag/cli/index.py` trong `_run_index(...)`.

Hiện tại đang gọi:

```python
callbacks=[ConsoleWorkflowCallbacks(verbose=verbose)]
```

Đề xuất thêm callback stage-cost:

```python
callbacks=[
    ConsoleWorkflowCallbacks(verbose=verbose),
    StageCostWorkflowCallback(registry=registry, output_dir=str(config.reporting.base_dir)),
]
```

---

## Bước 6 — Ghép `pricing.yaml` để ra cost tự động đẹp

Bạn đã có `pricing.yaml`. Có 2 cách:

1. **Dùng cost đã có trong metrics** (`input_cost`, `output_cost`, `total_cost`) nếu provider trả về chuẩn.
2. **Fallback tự tính** từ tokens + giá trong `pricing.yaml`:

$$
Cost_{stage} = \frac{prompt\_tokens}{10^6} \cdot P_{in} + \frac{completion\_tokens}{10^6} \cdot P_{out}
$$

Với embedding stage:

$$
Cost_{emb\_stage} = \frac{embedding\_tokens}{10^6} \cdot P_{emb}
$$

---

## Định dạng output đề xuất

## 1) `stage_token_usage.json`

```json
[
  {
    "stage": "extract_graph",
    "prompt_tokens": 12345,
    "completion_tokens": 4567,
    "total_tokens": 16912,
    "input_cost": 0.12,
    "output_cost": 0.20,
    "total_cost": 0.32,
    "llm_calls": 89,
    "duration_seconds": 75.4
  },
  {
    "stage": "generate_text_embeddings",
    "prompt_tokens": 9876,
    "completion_tokens": 0,
    "total_tokens": 9876,
    "input_cost": 0.05,
    "output_cost": 0.0,
    "total_cost": 0.05,
    "llm_calls": 40,
    "duration_seconds": 21.3
  }
]
```

## 2) `stage_token_usage.csv`

Columns:
- `stage`
- `prompt_tokens`
- `completion_tokens`
- `total_tokens`
- `input_cost`
- `output_cost`
- `total_cost`
- `llm_calls`
- `duration_seconds`

---

## Source code mẫu dashboard (để visualize)

Bạn có thể làm dashboard mini bằng Streamlit đọc `stage_token_usage.json`.

```python
# file: scripts/stage_cost_dashboard.py
import json
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="GraphRAG Stage Cost", layout="wide")
st.title("GraphRAG Stage-Level Token & Cost Dashboard")

path = st.text_input("Path JSON", "logs/stage_token_usage.json")

with open(path, "r", encoding="utf-8") as f:
    rows = json.load(f)

df = pd.DataFrame(rows)

st.subheader("Stage table")
st.dataframe(df, use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    fig_cost = px.bar(df, x="stage", y="total_cost", title="Cost per stage")
    st.plotly_chart(fig_cost, use_container_width=True)
with c2:
    fig_tokens = px.bar(df, x="stage", y="total_tokens", title="Tokens per stage")
    st.plotly_chart(fig_tokens, use_container_width=True)

fig_scatter = px.scatter(
    df,
    x="duration_seconds",
    y="total_cost",
    size="total_tokens",
    color="stage",
    title="Duration vs Cost (bubble=size tokens)",
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.metric("Total cost", f"${df['total_cost'].sum():.4f}")
st.metric("Total tokens", int(df["total_tokens"].sum()))
```

---

## Test plan để xác nhận đo đúng

1. **Smoke test**
   - Chạy index dataset nhỏ.
   - Có sinh `stage_token_usage.json/csv`.

2. **Consistency test**
   - Tổng `stage total_tokens` xấp xỉ tổng model metrics file.
   - Tổng `stage total_cost` xấp xỉ cost tổng của run.

3. **Cache test**
   - Run lần 2 với cache warm.
   - Tokens/cost giảm rõ ở các stage completion-heavy.

4. **Temporal workflow test**
   - Bật workflow temporal.
   - Có row riêng cho `extract_temporal_facts`/`resolve_temporal_conflicts`.

---

## Rủi ro & lưu ý khi triển khai thật

1. **Metrics store scope là singleton theo init args**  
   => Cần snapshot delta chính xác theo thời điểm start/end stage.

2. **Một stage có nhiều model calls**  
   => Phải register đủ stores cho stage (extraction + summarization + embedding nếu có).

3. **Cache có thể làm token/cost về rất thấp**  
   => Báo cáo nên có thêm `cached_responses` hoặc cờ cache-hit.

4. **Streaming response**
   => Với một số mode query, usage/cost có thể không đầy đủ như non-streaming; index thường ổn định hơn.

---

## Lộ trình triển khai đề xuất (để bắt đầu coding sau)

- Giai đoạn 1 (1 ngày): bật model metrics file + kiểm tra logs/metrics hoạt động.
- Giai đoạn 2 (1-2 ngày): thêm registry + callback + xuất `stage_token_usage.*`.
- Giai đoạn 3 (0.5-1 ngày): thêm dashboard script và validate consistency.
- Giai đoạn 4 (0.5 ngày): nối với `pricing.yaml` để fallback cost calc.

---

## Kết luận

Bạn hoàn toàn có thể đo chi tiết API usage theo từng stage trong GraphRAG, không cần phụ thuộc OpenAI dashboard.  
Mấu chốt là: **model metrics + stage snapshot delta + output ledger**.  
Khi có ledger này, tối ưu chi phí sẽ rất “thấy được” và báo cáo với team cũng trực quan hơn nhiều.
