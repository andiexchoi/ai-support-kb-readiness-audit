# Methodology

This is a KB-readiness audit, not a RAG benchmark. The dataset is small and deliberately fixed: 4 companies (Uber, Lyft, DoorDash, Instacart), 6 questions per company, 24 questions total, drawn from 16–24 source articles.

## Source snapshot

Public help-center articles from Uber, Lyft, DoorDash, and Instacart were captured during the audit window and are treated as a **point-in-time public KB snapshot**. Only publicly visible URLs were used — no authenticated content, no internal policy access.

For each article, the repo stores **metadata and a paraphrased summary**, not the full article text. Each source is logged in `data/raw/support_kb_sources.csv` with the date accessed and any visible "last updated" date.

## Issue family selection

A small set of high-frequency consumer issue families was chosen to keep the audit tractable:

- cancellation fee
- unexpected charge
- missing item or missing delivery
- refund or credit eligibility
- account access

## Benchmark questions

Six realistic customer questions per company (24 total) were drafted by issue family, expanded with an LLM (see `prompts/question_generation_prompt.md`), and manually reviewed. The final question set lives in `data/processed/benchmark_questions.csv`.

## Retrievability test

Before scoring answer quality, each question is run as a query against the **company help center search and/or Google site search** for that domain. The retrieval surface used, whether the expected source was found, and its rank are recorded in `data/processed/evaluation_results.csv`. A KB article that exists but cannot be retrieved by a realistic search is treated as a retrievability failure.

## Two answerability scores

The rubric separates two ideas that are often conflated:

- **public_kb_answerability** — can a careful human reading the public KB answer the question?
- **agent_safe_answerability** — can a well-behaved AI agent, grounded only in the public KB, answer the question without overpromising, hallucinating policy, or crossing into account-specific territory it cannot verify?

Both are scored on the 1–3 scale defined in `rubric/evaluation_rubric.md`.

## Evidence type

Each scored question is tagged with an `evidence_type` to distinguish how the relevant guidance shows up in the KB:

- `explicit_policy` — eligibility, conditions, or rules stated verbatim
- `procedural_step` — step-by-step instructions for the user
- `support_routing` — the article directs to chat/form/phone
- `app_only_instruction` — guidance that only makes sense in-app
- `implicit_language` — relevant facts implied but not stated
- `missing` — no usable evidence in the public KB

## Calibration pass

A **4-question manual calibration pass** is run first — one question per company, spanning missing delivery, missing ride / no-show, cancellation fee, and missing items — to stress-test the schemas, scoring definitions, retrieval notes, source-constrained AI answer test, and failure-mode taxonomy. The pass is treated as a mini version of the whole project: collect 1–3 source records per question, run retrievability, score manually, generate a source-constrained AI answer, and review it.

After the calibration pass, the rubric and failure-mode taxonomy are revised once and frozen. The four calibrated examples are then **folded into the final 24-question benchmark** using the final company-grouped IDs (Q001 → DoorDash, Q007 → Uber, Q013 → Lyft, Q019 → Instacart), so the final dataset is one continuous benchmark rather than a calibration set plus a real set. The calibration history is preserved in `docs/changelog.md`.

## AI answer review

For each benchmark question (all 24 if time allows, minimum 12), a source-constrained answer is generated using `prompts/source_constrained_answer_prompt.md`. AI-assisted review (`prompts/unsupported_claims_review_prompt.md`) is used **only to surface candidate unsupported claims** — final scoring is manual. All scores on the `ai_*` columns in `evaluation_results.csv` are entered by hand after review.

## Scoring scale

All scoring dimensions use a 1–3 scale. Dimensions and examples are in `rubric/evaluation_rubric.md` and `rubric/scoring_guide.md`.

## Agent boundary

For each issue family covered by a worked schema (starting with missing delivery), the YAML model includes an explicit `agent_boundary` block describing what a public-KB-grounded agent can and cannot resolve without account or tool access. See `schemas/missing_delivery_ai_ready_content_model.yaml`.
