# Evaluation Rubric

Each source article is scored on six dimensions on a 1–3 scale. See `scoring_guide.md` for examples.

## Dimensions

### 1. Agent-safe answerability
Can a well-behaved agent give a complete, grounded answer to the target question using only this source?

### 2. Faithfulness support
Does the source contain enough explicit policy language to support a faithful answer without inference?

### 3. Policy clarity
Are conditions, eligibility criteria, and exceptions stated unambiguously?

### 4. Freshness signal
Does the article expose a "last updated" date or other freshness signal an agent could use to assess staleness?

### 5. Escalation clarity
When the article cannot resolve the issue, does it clearly direct the user to the next step (chat, form, phone)?

### 6. Account-specific dependency
How dependent is the answer on authenticated state the agent may not have? (Lower dependence = higher score.)

## Total

Sum of the six dimensions, max 18.
