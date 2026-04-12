# Step 1: Reading Order & Workflow Overview

**START HERE.** This file gives you the reading order and a quick map of all docs in `md/step1/`.

---

## Reading Order

| Order | File | Purpose |
|:---:|---|---|
| 1 | `step_1_overview.md` (this file) | Map of all docs + workflow phases |
| 2 | `pipeline.md` ⭐ | **Full step-by-step**: OpenAI baseline → Ollama local → root cause → fix |
| 3 | `ollama_settings_templates.md` | 3 copy-paste `settings.yaml` presets for Ollama |
| 4 | `task_extraction.md` | Temporal Conflict extension master plan |

Supporting docs:
- `summary_focus_packages.md` — architecture deep-dive
- `summary_callgraph_focus.md` — function-level call graph
- `summary_trace_entity_query.md` — runtime trace example
- `cost_callback_llm_api.md` — cost tracking design
- `summary.md` — full repo overview

---

## Workflow Phases

### Phase 1 — Baseline OpenAI ✅

```
init workspace
  → put OpenAI key in .env
  → index (entities, relationships, communities, reports, embeddings)
  → query (global / local / drift / basic)
```

**Works out of the box.** No manual config needed after `init`.

### Phase 2 — Switch to Ollama Local

```
Same workspace (already has settings.yaml)
  → Fix settings.yaml for Ollama
  → Fix .env for Ollama
  → index again
  → query
```

**⚠️ Key difference:** Ollama uses `nomic-embed-text` with **768 dimensions**, while OpenAI uses `text-embedding-3-large` with **3072 dimensions**. If you don't fix this, the index **crashes**.

Root cause: `_validate_vector_store()` auto-creates index schemas with `DEFAULT_VECTOR_SIZE = 3072` if `index_schema` is missing.

Full fix: see `pipeline.md`.

### Phase 3 — Temporal Conflict Extension (add-only)

Add temporal layer on top of baseline without breaking it.

```
extract_graph (baseline)
  → extract_temporal_facts      ← NEW
  → resolve_temporal_conflicts ← NEW
  → create_communities
  → create_community_reports
  → generate_text_embeddings
```

See `task_extraction.md` for details.

---

## File Map

```
md/step1/
├── step_1_overview.md          ← YOU ARE HERE
├── pipeline.md                ← Full setup guide (START HERE for Ollama)
├── ollama_settings_templates.md ← 3 settings.yaml presets
├── task_extraction.md         ← Temporal extension plan
├── summary_focus_packages.md ← Architecture deep-dive
├── summary_callgraph_focus.md ← Call graph (function-level)
├── summary_trace_entity_query.md ← Runtime trace
├── cost_callback_llm_api.md  ← Cost tracking
└── summary.md                ← Full repo overview
```

---

## Quick Status

| Phase | Status | Next step |
|---|---|---|
| Baseline OpenAI | ✅ Working | Done |
| Ollama local | ⚠️ Needs manual config | Fix `settings.yaml` — see `pipeline.md` |
| Temporal extraction | 📋 Planning | Implement `extract_temporal_facts` workflow |
| Temporal conflict | 📋 Planning | Implement `resolve_temporal_conflicts` workflow |
| Temporal query | 📋 Planning | Extend local search context builder |
