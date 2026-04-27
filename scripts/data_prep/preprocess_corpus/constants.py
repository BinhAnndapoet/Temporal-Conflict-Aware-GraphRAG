"""Constants, prompts, and configuration for the preprocessing pipeline."""

from __future__ import annotations

# ────────────────────────────────────────────────────────────────
# LLM / Ollama defaults
# ────────────────────────────────────────────────────────────────

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "qwen3:14b"
DEFAULT_BATCH_SIZE = 20
DEFAULT_REVIEW_BATCH_SIZE = 20
DEFAULT_NUM_CTX = 8192

# ────────────────────────────────────────────────────────────────
# Decision sets
# ────────────────────────────────────────────────────────────────

ALLOWED_INITIAL_DECISIONS = {"KEEP_FACT", "KEEP_CONTEXT", "MOVE_TO_METADATA", "DISCARD"}
ALLOWED_REVIEW_DECISIONS = {"RESCUE_KEEP_FACT", "RESCUE_KEEP_CONTEXT", "MOVE_TO_METADATA", "CONFIRM_DISCARD"}
ALLOWED_KEEP_REVIEW_DECISIONS = {"CONFIRM_KEEP", "MOVE_TO_METADATA", "DROP_NOISE"}
ALLOWED_AUDIT_LABELS = {"CORRECT_KEEP", "POSSIBLE_FALSE_KEEP", "CORRECT_DROP", "POSSIBLE_FALSE_DROP", "METADATA_ONLY"}

# ────────────────────────────────────────────────────────────────
# Abbreviations for sentence splitting (mechanical only)
# ────────────────────────────────────────────────────────────────

ABBREVIATIONS = [
    "Inc.", "Co.", "Corp.", "Ltd.", "LLC.", "L.P.", "PLC.", "plc.",
    "U.S.", "U.K.", "U.A.E.",
    "Mr.", "Ms.", "Mrs.", "Dr.",
    "vs.", "e.g.", "i.e.",
    "No.", "St.",
]

# ────────────────────────────────────────────────────────────────
# LLM Prompts
# ────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a careful business transcript evidence filter for Temporal GraphRAG Document Extraction.

You preprocess earnings-call transcript sentence units from multiple companies and sectors.
Your job is to preserve original evidence that may support temporal graph facts, while removing only transcript noise.

You never rewrite, summarize, normalize, translate, or add information.
You only decide whether each original sentence unit should be kept in clean text, moved to metadata, or removed."""

INITIAL_PROMPT_TEMPLATE = """/no_think
You are preprocessing sentence units from a corporate earnings-call transcript for Temporal GraphRAG Document Extraction.

Downstream stage:
The next stage will extract temporal knowledge facts such as:
(Entity 1, Relation, Entity 2, Time) with provenance.

Your task:
For every TARGET sentence, choose exactly one decision:
- KEEP_FACT: keep the original target sentence because it supports at least one graph-extractable fact.
- KEEP_CONTEXT: keep the original target sentence because it is a short local anchor that helps nearby facts keep their subject, section, time, brand, segment, or scope.
- MOVE_TO_METADATA: remove from clean text but preserve as document-level metadata/convention.
- DISCARD: remove the original target sentence because it is clearly pure transcript noise.

Decision applies ONLY to the target sentence. The context_before/context_after fields are only there to help you understand the target.

High-recall policy:
- Prefer KEEP_FACT unless the target sentence is clearly pure noise.
- A sentence does NOT need numbers to be KEEP_FACT.
- Qualitative business evidence is still evidence.
- Keep concrete company-specific evidence, including business states, actions, changes, trends, expectations, causes, commitments, availability, risks, market conditions, operational behavior, partner/customer/channel behavior, leadership changes, product/service launches, strategy, guidance/outlook, quantitative metrics, capital allocation, ESG/operations, macro impacts, and temporal comparisons.
- If uncertain between KEEP_FACT and DISCARD, choose KEEP_FACT.

KEEP_CONTEXT policy:
- Use KEEP_CONTEXT only when the target is a local anchor that helps nearby factual sentences resolve subject/scope/time.
- Good examples: "Turning to HEYDUDE.", "Now turning to guidance.", "Starting with the Crocs brand.", "By geography."
- Do NOT use KEEP_CONTEXT for greetings, thank-you sentences, participant introductions, speaker handoffs, generic call titles, or safe-harbor text.

MOVE_TO_METADATA policy:
- Use MOVE_TO_METADATA for reporting conventions or measurement basis that may affect interpretation but should not be passed as graph evidence.
- Examples: constant-currency basis, non-GAAP measurement definition, reconciliation location if useful for audit.
- Do NOT use KEEP_FACT for generic non-GAAP or safe-harbor wording.

DISCARD policy:
- DISCARD pure greeting, thanks, speaker name/title, separator, operator instruction, call logistics, speaker handoff, participant introduction, safe-harbor/legal boilerplate, SEC filing reference, press release location reference, or generic filler.
- Safe-harbor sentences remain DISCARD even if they mention strategy, plans, objectives, expectations, risks, or outlook generically.
- Generic mentions of risks/expectations/objectives inside legal disclaimers are NOT company-specific graph facts.

Important:
- Do NOT rewrite, summarize, normalize, correct, translate, or add information.
- Keep original evidence if it can plausibly support a graph fact.
- Do not discard just because the sentence lacks numbers.

Document metadata inferred from filename:
{document_metadata_json}

Return ONLY valid JSON. The JSON must be one object with this exact structure:
{{
  "decisions": [
    {{
      "source_id": "string exactly as provided",
      "decision": "KEEP_FACT or KEEP_CONTEXT or MOVE_TO_METADATA or DISCARD",
      "reason": "short reason",
      "fact_category": "metric | guidance_outlook | strategy | product_service | market_geography | leadership | operations | risk_macro | ESG | capital_allocation | customer_partner_channel | context_anchor | reporting_convention | metadata | speaker | logistics | boilerplate | greeting | other"
    }}
  ]
}}

Input items:
{input_json}
"""

DROP_REVIEW_PROMPT_TEMPLATE = """/no_think
You are reviewing sentences that were initially marked DISCARD during preprocessing for Temporal GraphRAG Document Extraction.

Purpose:
Prevent false drops, but do NOT rescue normal transcript noise.

For every TARGET sentence, choose exactly one review_decision:
- RESCUE_KEEP_FACT: the target sentence should be kept because it contains concrete company-specific business evidence.
- RESCUE_KEEP_CONTEXT: the target sentence should be kept because it is a necessary local anchor for nearby facts.
- MOVE_TO_METADATA: the target is useful as document-level convention/metadata but should not enter clean text.
- CONFIRM_DISCARD: the target is truly noise/boilerplate/logistics.

Strict rescue policy:
- Do NOT rescue greetings or thank-you sentences.
- Do NOT rescue participant introductions.
- Do NOT rescue speaker handoffs.
- Do NOT rescue generic call titles.
- Do NOT rescue safe-harbor/legal boilerplate.
- Do NOT rescue generic risk disclaimer sentences unless they describe a concrete company-specific risk/event/state.
- Do NOT rescue a sentence just because it mentions the company name or quarter; document metadata already provides that.
- Do NOT rescue generic mentions of strategy, objectives, risks, expectations, outlook, or plans inside legal disclaimers.
- Rescue qualitative operational facts, business states, product/market actions, leadership changes, guidance drivers, capital allocation decisions, ESG/operations facts, and concrete risk/macro impacts.
- If unsure whether it is graph evidence, rescue.
- If unsure whether it is transcript noise, confirm discard.

Do NOT rewrite the sentence.

Document metadata inferred from filename:
{document_metadata_json}

Return ONLY valid JSON:
{{
  "decisions": [
    {{
      "source_id": "string exactly as provided",
      "review_decision": "RESCUE_KEEP_FACT or RESCUE_KEEP_CONTEXT or MOVE_TO_METADATA or CONFIRM_DISCARD",
      "reason": "short reason",
      "fact_category": "metric | guidance_outlook | strategy | product_service | market_geography | leadership | operations | risk_macro | ESG | capital_allocation | customer_partner_channel | context_anchor | reporting_convention | metadata | speaker | logistics | boilerplate | greeting | other"
    }}
  ]
}}

Initial DISCARD candidates with local context:
{input_json}
"""

KEEP_REVIEW_PROMPT_TEMPLATE = """/no_think
You are auditing sentence units that were initially kept or rescued during preprocessing for Temporal GraphRAG Document Extraction.

Purpose:
Prevent false keeps in the clean corpus.

For every TARGET sentence, choose exactly one keep_review_decision:
- CONFIRM_KEEP: target should remain in clean text as graph evidence or necessary local context.
- MOVE_TO_METADATA: target should be removed from clean text but preserved as metadata/convention.
- DROP_NOISE: target should be removed from clean text.

Strict keep policy:
- Keep only original target sentences that help downstream Document Extraction.
- KEEP_CONTEXT is valid only if the target locally resolves subject/scope/time for nearby facts.
- Do NOT keep greetings or thank-you lines as context.
- Do NOT keep speaker handoffs as context.
- Do NOT keep participant-introduction sentences in clean text.
- Do NOT keep safe-harbor/legal boilerplate even if it mentions strategy, risks, objectives, expectations, outlook, or plans.
- Reporting conventions such as constant currency basis or non-GAAP definitions should be MOVE_TO_METADATA, not normal clean text.

Document metadata inferred from filename:
{document_metadata_json}

Return ONLY valid JSON:
{{
  "decisions": [
    {{
      "source_id": "string exactly as provided",
      "keep_review_decision": "CONFIRM_KEEP or MOVE_TO_METADATA or DROP_NOISE",
      "reason": "short reason",
      "fact_category": "metric | guidance_outlook | strategy | product_service | market_geography | leadership | operations | risk_macro | ESG | capital_allocation | customer_partner_channel | context_anchor | reporting_convention | metadata | speaker | logistics | boilerplate | greeting | other"
    }}
  ]
}}

Risky kept candidates with local context:
{input_json}
"""

AUDIT_PROMPT_TEMPLATE = """/no_think
You are auditing preprocessing decisions for a Temporal GraphRAG corpus.

This audit does NOT change the output. It only estimates whether final keep/drop decisions look correct.

For each target item, choose exactly one audit_label:
- CORRECT_KEEP: final decision kept the sentence and that seems correct.
- POSSIBLE_FALSE_KEEP: final decision kept the sentence but it may be noise or too vague for graph extraction.
- CORRECT_DROP: final decision dropped the sentence and that seems correct.
- POSSIBLE_FALSE_DROP: final decision dropped the sentence but it may contain useful evidence for graph extraction.

Use high recall for false-drop detection. Qualitative business facts count as useful evidence.

Return ONLY valid JSON:
{{
  "audit": [
    {{
      "source_id": "string exactly as provided",
      "audit_label": "CORRECT_KEEP or POSSIBLE_FALSE_KEEP or CORRECT_DROP or POSSIBLE_FALSE_DROP",
      "reason": "short reason"
    }}
  ]
}}

Audit items:
{input_json}
"""
