#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────
# Benchmark E2E: preprocess 1 raw file → copy to input → graphrag index
# Usage:
#   bash scripts/benchmark_e2e.sh <raw_file> <preprocess_model> [optimized] [index_model]
#
# Examples:
#   bash scripts/benchmark_e2e.sh \
#       ../my_workspace/data/raw_txt/Aon_plc/AON_financials_2020_q1.txt \
#       llama3.1:latest optimized
#
#   # Hybrid: Qwen preprocesses, Llama indexes.
#   bash scripts/benchmark_e2e.sh \
#       ../my_workspace/data/raw_txt/Aon_plc/AON_financials_2020_q1.txt \
#       qwen3:14b optimized llama3.1:latest
#
#   bash scripts/benchmark_e2e.sh \
#       ../my_workspace/data/raw_txt/Crocs_Inc/CROX_consumer_discretionary_2024_q1.txt \
#       qwen3:14b
# ──────────────────────────────────────────────────────────────────
set -euo pipefail

RAW_FILE="${1:?Usage: $0 <raw_file> <preprocess_model> [optimized] [index_model]}"
PREPROCESS_MODEL="${2:?Usage: $0 <raw_file> <preprocess_model> [optimized] [index_model]}"
USE_OPTIMIZED="${3:-default}"
INDEX_MODEL="${4:-$PREPROCESS_MODEL}"

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILE_STEM=$(basename "$RAW_FILE" .txt)
PREPROCESS_MODEL_SAFE=$(echo "$PREPROCESS_MODEL" | tr ':' '_' | tr '/' '_')
INDEX_MODEL_SAFE=$(echo "$INDEX_MODEL" | tr ':' '_' | tr '/' '_')
if [ "$PREPROCESS_MODEL" = "$INDEX_MODEL" ]; then
    MODEL_LABEL="$PREPROCESS_MODEL_SAFE"
else
    MODEL_LABEL="pre_${PREPROCESS_MODEL_SAFE}__idx_${INDEX_MODEL_SAFE}"
fi
WS_NAME="bench_${FILE_STEM}_${MODEL_LABEL}_${TIMESTAMP}"
WS_DIR="${REPO_DIR}/../${WS_NAME}"

echo "═══════════════════════════════════════════════════════════"
echo "  BENCHMARK E2E"
echo "  File            : $RAW_FILE"
echo "  Preprocess model: $PREPROCESS_MODEL"
echo "  Index model     : $INDEX_MODEL"
echo "  Settings        : $USE_OPTIMIZED"
echo "  Workspace: $WS_DIR"
echo "═══════════════════════════════════════════════════════════"

# ── ENV ──
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_CHAT_MODEL="$INDEX_MODEL"
export OLLAMA_EMBED_MODEL=nomic-embed-text:latest
export OLLAMA_EMBED_DIM=768
export GRAPHRAG_API_KEY=ollama

# ── Step 1: Create workspace ──
echo ""
echo "[Step 1] Creating workspace..."
T1_START=$(date +%s%N)
mkdir -p "$WS_DIR/input"
T1_END=$(date +%s%N)
T1_MS=$(( (T1_END - T1_START) / 1000000 ))
echo "  Done (${T1_MS}ms)"

# ── Step 2: Init workspace ──
echo ""
echo "[Step 2] Init workspace..."
T2_START=$(date +%s%N)
cd "$REPO_DIR"
uv run python -m graphrag init \
    --root "$WS_DIR" \
    --model "$INDEX_MODEL" \
    --embedding "$OLLAMA_EMBED_MODEL"
T2_END=$(date +%s%N)
T2_MS=$(( (T2_END - T2_START) / 1000000 ))
echo "  Done (${T2_MS}ms)"

# ── Step 3: Copy settings + env ──
echo ""
echo "[Step 3] Configuring workspace..."
T3_START=$(date +%s%N)

cat > "$WS_DIR/.env" <<EOF
GRAPHRAG_API_KEY=ollama
OLLAMA_BASE_URL=${OLLAMA_BASE_URL}
OLLAMA_CHAT_MODEL=${OLLAMA_CHAT_MODEL}
OLLAMA_EMBED_MODEL=${OLLAMA_EMBED_MODEL}
OLLAMA_EMBED_DIM=${OLLAMA_EMBED_DIM}
EOF

if [ "$USE_OPTIMIZED" = "optimized" ] && [ -f "$REPO_DIR/configs/settings.ollama.optimized.yaml" ]; then
    cp "$REPO_DIR/configs/settings.ollama.optimized.yaml" "$WS_DIR/settings.yaml"
    echo "  Using OPTIMIZED settings (concurrent=2, embed_batch=16)"
else
    # Patch the default settings for Ollama
    cat > "$WS_DIR/settings.yaml" <<'YAMLEOF'
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

input:
  type: text
chunking:
  type: tokens
  size: 1200
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
embed_text:
  embedding_model_id: default_embedding_model
  batch_size: 1
  batch_max_tokens: 1024
  names: [entity_description, community_full_content, text_unit_text]
extract_graph:
  completion_model_id: default_completion_model
  prompt: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 0
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
YAMLEOF
    echo "  Using DEFAULT settings (concurrent=1, embed_batch=1)"
fi

cat > "$WS_DIR/prompts/extract_graph.txt" <<'PROMPTEOF'
/no_think

-Goal-
Given a text document and a list of entity types, identify entities of those types and relationships among them.

-Critical Output Rules-
Return ONLY tuple records.
Do NOT return Markdown headings, bullet lists, JSON, code fences, explanations, notes, or a final-answer section.
Every entity must use exactly:
("entity"<|><entity_name><|><entity_type><|><entity_description>)
Every relationship must use exactly:
("relationship"<|><source_entity><|><target_entity><|><relation_type><|><relationship_description><|><relationship_strength>)
Use ## between records.
End with <|COMPLETE|>.

-Steps-
1. Identify entities.
- entity_name: capitalized entity name
- entity_type: one of [{entity_types}]
- entity_description: concise evidence-based description from the text
Format:
("entity"<|><entity_name><|><entity_type><|><entity_description>)

2. Identify clearly related entity pairs.
- source_entity: exact entity name from step 1
- target_entity: exact entity name from step 1
- relation_type: concise UPPER_SNAKE_CASE label, such as PART_OF, AFFECTS, LOCATED_IN, ANNOUNCED, ACQUIRED, PARTNERED_WITH
- relationship_description: evidence-based description from the text
- relationship_strength: numeric score from 1 to 10
Format:
("relationship"<|><source_entity><|><target_entity><|><relation_type><|><relationship_description><|><relationship_strength>)

3. Return a single list of tuple records in English.
4. Output <|COMPLETE|> when finished.

######################
-Examples-
######################
Entity_types: ORGANIZATION,PERSON,GEO,EVENT
Text:
Aon announced that its Reinsurance Solutions segment delivered 9% organic revenue growth in Q1 2020. CEO Greg Case said the Aon United strategy helped teams respond to COVID-19 and serve clients in New York.
######################
Output:
("entity"<|>AON<|>ORGANIZATION<|>Aon is the company discussing Q1 2020 results)
##
("entity"<|>REINSURANCE SOLUTIONS<|>ORGANIZATION<|>Reinsurance Solutions is an Aon segment that delivered 9% organic revenue growth)
##
("entity"<|>GREG CASE<|>PERSON<|>Greg Case is Aon's CEO)
##
("entity"<|>AON UNITED<|>ORGANIZATION<|>Aon United is a strategy used by Aon teams)
##
("entity"<|>COVID-19<|>EVENT<|>COVID-19 is the crisis Aon teams responded to)
##
("entity"<|>NEW YORK<|>GEO<|>New York is a client location mentioned in the text)
##
("relationship"<|>REINSURANCE SOLUTIONS<|>AON<|>PART_OF<|>Reinsurance Solutions is a segment of Aon<|>9)
##
("relationship"<|>GREG CASE<|>AON<|>CEO_OF<|>Greg Case is Aon's CEO<|>10)
##
("relationship"<|>AON UNITED<|>COVID-19<|>USED_TO_RESPOND_TO<|>Aon United helped teams respond to COVID-19<|>8)
##
("relationship"<|>AON<|>NEW YORK<|>SERVES_CLIENTS_IN<|>Aon served clients in New York<|>6)
<|COMPLETE|>

######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
PROMPTEOF

T3_END=$(date +%s%N)
T3_MS=$(( (T3_END - T3_START) / 1000000 ))
echo "  Done (${T3_MS}ms)"

# ── Step 4: Preprocess raw file ──
echo ""
echo "[Step 4] Preprocessing: $FILE_STEM with $PREPROCESS_MODEL ..."
T4_START=$(date +%s%N)
cd "$REPO_DIR"
uv run python -m scripts.data_prep.preprocess_corpus \
    --env-file "$WS_DIR/.env" \
    --input "$RAW_FILE" \
    --output "$WS_DIR/data/clean_corpus/" \
    --mode file \
    --model "$PREPROCESS_MODEL" \
    --batch-size 30 \
    --review-batch-size 30 \
    --context-window 1 \
    --review-window 1 \
    --fallback-policy abort \
    --timeout 600 2>&1 | tee "$WS_DIR/preprocess.log"
T4_END=$(date +%s%N)
T4_SEC=$(( (T4_END - T4_START) / 1000000000 ))
echo "  Preprocessing done (${T4_SEC}s)"

# ── Step 4.1: Read preprocessing quality metrics ──
QUALITY_JSON="$WS_DIR/data/clean_corpus/drop_logs/$(basename "$(dirname "$RAW_FILE")")/${FILE_STEM}.analysis.json"
SENTENCE_UNITS_BEFORE=null
SENTENCE_UNITS_AFTER=null
RETENTION_PCT=null
FINAL_REDUCTION_PCT=null
FALLBACK_COUNT=null
RESCUED_BY_REVIEW=null

if [ -f "$QUALITY_JSON" ] && command -v jq >/dev/null 2>&1; then
    SENTENCE_UNITS_BEFORE=$(jq -r '.quality_report.sentence_units_before // null' "$QUALITY_JSON")
    SENTENCE_UNITS_AFTER=$(jq -r '.quality_report.sentence_units_after // null' "$QUALITY_JSON")
    RETENTION_PCT=$(jq -r '.quality_report.retention_pct // null' "$QUALITY_JSON")
    FINAL_REDUCTION_PCT=$(jq -r '.quality_report.final_reduction_pct // null' "$QUALITY_JSON")
    FALLBACK_COUNT=$(jq -r '.quality_report.fallback_count // null' "$QUALITY_JSON")
    RESCUED_BY_REVIEW=$(jq -r '.quality_report.rescued_by_review // null' "$QUALITY_JSON")
fi

# ── Step 5: Copy clean to input ──
echo ""
echo "[Step 5] Copying clean corpus to input..."
T5_START=$(date +%s%N)
cd "$REPO_DIR"
uv run python scripts/data_prep/prepare_graphrag_input.py \
    --clean-corpus "$WS_DIR/data/clean_corpus" \
    --workspace-input "$WS_DIR/input" \
    --clear --flatten
T5_END=$(date +%s%N)
T5_MS=$(( (T5_END - T5_START) / 1000000 ))
echo "  Done (${T5_MS}ms)"

# ── Step 6: Run GraphRAG index ──
echo ""
echo "[Step 6] Running GraphRAG index..."
T6_START=$(date +%s%N)
cd "$REPO_DIR"
uv run python -m graphrag index --root "$WS_DIR" 2>&1 | tee "$WS_DIR/index.log"
T6_END=$(date +%s%N)
T6_SEC=$(( (T6_END - T6_START) / 1000000000 ))
echo "  Indexing done (${T6_SEC}s)"

# ── Step 7: Report ──
TOTAL_SEC=$(( (T6_END - T1_START) / 1000000000 ))

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  BENCHMARK RESULTS"
echo "═══════════════════════════════════════════════════════════"
echo "  File       : $FILE_STEM"
echo "  Preprocess : $PREPROCESS_MODEL"
echo "  Index      : $INDEX_MODEL"
echo "  Settings   : $USE_OPTIMIZED"
echo "  Workspace  : $WS_DIR"
echo "───────────────────────────────────────────────────────────"
echo "  Create workspace : ${T1_MS}ms"
echo "  Init workspace   : ${T2_MS}ms"
echo "  Configure        : ${T3_MS}ms"
echo "  Preprocess       : ${T4_SEC}s"
echo "  Retention        : ${RETENTION_PCT}%"
echo "  Fallback         : ${FALLBACK_COUNT}"
echo "  Copy to input    : ${T5_MS}ms"
echo "  Index            : ${T6_SEC}s"
echo "  TOTAL            : ${TOTAL_SEC}s"
echo "═══════════════════════════════════════════════════════════"

# Save report
cat > "$WS_DIR/benchmark_report.json" <<EOF
{
    "file": "$FILE_STEM",
    "preprocess_model": "$PREPROCESS_MODEL",
    "index_model": "$INDEX_MODEL",
    "settings": "$USE_OPTIMIZED",
    "workspace": "$WS_DIR",
    "preprocess_quality": {
        "analysis_json": "$QUALITY_JSON",
        "sentence_units_before": $SENTENCE_UNITS_BEFORE,
        "sentence_units_after": $SENTENCE_UNITS_AFTER,
        "retention_pct": $RETENTION_PCT,
        "final_reduction_pct": $FINAL_REDUCTION_PCT,
        "fallback_count": $FALLBACK_COUNT,
        "rescued_by_review": $RESCUED_BY_REVIEW
    },
    "timing": {
        "create_workspace_ms": $T1_MS,
        "init_workspace_ms": $T2_MS,
        "configure_ms": $T3_MS,
        "preprocess_s": $T4_SEC,
        "copy_to_input_ms": $T5_MS,
        "index_s": $T6_SEC,
        "total_s": $TOTAL_SEC
    }
}
EOF

echo ""
echo "Stats from GraphRAG:"
cat "$WS_DIR/output/stats.json" 2>/dev/null || echo "(no stats.json)"
echo ""
echo "Report saved to: $WS_DIR/benchmark_report.json"
