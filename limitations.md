# Limitations

- **KB-readiness audit, not a RAG benchmark.** This project evaluates whether public docs are ready to back an AI agent — not the performance of any specific retrieval or generation pipeline.
- **Public docs only.** No access to internal policy, agent macros, or routing logic. Real support agents may have better information than what is publicly visible.
- **Small, fixed sample.** 4 companies × 6 questions = 24 questions, drawn from 16–24 articles. Findings are directional, not statistically representative.
- **Paraphrased summaries, not full articles.** The repo stores metadata and short summaries of public articles, not the article text. This keeps the project public-safe and treats the dataset as a point-in-time snapshot.
- **Retrievability is tested, not modeled.** Retrieval scores reflect what the company help-center search and Google site search return today, not a custom retriever.
- **Public KB answerability vs agent-safe answerability are scored separately.** A question can be answerable in principle but not safely answerable by a grounded agent (and vice versa).
- **No account-specific workflows.** Many real resolutions depend on authenticated state (order ID, account tier, region). The `agent_boundary` block captures this; the audit can flag account-dependence but not test it.
- **Snapshot in time.** KBs change frequently. Findings reflect the source state on the dates listed in `data/raw/support_kb_sources.csv`.
- **AI-assisted, manually scored.** AI is used to surface candidate unsupported claims. Final scoring is manual.
- **Exploratory audit.** Portfolio-grade artifact, not a peer-reviewed study. The scoring rubric is auditable but subjective.
- **English-only.** Localized content was not evaluated.
