# Data

## Structure

- `raw/` — closest-to-source material. Includes `support_kb_sources.csv` (source metadata) and `source_snapshots/` (structured per-article summaries by company).
- `processed/` — derived datasets: benchmark questions, scoring results, AI answer reviews, and failure mode tallies.

## A note on source snapshots

This repo stores **structured summaries** of source articles, not full copied text. Each snapshot captures the relevant policy language in paraphrased form, plus the URL and the date accessed. This keeps the repo public-safe and focused on analysis.

See `raw/source_snapshots/<company>/` for examples.

## File-by-file

| File | Purpose |
|---|---|
| `raw/support_kb_sources.csv` | One row per source article with metadata |
| `raw/source_snapshots/<company>/*.md` | Structured per-article summaries |
| `processed/benchmark_questions.csv` | Customer questions used to probe each KB |
| `processed/evaluation_results.csv` | Human content audit scores per source |
| `ai_answer_reviews.csv` | Source-constrained AI answers per benchmark question, with manual review scores |
| `processed/failure_modes_summary.csv` | Tally of failure modes across the dataset |
