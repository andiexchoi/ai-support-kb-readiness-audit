# Are Public Support Knowledge Bases Ready for AI Agents?

A KB-readiness audit of public support knowledge bases from Uber, Lyft, DoorDash, and Instacart, scored against an "agent-safe answerability" rubric.

This is a portfolio piece tracing a path from **technical writer to AI knowledge architect**: not "how good is RAG?" but "is this content ready to be retrieved, grounded, and acted on by an AI agent — and if not, what would it take to get it there?"

## What this project is

A KB-readiness audit, not a RAG benchmark. The question is: if you handed today's public customer support knowledge bases to an AI agent, would they support accurate, grounded, escalation-aware answers — or do the docs themselves need to change?

## Scope (locked)

- **4 companies:** Uber, Lyft, DoorDash, Instacart
- **24 benchmark questions:** 6 per company
- **16–24 source articles**
- **AI answer test:** all 24 questions if time allows; minimum 12
- **Scoring scale:** 1–3 across all dimensions
- **Core deliverables:** final write-up, three CSVs, rubric, one AI-ready content schema

## Why it matters

AI support agents are only as good as the knowledge they retrieve. Most public KBs were written for humans who can tolerate ambiguity, follow links across pages, and infer escalation. AI agents cannot. This audit separates **public KB answerability** (can a careful human get the answer?) from **agent-safe answerability** (can a grounded agent give a complete, non-overpromising answer?), and proposes a content model that makes the second possible.

## What's in the repo

- [`methodology.md`](methodology.md) — how the audit was run
- [`related_work.md`](related_work.md) — WixQA, ARES, Doc2Dial/MultiDoc2Dial, Amazon agent eval in plain English
- [`limitations.md`](limitations.md) — what this is and isn't
- [`writeup/index.md`](writeup/index.md) — final public-facing essay
- [`analysis/score_analysis.md`](analysis/score_analysis.md) — detailed evidence-oriented score analysis
- [`data/processed/evaluation_results.csv`](data/processed/evaluation_results.csv) — per-question scores across all rubric dimensions
- [`data/ai_answer_reviews.csv`](data/ai_answer_reviews.csv) — source-constrained AI answers and unsupported-claims reviews
- [`schemas/missing_delivery_ai_ready_content_model.yaml`](schemas/missing_delivery_ai_ready_content_model.yaml) — worked AI-ready content model for the missing-delivery issue family
- [`schemas/cancellation_fee_ai_ready_content_model.yaml`](schemas/cancellation_fee_ai_ready_content_model.yaml) — worked AI-ready content model for the cancellation-fee issue family
- `data/` — source metadata, paraphrased summaries, benchmark questions, scores
- `rubric/` — scoring dimensions and examples (1–3 scale)
- `prompts/` — exact prompts used with AI, plus review prompts
- `schemas/` — proposed AI-ready content models (with `agent_boundary`) and reusable template
- `analysis/` — score breakdowns and patterns
- `visuals/` — charts
- `writeup/` — final essay
- `docs/` — plan, changelog, glossary

## How to read the results

1. Start with `writeup/index.md` for the narrative.
2. Read `methodology.md` to see how scoring worked.
3. Inspect `data/processed/evaluation_results.csv` for raw scores.
4. Look at `schemas/missing_delivery_ai_ready_content_model.yaml` for the proposed model and its `agent_boundary` block.

## Minimum publishable version

Done means:

- 16–24 source records completed
- 24 benchmark questions completed
- all 24 questions manually scored
- AI answer review completed for at least 12 questions
- one AI-ready schema completed
- 4–6 findings written
- final write-up published

## License

See `LICENSE`.
