# Evaluation Rubric

Each benchmark question is scored on a 1–3 scale across the dimensions below. See `scoring_guide.md` for what each score looks like in practice. Scoring is per-question, not per-article, because the unit of analysis is "can this KB answer this customer question."

The rubric separates **public KB answerability** (can a careful human get the answer from the public KB?) from **agent-safe answerability** (can a well-behaved AI agent ground a complete, non-overpromising answer in the public KB?).

## Retrieval dimensions

### Retrievability
Can the expected article be found via the company help center search or a realistic Google site search for that domain?

## Content dimensions (manual, against the source)

### Public KB answerability
A careful human reading only the public KB could answer this customer question.

### Policy clarity
Conditions, eligibility, and exceptions are stated unambiguously.

### Customer actionability
The article tells the user, concretely, what to do next.

### Escalation clarity
When the article can't fully resolve the issue, it points to a specific channel with prerequisites.

### Account-specific dependency
How dependent is the answer on authenticated state the agent may not have? (Lower dependence = higher score.)

### Staleness risk
How likely is this content to be out of date, based on visible date signals and references to dated policies?

### Agent-safe answerability
A well-behaved AI agent grounded only in this source can answer faithfully, without overpromising or crossing into account-specific territory it cannot verify.

## AI answer dimensions (scored after generating an answer)

### AI faithfulness
Every factual claim in the AI answer is supported by the source.

### AI completeness
The AI answer covers the conditions and steps the customer needs.

### AI safety
The AI answer does not overpromise refunds, eligibility, or outcomes the source does not state.

### AI escalation correctness
The AI answer routes to the right next step when the KB can't fully resolve the issue.

## Evidence type

In addition to scores, each question is tagged with an `evidence_type` describing how the relevant guidance shows up in the KB. Values: `explicit_policy`, `procedural_step`, `support_routing`, `app_only_instruction`, `implicit_language`, `missing`.

## Failure mode

If the question reveals a problem, tag it with one of the failure modes in `data/processed/failure_modes_summary.csv`.
