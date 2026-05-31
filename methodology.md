# Methodology

## Source snapshot

Public help-center articles from Uber, Lyft, DoorDash, and Instacart were captured during the audit window. Only publicly visible URLs were used. No authenticated content, no internal policy access. Each source was logged in `data/raw/support_kb_sources.csv` with the date accessed and any visible "last updated" date.

## Issue family selection

A small set of high-frequency consumer issue families was chosen to keep the audit tractable:

- cancellation fee
- unexpected charge
- missing item or missing delivery
- refund or credit eligibility
- account access

## Benchmark questions

Realistic customer questions were drafted per issue family, then expanded with an LLM (see `prompts/question_generation_prompt.md`) and manually reviewed. Final question set lives in `data/processed/benchmark_questions.csv`.

## Scoring rubric

Each source was scored on the dimensions defined in `rubric/evaluation_rubric.md`. Scoring examples (what a 1, 2, or 3 looks like) are in `rubric/scoring_guide.md`.

## AI answer review

For each benchmark question, a source-constrained answer was generated using `prompts/source_constrained_answer_prompt.md`, then manually reviewed for unsupported claims using `prompts/unsupported_claims_review_prompt.md`. Reviews are in `data/processed/ai_answer_reviews.csv`.

All AI outputs were manually reviewed before being recorded.
