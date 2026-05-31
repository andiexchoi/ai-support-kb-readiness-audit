# Scoring Guide

Examples of what each score looks like in practice, per dimension.

## Agent-safe answerability

- **1** — Article is tangential. An agent grounded only in this source would have to guess.
- **2** — Article covers the topic but omits at least one condition the answer depends on.
- **3** — Article fully covers the question with explicit conditions and resolution steps.

## Faithfulness support

- **1** — Key policy facts are implied, not stated. Any answer would require inference.
- **2** — Most facts are stated; some require minor inference.
- **3** — All policy-relevant claims appear verbatim in the source.

## Policy clarity

- **1** — Conditions are vague ("in some cases", "may be eligible") without specifying which.
- **2** — Conditions are partially specified.
- **3** — Conditions, eligibility, and exceptions are explicit.

## Freshness signal

- **1** — No visible last-updated date or version indicator.
- **2** — Indirect freshness signal (e.g., article references a recent event).
- **3** — Explicit "last updated" date or version visible.

## Escalation clarity

- **1** — No escalation path mentioned.
- **2** — Escalation mentioned but ambiguous ("contact support").
- **3** — Clear, specific escalation path with channel and prerequisites.

## Account-specific dependency

- **1** — Answer fundamentally depends on authenticated state the agent cannot access.
- **2** — Partial dependence; agent can answer in general but not for the user's specific case.
- **3** — Answer is general-purpose and does not require account context.
