# Ollama Settings Templates

3 copy-paste `settings.yaml` presets cho Ollama local. Chọn preset phù hợp với cấu hình máy của bạn.

---

## Preset 1: Ollama Minimal (recommended — khuyến nghị dùng)

Phù hợp cho hầu hết setup Ollama local thông thường.

**Giả định:**
- Completion: `llama3.1:latest`
- Embedding: `nomic-embed-text:latest` (768 chiều)
- Vector store: LanceDB

```yaml
### This config file contains required core defaults that must be set, along with a handful of common optional settings.
### For a full list of available settings, see https://microsoft.github.io/graphrag/config/yaml/

### LLM settings ###
## There are a number of settings to tune the threading and token limits for LLM calls - check the docs.

completion_models:
  default_completion_model:
    model_provider: ollama
    model: llama3.1:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

embedding_models:
  default_embedding_model:
    model_provider: ollama
    model: nomic-embed-text:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

### Document processing settings ###

input:
  type: text

chunking:
  type: tokens
  size: 500
  overlap: 80
  encoding_model: o200k_base

### Storage settings ###

input_storage:
  type: file
  base_dir: "input"

output_storage:
  type: file
  base_dir: "output"

reporting:
  type: file
  base_dir: "logs"

cache:
  type: json
  storage:
    type: file
    base_dir: "cache"

### Vector Store ###
## ⚠️ CRITICAL: vector_size phải khớp với embedding model
## nomic-embed-text = 768 chiều
## text-embedding-3-large (OpenAI) = 3072 chiều
vector_store:
  type: lancedb
  db_uri: output/lancedb
  vector_size: 768
  index_schema:
    text_unit_text:
      index_name: text_unit_text
      vector_size: 768
    entity_description:
      index_name: entity_description
      vector_size: 768
    community_full_content:
      index_name: community_full_content
      vector_size: 768

### Workflow settings ###

embed_text:
  embedding_model_id: default_embedding_model
  batch_size: 1
  batch_max_tokens: 1024
  names: [entity_description, community_full_content, text_unit_text]

extract_graph:
  completion_model_id: default_completion_model
  prompt: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 1

summarize_descriptions:
  completion_model_id: default_completion_model
  prompt: "prompts/summarize_descriptions.txt"
  max_length: 500

extract_graph_nlp:
  text_analyzer:
    extractor_type: regex_english

cluster_graph:
  max_cluster_size: 10

extract_claims:
  enabled: false
  completion_model_id: default_completion_model
  prompt: "prompts/extract_claims.txt"
  description: "Any claims or facts that could be relevant to information discovery."
  max_gleanings: 1

community_reports:
  completion_model_id: default_completion_model
  graph_prompt: "prompts/community_report_graph.txt"
  text_prompt: "prompts/community_report_text.txt"
  max_length: 2000
  max_input_length: 8000

snapshots:
  graphml: false
  embeddings: false

### Query settings ###

local_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/local_search_system_prompt.txt"

global_search:
  completion_model_id: default_completion_model
  map_prompt: "prompts/global_search_map_system_prompt.txt"
  reduce_prompt: "prompts/global_search_reduce_system_prompt.txt"
  knowledge_prompt: "prompts/global_search_knowledge_system_prompt.txt"

drift_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/drift_search_system_prompt.txt"
  reduce_prompt: "prompts/drift_search_reduce_prompt.txt"

basic_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/basic_search_system_prompt.txt"
```

---

## Preset 2: Ollama Fast (máy yếu / RAM thấp)

Tối ưu cho máy có ít RAM hoặc Ollama chạy chậm.

**Giả định:** Same models, nhưng giảm chunk size, giảm concurrency.

```yaml
### Ollama Fast Preset — cho máy yếu / RAM thấp

completion_models:
  default_completion_model:
    model_provider: ollama
    model: llama3.1:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

embedding_models:
  default_embedding_model:
    model_provider: ollama
    model: nomic-embed-text:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

input:
  type: text

chunking:
  type: tokens
  size: 300           # ← giảm từ 500 xuống 300 cho nhanh
  overlap: 50
  encoding_model: o200k_base

input_storage:
  type: file
  base_dir: "input"

output_storage:
  type: file
  base_dir: "output"

reporting:
  type: file
  base_dir: "logs"

cache:
  type: json
  storage:
    type: file
    base_dir: "cache"

vector_store:
  type: lancedb
  db_uri: output/lancedb
  vector_size: 768
  index_schema:
    text_unit_text:
      index_name: text_unit_text
      vector_size: 768
    entity_description:
      index_name: entity_description
      vector_size: 768
    community_full_content:
      index_name: community_full_content
      vector_size: 768

# ⚠️ Quan trọng: concurrent_requests thấp
concurrent_requests: 1

embed_text:
  embedding_model_id: default_embedding_model
  batch_size: 1
  batch_max_tokens: 512   # ← giảm từ 1024
  names: [entity_description, community_full_content, text_unit_text]

extract_graph:
  completion_model_id: default_completion_model
  prompt: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 1

summarize_descriptions:
  completion_model_id: default_completion_model
  prompt: "prompts/summarize_descriptions.txt"
  max_length: 500

extract_graph_nlp:
  text_analyzer:
    extractor_type: regex_english

cluster_graph:
  max_cluster_size: 10

extract_claims:
  enabled: false
  completion_model_id: default_completion_model
  prompt: "prompts/extract_claims.txt"
  description: "Any claims or facts that could be relevant to information discovery."
  max_gleanings: 1

community_reports:
  completion_model_id: default_completion_model
  graph_prompt: "prompts/community_report_graph.txt"
  text_prompt: "prompts/community_report_text.txt"
  max_length: 2000
  max_input_length: 8000

snapshots:
  graphml: false
  embeddings: false

local_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/local_search_system_prompt.txt"

global_search:
  completion_model_id: default_completion_model
  map_prompt: "prompts/global_search_map_system_prompt.txt"
  reduce_prompt: "prompts/global_search_reduce_system_prompt.txt"
  knowledge_prompt: "prompts/global_search_knowledge_system_prompt.txt"

drift_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/drift_search_system_prompt.txt"
  reduce_prompt: "prompts/drift_search_reduce_prompt.txt"

basic_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/basic_search_system_prompt.txt"
```

---

## Preset 3: Ollama High-Quality (máy mạnh)

Cho máy có nhiều RAM / GPU mạnh. Chunk lớn hơn, context token cao hơn.

**Giả định:** Same models, nhưng tăng chunk size, tăng max_gleanings.

```yaml
### Ollama High-Quality Preset — cho máy mạnh / GPU

completion_models:
  default_completion_model:
    model_provider: ollama
    model: llama3.1:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

embedding_models:
  default_embedding_model:
    model_provider: ollama
    model: nomic-embed-text:latest
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: http://localhost:11434
    retry:
      type: exponential_backoff

input:
  type: text

chunking:
  type: tokens
  size: 1000          # ← tăng từ 500 lên 1000
  overlap: 100
  encoding_model: o200k_base

input_storage:
  type: file
  base_dir: "input"

output_storage:
  type: file
  base_dir: "output"

reporting:
  type: file
  base_dir: "logs"

cache:
  type: json
  storage:
    type: file
    base_dir: "cache"

vector_store:
  type: lancedb
  db_uri: output/lancedb
  vector_size: 768
  index_schema:
    text_unit_text:
      index_name: text_unit_text
      vector_size: 768
    entity_description:
      index_name: entity_description
      vector_size: 768
    community_full_content:
      index_name: community_full_content
      vector_size: 768

concurrent_requests: 1

embed_text:
  embedding_model_id: default_embedding_model
  batch_size: 1
  batch_max_tokens: 1024
  names: [entity_description, community_full_content, text_unit_text]

extract_graph:
  completion_model_id: default_completion_model
  prompt: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 2      # ← tăng từ 1 lên 2 → trích xuất tốt hơn

summarize_descriptions:
  completion_model_id: default_completion_model
  prompt: "prompts/summarize_descriptions.txt"
  max_length: 500

extract_graph_nlp:
  text_analyzer:
    extractor_type: regex_english

cluster_graph:
  max_cluster_size: 10

extract_claims:
  enabled: false
  completion_model_id: default_completion_model
  prompt: "prompts/extract_claims.txt"
  description: "Any claims or facts that could be relevant to information discovery."
  max_gleanings: 1

community_reports:
  completion_model_id: default_completion_model
  graph_prompt: "prompts/community_report_graph.txt"
  text_prompt: "prompts/community_report_text.txt"
  max_length: 2000
  max_input_length: 8000

snapshots:
  graphml: false
  embeddings: false

local_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/local_search_system_prompt.txt"

global_search:
  completion_model_id: default_completion_model
  map_prompt: "prompts/global_search_map_system_prompt.txt"
  reduce_prompt: "prompts/global_search_reduce_system_prompt.txt"
  knowledge_prompt: "prompts/global_search_knowledge_system_prompt.txt"

drift_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/drift_search_system_prompt.txt"
  reduce_prompt: "prompts/drift_search_reduce_prompt.txt"

basic_search:
  completion_model_id: default_completion_model
  embedding_model_id: default_embedding_model
  prompt: "prompts/basic_search_system_prompt.txt"
```

---

## So sánh nhanh: 3 Presets

| Cài đặt | Minimal | Fast | High-Quality |
|---|---|---|---|
| `chunking.size` | 500 | 300 | 1000 |
| `embed_text.batch_size` | 1 | 1 | 1 |
| `extract_graph.max_gleanings` | 1 | 1 | 2 |
| `concurrent_requests` | mặc định | 1 | mặc định |
| Phù hợp | Hầu hết máy | Máy yếu / RAM thấp | Máy mạnh / GPU |

---

## Cách áp dụng

1. Chạy `graphrag init --root <workspace> --model llama3.1:latest --embedding nomic-embed-text:latest`
2. Thay thế toàn bộ file `settings.yaml` trong workspace bằng preset đã chọn
3. Sửa `.env`: `GRAPHRAG_API_KEY=OLLAMA_DUMMY_KEY`
4. Chạy `uv run python -m graphrag index --root <workspace>`

**Lưu ý:** Tất cả 3 presets đều dùng `llama3.1:latest` và `nomic-embed-text:latest`. Nếu bạn dùng model khác:
- Đổi `model:` trong `completion_models` và `embedding_models`
- Đổi `vector_size` cho khớp với embedding model thực tế của bạn
- Cập nhật cả 3 entries trong `index_schema` theo `vector_size` mới
