# Project Plan

## Goal

Produce a credible, public-safe audit of whether four major consumer support KBs are ready to back an AI agent — and propose a content model that would make them ready.

## Phases

### 1. Scope and rubric
- Pick issue families
- Draft rubric (`rubric/evaluation_rubric.md`)
- Draft scoring examples (`rubric/scoring_guide.md`)

### 2. Source snapshot
- Collect public help-center articles
- Record metadata in `data/raw/support_kb_sources.csv`
- Write structured summaries in `data/raw/source_snapshots/`

### 3. Benchmark questions
- Draft questions per issue family
- Expand via LLM (`prompts/question_generation_prompt.md`)
- Manually review
- Save to `data/processed/benchmark_questions.csv`

### 4. Human content audit
- Score each source against the rubric
- Fill in `data/processed/evaluation_results.csv`

### 5. AI answer review
- Generate source-constrained answers (`prompts/source_constrained_answer_prompt.md`)
- Review for unsupported claims (`prompts/unsupported_claims_review_prompt.md`)
- Fill in `data/processed/ai_answer_reviews.csv`

### 6. Analysis
- Roll up to company, issue family, failure mode
- Write `analysis/score_analysis.md`
- Produce visuals

### 7. Schema
- Complete `schemas/missing_delivery_ai_ready_content_model.yaml`
- Generalize into `schemas/support_issue_schema_template.yaml`

### 8. Write-up
- Draft `writeup/index.md`
- Embed figures
