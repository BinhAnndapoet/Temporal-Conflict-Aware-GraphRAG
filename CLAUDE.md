# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **uv workspace monorepo** containing GraphRAG v3.0.7 with **Temporal Conflict-Aware** extension goals.

**Quick start — Step 1:** Đọc `md/step1/step_1_overview.md` → `md/step1/pipeline.md` để setup và chạy index/query thành công.

**Workspace outside repo:** All outputs (data, logs, artifacts) go to a **workspace directory outside the repo**, keeping source code clean.

## Documentation (`md/step1/`)

| File | Purpose |
|------|---------|
| `md/step1/step_1_overview.md` ⭐ | **START HERE** — Reading order + workflow overview |
| `md/step1/pipeline.md` | Full setup guide: OpenAI vs Ollama, root cause, step-by-step config, 3 presets, troubleshooting. Test confirmed: Index + Query 100% success with Ollama local. |
| `md/step1/task_extraction.md` | Master plan for Temporal Conflict extension (add-only approach) |
| `md/step1/ollama_settings_templates.md` | 3 Ollama config presets |
| `md/step1/summary*.md` | Architecture deep-dives (callgraph, packages, trace) |
| `md/step1/cost_callback_llm_api.md` | Cost tracking design |

## Repository Structure

```
Temporal-Conflict-Aware-GraphRAG/
├── pyproject.toml          # Root: uv workspace + poethepoet tasks + tool config
├── uv.lock
├── packages/               # All source packages (editable installs)
│   ├── graphrag/           # Main CLI + pipeline + query (depends on all others)
│   ├── graphrag-llm/       # LLM abstraction (wraps LiteLLM: ollama/openai/azure)
│   ├── graphrag-chunking/  # Text → chunks (sentence/token chunkers)
│   ├── graphrag-storage/   # Storage layer (file/Azure Blob/Cosmos/Memory)
│   ├── graphrag-vectors/   # Vector stores (LanceDB default, Azure AI Search, Cosmos)
│   ├── graphrag-cache/     # LLM response caching (Json/Memory/Noop)
│   ├── graphrag-common/    # Config loading, factory pattern, hashing
│   └── graphrag-input/     # Document loading (text/CSV/PDF via markitdown)
├── tests/                  # Full test suite (unit/integration/smoke/verbs)
├── scripts/                # Dev utilities (build, parquet conversion, release)
└── md/                     # Design docs (Vietnamese + English)
```

## Common Commands

All commands run from the **repo root** (never from the workspace directory).

### Environment Setup

```bash
uv sync --all-packages          # Sync + create .venv + editable install (run once after clone or dependency changes)
```

### CLI Workflow (workspace outside repo)

```bash
# ⚠️ INIT: OpenAI — non-interactive
uv run python -m graphrag init --root /home/manh/Projects/ban/my_workspace

# ⚠️ INIT: Ollama — MUST pass --model and --embedding non-interactive
# (without flags, Typer prompts for model and defaults to gpt-4.1)
uv run python -m graphrag init --root /home/manh/Projects/ban/my_workspace_ollama \
  --model llama3.1:latest --embedding nomic-embed-text:latest

# Index
uv run python -m graphrag index --root /home/manh/Projects/ban/my_workspace

# Query
uv run python -m graphrag query --root /home/manh/Projects/ban/my_workspace --method global "question"

# Update (incremental — temporal conflict detection lives here)
uv run python -m graphrag update --root /home/manh/Projects/ban/my_workspace
```

### Development Tools (via poethepoet)

```bash
poe format        # Sort imports + ruff format
poe check         # Format check + ruff lint + pyright
poe fix           # Ruff auto-fix
poe test          # Full test suite + coverage report
poe test_unit     # Unit tests only
poe test_integration  # Integration tests only
poe test_smoke    # Smoke tests only
poe test_only -k "pattern"   # Run tests matching pattern
```

### Key Configuration Files

- **`md/step1/pipeline.md`**: Full setup guide — **read this first**
- **Default `settings.yaml` scaffold**: `packages/graphrag/graphrag/config/init_content.py` (`INIT_YAML`, `INIT_DOTENV`)
- **Default values**: `packages/graphrag/graphrag/config/defaults.py`
- **Config models (Pydantic)**: `packages/graphrag/graphrag/config/models/graph_rag_config.py`

## Ollama Local Setup — Quick Reference

> Full details: see `md/step1/pipeline.md`. This section is a quick reference.

### Critical bug: `init` requires non-interactive flags for Ollama

```bash
# ❌ Interactive — will prompt for model and default to gpt-4.1
uv run python -m graphrag init --root /path/to/workspace

# ✅ Non-interactive — must pass both flags
uv run python -m graphrag init --root /path/to/workspace \
  --model llama3.1:latest --embedding nomic-embed-text:latest
```

### After `init`, edit `settings.yaml` — 5 groups

1. **`.env`**: `GRAPHRAG_API_KEY=OLLAMA_DUMMY_KEY`
2. **`completion_models`**: `model_provider: ollama`, `model: llama3.1:latest`, add `api_base: http://localhost:11434`
3. **`embedding_models`**: `model_provider: ollama`, `model: nomic-embed-text:latest`, add `api_base: http://localhost:11434`
4. **`vector_store`** (CRITICAL): add `vector_size: 768` + full `index_schema` with all 3 entries at `vector_size: 768`
5. **(Recommended)**: `concurrent_requests: 1`, `embed_text.batch_size: 1`, `chunking.size: 500`

### Root cause of the embedding crash

`graphrag init` scaffold has no `index_schema` → `_validate_vector_store()` auto-creates 3 schemas with `DEFAULT_VECTOR_SIZE = 3072`. OpenAI `text-embedding-3-large` = 3072 ✅. Ollama `nomic-embed-text` = 768 ❌ → LanceDB dimension mismatch crash.

Full `settings.yaml` copy-paste ready for Ollama: see `md/step1/pipeline.md` Section 8.

## Architecture

Full architecture guide: see `md/step1/pipeline.md` (Section 1) and `md/step1/summary_focus_packages.md`.

### Indexing Pipeline

`graphrag index` → `build_index()` in `graphrag/api/index.py` → `PipelineRunner` in `graphrag/index/run/run_pipeline.py`

Standard pipeline workflows (defined in `graphrag/index/workflows/factory.py`):
```
load_input_documents
  → create_base_text_units          (via graphrag-chunking)
  → create_final_documents
  → extract_graph                   ← LLM: entity + relationship extraction
  → finalize_graph
  → extract_covariates              (optional: claim extraction)
  → create_communities             (Leiden hierarchical clustering)
  → create_final_text_units
  → create_community_reports       ← LLM: community summaries
  → generate_text_embeddings       ← LLM embedding → LanceDB
```

Fast pipeline skips LLM for graph extraction (NLP noun-phrase only).

### Query Engines

`graphrag query --method <mode>` dispatches via `graphrag/query/factory.py`:

| Mode | Strategy |
|------|----------|
| `global` | Map-reduce over community reports |
| `local` | Entity-centric: graph neighbors + text + reports |
| `drift` | Global primer → iterative local follow-up loop |
| `basic` | Pure vector similarity on text units |

### How Packages Connect

```
CLI (graphrag/cli/main.py)
  │
  ├─► graphrag-llm/         LiteLLM completion + embedding
  ├─► graphrag-chunking/   Sentence/token chunking
  ├─► graphrag-storage/    Parquet/Blob/Cosmos read-write
  ├─► graphrag-vectors/    LanceDB vector indexing
  ├─► graphrag-cache/      LLM response caching
  ├─► graphrag-common/     Config loading, factory registry
  └─► graphrag-input/      Text/CSV/PDF document loading
```

## Temporal Conflict Extension — Add-Only Approach

Full plan: see `md/step1/task_extraction.md`. Key principle: **add new files, never overwrite baseline**.

The `update` pipeline (`graphrag update`) is the natural place to detect temporal conflicts — it processes new time-stamped documents and resolves contradictions against the existing graph.

| Purpose | Location |
|---------|----------|
| Temporal config model | `packages/graphrag/graphrag/config/models/temporal_extraction_config.py` (new) |
| Register temporal config | `packages/graphrag/graphrag/config/models/graph_rag_config.py` (edit — add field only) |
| Temporal fact extraction workflow | `packages/graphrag/graphrag/index/workflows/extract_temporal_facts.py` (new) |
| Conflict resolution workflow | `packages/graphrag/graphrag/index/workflows/resolve_temporal_conflicts.py` (new) |
| Register new workflows | `packages/graphrag/graphrag/index/workflows/factory.py` (edit — register only) |
| Temporal operations | `packages/graphrag/graphrag/index/operations/extract_temporal/` (new dir) |
| Prompt for temporal extraction | `packages/graphrag/graphrag/prompts/index/extract_temporal_facts.py` (new) |

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `No module named graphrag` | `.venv` not synced | `uv sync --all-packages` |
| `model 'llama3.1' not found` | Name mismatch with `ollama list` | Always use exact name: `llama3.1:latest` (with `:latest`) |
| `expected 3072, got 768` | `vector_size` mismatch | Set `vector_size: 768` + full `index_schema` in `settings.yaml` |
| `Graph Extraction failed. No relationships detected` | Input data lacks entity relationships | Use complete sentences, not bullet points |
| Pipeline very slow / timeout | `concurrent_requests: 25` too high for Ollama local | Set `concurrent_requests: 1`, `embed_text.batch_size: 1` |
| `Project already initialized at ...` | Workspace already has `settings.yaml` | Normal — skip `init`, go to `index` |
| Interactive prompt on `init` | Missing `--model` flags | Always use: `init --root ... --model llama3.1:latest --embedding nomic-embed-text:latest` |
