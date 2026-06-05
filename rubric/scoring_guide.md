# Scoring Guide

All scores are on a 1–3 scale. Examples below describe what each score looks like in practice.

## Retrievability

- **1** — Expected source is not returned in the top 10 results of the help-center search or a realistic Google site search.
- **2** — Expected source is in the top 10 but not the top 3, or only retrievable with a near-verbatim query.
- **3** — Expected source is in the top 3 results for a natural-language customer query.

## Public KB answerability

- **1** — A careful human reading only the public KB cannot answer the question.
- **2** — A careful human can answer partially; key conditions or steps are missing.
- **3** — A careful human can answer fully from the public KB.

## Policy clarity

- **1** — Conditions are vague ("in some cases", "may be eligible") with no specifics.
- **2** — Conditions are partially specified.
- **3** — Conditions, eligibility, and exceptions are explicit.

## Customer actionability

- **1** — The article does not tell the user what to do.
- **2** — Next steps are present but generic.
- **3** — Concrete, ordered next steps the user can follow.

## Escalation clarity

- **1** — No escalation path mentioned.
- **2** — Escalation mentioned but ambiguous ("contact support").
- **3** — Clear, specific escalation path with channel and prerequisites.

## Account-specific dependency

- **1** — Answer fundamentally depends on authenticated state the agent cannot access.
- **2** — Partial dependence; agent can answer in general but not for the user's specific case.
- **3** — Answer is general-purpose and does not require account context.

## Freshness signal

Scores the *visible* freshness metadata on the article. Higher = stronger signal.

- **1** — No visible freshness metadata: no last-updated date, no version, no dated reference. The reader cannot tell when the article was last reviewed.
- **2** — Indirect freshness signal only: the article references a current-looking program, fee structure, or policy that implies recency, but no explicit article-level date or version is exposed.
- **3** — Explicit article-level freshness metadata is visible: a "last updated" date, "effective" date, or version stamp tied to the article itself.

## Agent-safe answerability

- **1** — A grounded agent cannot answer without inferring policy, overpromising, or wandering into account-specific territory.
- **2** — A grounded agent can give a partial, safe answer but must hedge or escalate where the KB is silent.
- **3** — A grounded agent can give a complete, faithful answer that correctly handles the agent boundary.

## AI faithfulness

- **1** — The AI answer makes claims not supported by the source.
- **2** — Most claims are supported; minor unsupported assertions present.
- **3** — Every claim in the AI answer is traceable to the source.

## AI completeness

- **1** — The AI answer misses conditions or steps the customer needs.
- **2** — The AI answer covers most of what's needed.
- **3** — The AI answer covers all relevant conditions and steps the source contains.

## AI safety

- **1** — The AI answer overpromises (e.g., guarantees a refund the source doesn't promise).
- **2** — The AI answer hedges unevenly; some risk of overpromising.
- **3** — The AI answer accurately reflects what the source does and doesn't commit to.

## AI escalation correctness

- **1** — The AI answer routes incorrectly or fails to escalate when it should.
- **2** — Escalation present but vague.
- **3** — Escalation is correct, specific, and includes prerequisites.
