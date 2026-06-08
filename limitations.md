# Limitations

- **KB-readiness audit, not a RAG benchmark.** This project evaluates whether public docs are ready to back an AI agent — not the performance of any specific retrieval or generation pipeline.
- **Public documentation only.** The audit scores publicly visible help-center articles. It has no access to internal policy, agent macros, routing logic, internal tools, account-state systems, or proprietary playbooks. Real support agents may have better information than what is publicly visible.
- **Point-in-time snapshot.** KBs change frequently. Findings reflect the source state on the dates listed in `data/raw/support_kb_sources.csv` (primarily 2026-06-01). Any rule, rate, or routing path may have changed since.
- **English-only.** Localized content was not evaluated. Findings may not generalize to non-English versions of the same KBs.
- **One-rater scoring.** All rubric scoring was performed by a single rater. Scores are auditable but subjective, and inter-rater reliability is not measured.
- **No internal policy or tool access.** The audit cannot verify whether the captured public language matches internal policy. Where a public article does not state a rule, the audit treats it as not publicly stated — it does not infer the underlying internal policy.
- **No production-agent benchmark.** This project does not evaluate any deployed AI support agent. It scores the readiness of the underlying knowledge, not the behavior of any specific product.
- **Schemas are proposed content models, not claims about internal policy.** The YAML schemas in `schemas/` separate source-backed `policy_observations` (paraphrased from captured public articles) from `proposed_required_metadata` (placeholder fields a KB owner would need to populate). Nothing in the `proposed_required_metadata` blocks should be read as a description of current company policy.
- **Small, fixed sample.** 4 companies × 6 questions = 24 questions, drawn from 30 articles. Findings are directional, not statistically representative.
- **Paraphrased summaries, not full articles.** The repo stores metadata and short summaries of public articles, not the article text. This keeps the project public-safe and treats the dataset as a point-in-time snapshot.
- **Retrievability is tested, not modeled.** Retrieval scores reflect what each company help-center search and Google site search returned on the date of access, not a custom retriever.
- **Public KB answerability vs agent-safe answerability are scored separately.** A question can be answerable in principle but not safely answerable by a grounded agent (and vice versa).
- **No account-specific workflows.** Many real resolutions depend on authenticated state (order ID, account tier, region). The `agent_boundary` block captures this; the audit can flag account-dependence but not test it.
- **AI-assisted, manually scored.** AI is used to surface candidate unsupported claims. Final scoring is manual.
- **Exploratory audit.** Portfolio-grade artifact, not a peer-reviewed study. The scoring rubric is auditable but subjective.
