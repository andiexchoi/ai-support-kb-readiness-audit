# Project Plan

## Goal

Produce a credible, public-safe **KB-readiness audit** of four major consumer support knowledge bases — and propose a content model that would make them ready for an AI agent. Portfolio framing: technical writer → AI knowledge architect.

## Locked scope

- 4 companies: Uber, Lyft, DoorDash, Instacart
- 6 questions per company; 24 total
- 16–24 source articles
- 1–3 scoring scale
- AI answer test: all 24 if possible, minimum 12
- Deliverables: write-up, three CSVs, rubric, one AI-ready schema

## Phases

### 1. Scope and rubric
- Lock issue families and the 1–3 rubric
- Draft `rubric/evaluation_rubric.md` and `rubric/scoring_guide.md`

### 2. Source snapshot
- Collect public help-center articles (treat as point-in-time public KB)
- Record metadata and **paraphrased summaries only** in `data/raw/support_kb_sources.csv`
- Tag each source with `evidence_type`

### 3. Benchmark questions
- Draft 6 questions per company by issue family
- Expand via LLM (`prompts/question_generation_prompt.md`)
- Manually review
- Save to `data/processed/benchmark_questions.csv`

### 4. Calibration pass
- Manually score 4 questions (one per company) end-to-end
- Adjust rubric / scoring guide if any dimension feels inconsistent
- Only then proceed to scoring the rest

### 5. Retrievability test
- For each question, run a realistic query against the help-center search and/or Google site search
- Record `search_surface`, `found_expected_source`, `rank_if_found`, `retrievability_score`

### 6. Manual content scoring
- Score each question against the rubric, including the split between `public_kb_answerability_score` and `agent_safe_answerability_score`
- Fill `data/processed/evaluation_results.csv`

### 7. AI answer review
- Generate source-constrained answers (`prompts/source_constrained_answer_prompt.md`)
- Use AI-assisted review only to surface candidate unsupported claims
- Manually score `ai_faithfulness_score`, `ai_completeness_score`, `ai_safety_score`, `ai_escalation_correctness_score`

### 8. Analysis
- Roll up to company, issue family, failure mode
- Write `analysis/score_analysis.md`
- Produce 4–6 findings and visuals

### 9. Schema
- Complete `schemas/missing_delivery_ai_ready_content_model.yaml` (includes `agent_boundary`)
- Generalize into `schemas/support_issue_schema_template.yaml`

### 10. Write-up
- Draft `writeup/index.md`
- Embed figures and link to data
