# Are Public Support Knowledge Bases Ready for AI Agents?

An audit of public support knowledge bases from Uber, Lyft, DoorDash, and Instacart, scored against an "agent-safe answerability" rubric.

## What this project is

A small research artifact that asks: if you handed today's customer support knowledge bases to an AI agent, would it be able to answer real customer questions accurately, with grounded sources, and without overpromising?

## Why it matters

AI support agents are only as good as the knowledge they retrieve. Most public KBs were written for humans who can tolerate ambiguity, follow links, and infer escalation. AI agents cannot. This audit looks at where current docs hold up, where they break, and what an AI-ready content model could look like.

## What's in the repo

- `methodology.md` — how the audit was run
- `related_work.md` — WixQA, RAGAS, Amazon agent eval in plain English
- `limitations.md` — what this is and isn't
- `data/` — source snapshots, benchmark questions, scores
- `rubric/` — scoring dimensions and examples
- `prompts/` — exact prompts used with AI, plus review prompts
- `schemas/` — proposed AI-ready content model and reusable template
- `analysis/` — score breakdowns and patterns
- `visuals/` — charts
- `writeup/` — final essay
- `docs/` — plan, changelog, glossary

## How to read the results

1. Start with `writeup/index.md` for the narrative.
2. Read `methodology.md` to see how scoring worked.
3. Inspect `data/processed/evaluation_results.csv` to see the raw scores.
4. Look at `schemas/missing_delivery_ai_ready_content_model.yaml` for the proposed model.

## License

See `LICENSE`.
