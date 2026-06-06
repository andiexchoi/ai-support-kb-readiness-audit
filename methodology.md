# Methodology

This is a KB-readiness audit, not a RAG benchmark. The dataset is small and deliberately fixed: 4 companies (Uber, Lyft, DoorDash, Instacart), 6 questions per company, 24 questions total, drawn from 16–24 source articles.

## Methodology thesis

This project is a public-layer audit of marketplace support knowledge. It evaluates whether the public-facing support documentation for Uber, Lyft, DoorDash, and Instacart is structured clearly enough to help an AI support agent answer, route, or escalate customer issues safely.

The project does not claim to evaluate each company's full internal support system, production chatbot, internal agent macros, refund decisioning, account-specific workflows, or private policy logic. Instead, it treats public support documentation as the observable customer-facing layer of a broader support knowledge system.

## Public documentation as observable support knowledge

This project uses public support documentation as the observable layer of each company's support knowledge system. In practice, marketplace support agents likely rely on internal policies, macros, account data, and app-based workflows that are not publicly accessible. I do not claim to evaluate those internal systems. Instead, I audit the public-facing layer to assess whether it provides clear, retrievable, policy-safe guidance that could ground customer-facing AI support answers or indicate when an issue must be routed to an authenticated app flow or human/account-specific review.

Because these services are app-mediated, many customer issues are not fully resolved through public articles alone. A public article may explain the policy, describe the in-app reporting path, or route the customer to support, while the actual outcome may depend on order, trip, payment, account, or fraud-review data. For that reason, I score not only whether the public source answers the question, but whether it makes the boundary between public guidance, app workflow, and account-specific review clear.

## Benchmark question design

Six realistic customer questions per company (24 total) were drafted by issue family, expanded with an LLM (see `prompts/question_generation_prompt.md`), and manually reviewed. The final question set lives in `data/processed/benchmark_questions.csv`.

I selected benchmark questions by combining visible public-support navigation signals, such as popular articles and top-level help categories, with high-risk customer complaint patterns found in public reporting and community discussions. I did not claim these questions represent internal ticket volume. Instead, I treated them as realistic, high-frequency, high-risk support scenarios that public KBs should be able to answer or safely route.

Benchmark questions were written in natural customer language rather than help-center article-title language. I intentionally avoided matching the exact wording of support article titles where possible, because one goal of the audit was to test whether public support search systems could map realistic customer phrasing to the correct source. When natural-language searches failed, I recorded whether a keyword reformulation retrieved the expected source.

### Issue family selection

A small set of high-frequency consumer issue families was chosen to keep the audit tractable:

- cancellation fee
- unexpected charge
- missing item or missing delivery
- refund or credit eligibility
- account access

## Source snapshot

Public help-center articles from Uber, Lyft, DoorDash, and Instacart were captured during the audit window and are treated as a **point-in-time public KB snapshot**. Only publicly visible URLs were used — no authenticated content, no internal policy access.

For each article, the repo stores **metadata and a paraphrased summary**, not the full article text. Each source is logged in `data/raw/support_kb_sources.csv` with the date accessed and any visible "last updated" date.

## Evaluation criteria

### AI-agent evaluation lens

For each benchmark question, I evaluate whether the public support source helps an AI agent determine:

- whether the question can be answered from public documentation alone
- whether the user must be routed to an authenticated app flow
- whether the issue requires order-, trip-, payment-, or account-specific review
- whether refund, credit, fee-waiver, or redelivery outcomes are stated as explicit rules or only possible outcomes
- whether the source gives a safe customer-facing next step
- whether the source provides enough information for an AI answer to avoid unsupported promises
- whether escalation conditions are clear enough for an AI agent to route correctly

This means a public article does not need to fully resolve every issue to score well. For app-mediated support flows, a strong source may instead clearly explain what the customer can do, what the company may review, what outcomes are not guaranteed, and where the AI agent must stop answering and route to a workflow or human review.

### Retrievability test

Before scoring answer quality, each question is run as a query against the **company help center search and/or Google site search** for that domain. The retrieval surface used, whether the expected source was found, and its rank are recorded in `data/processed/evaluation_results.csv`. A KB article that exists but cannot be retrieved by a realistic search is treated as a retrievability failure.

### Two answerability scores

The rubric separates two ideas that are often conflated:

- **public_kb_answerability** — can a careful human reading the public KB answer the question?
- **agent_safe_answerability** — can a well-behaved AI agent, grounded only in the public KB, answer the question without overpromising, hallucinating policy, or crossing into account-specific territory it cannot verify?

Both are scored on the 1–3 scale defined in `rubric/evaluation_rubric.md`.

### Evidence type

Each scored question is tagged with an `evidence_type` to distinguish how the relevant guidance shows up in the KB:

- `explicit_policy` — eligibility, conditions, or rules stated verbatim
- `procedural_step` — step-by-step instructions for the user
- `support_routing` — the article directs to chat/form/phone
- `app_only_instruction` — guidance that only makes sense in-app
- `implicit_language` — relevant facts implied but not stated
- `missing` — no usable evidence in the public KB

### Scoring scale

All scoring dimensions use a 1–3 scale. Dimensions and examples are in `rubric/evaluation_rubric.md` and `rubric/scoring_guide.md`.

## Calibration pass

A **4-question manual calibration pass** is run first — one question per company, spanning missing delivery, missing ride / no-show, cancellation fee, and missing items — to stress-test the schemas, scoring definitions, retrieval notes, source-constrained AI answer test, and failure-mode taxonomy. The pass is treated as a mini version of the whole project: collect 1–3 source records per question, run retrievability, score manually, generate a source-constrained AI answer, and review it.

After the calibration pass, the rubric and failure-mode taxonomy are revised once and frozen. The four calibrated examples are then **folded into the final 24-question benchmark** using the final company-grouped IDs (Q001 → DoorDash, Q007 → Uber, Q013 → Lyft, Q019 → Instacart), so the final dataset is one continuous benchmark rather than a calibration set plus a real set. The calibration history is preserved in `docs/changelog.md`.

## AI answer review

For each benchmark question (all 24 if time allows, minimum 12), a source-constrained answer is generated using `prompts/source_constrained_answer_prompt.md`. AI-assisted review (`prompts/unsupported_claims_review_prompt.md`) is used **only to surface candidate unsupported claims** — final scoring is manual. All scores on the `ai_*` columns in `evaluation_results.csv` are entered by hand after review.

## Agent boundary

For each issue family covered by a worked schema (starting with missing delivery), the YAML model includes an explicit `agent_boundary` block describing what a public-KB-grounded agent can and cannot resolve without account or tool access. See `schemas/missing_delivery_ai_ready_content_model.yaml`.
