# Question Generation Prompt

Used to draft realistic customer questions per issue family. All outputs were manually reviewed for plausibility before inclusion in the benchmark.

---

You are helping build a benchmark of realistic customer support questions for an AI-readiness audit of public knowledge bases.

For the issue family below, draft {{n}} questions that a real customer might ask. Vary:
- Level of detail (short vs. multi-sentence)
- Emotional tone (neutral, frustrated, urgent)
- Specificity (general policy question vs. specific incident)
- Account-state dependence (some questions should require account context, others should not)

Issue family: {{issue_family}}
Company context: {{company}}

For each question, also output:
- `realism_notes`: why a real customer might ask this
- `account_dependent`: yes/no
- `expected_difficulty`: easy / medium / hard for an AI grounded only in public docs

Format as CSV-ready rows.
