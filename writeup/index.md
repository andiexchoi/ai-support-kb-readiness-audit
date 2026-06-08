# Are Public Support Knowledge Bases Ready for AI Agents?

## Summary

This audit scored the public help-center content of four major consumer platforms — DoorDash, Uber, Lyft, and Instacart — against a 24-question benchmark covering the highest-volume rider and customer support intents (missing deliveries, refunds, cancellation fees, duplicate charges, escalation). Each question was scored on a six-dimension rubric (answerability, faithfulness support, policy clarity, freshness signal, escalation clarity, account dependency), and the source-constrained AI answer was reviewed for unsupported claims. The headline finding: the dominant failure is **retrieval, not content**. Two-thirds of evaluated rows fall into `hard_to_retrieve` (41.7%) or `query_phrasing_sensitivity` (25%) — the article exists, is correct, and is agent-safe, but the internal help-center search will not surface it from natural customer wording. Where AI overpromising shows up, it is almost always in **off-source** synthesis (external search blending Reddit, JustAnswer, Quora) rather than in answers grounded in the captured KB.

## Why this matters

AI support agents are being deployed against the same knowledge bases that humans have used for years. But humans can tolerate ambiguity. Agents can't — they either guess (and overpromise) or refuse (and frustrate). This audit asks how ready four major consumer support KBs are to back an AI agent.

## Related work

WixQA, ARES, Doc2Dial/MultiDoc2Dial, and Amazon's public writeups on agent evaluation. See [`../related_work.md`](../related_work.md).

## Methodology

Source snapshot of public help-center articles from Uber, Lyft, DoorDash, and Instacart accessed 2026-06-01. A 24-question benchmark covering 13 issue families. Scoring rubric across six dimensions (1–3 scale): answerability, faithfulness support, policy clarity, freshness signal, escalation clarity, account dependency. Source-constrained AI answers generated against the captured snapshot only, then reviewed for unsupported claims. External search behavior (Google AI Overview) captured during retrieval as a comparison signal. See [`../methodology.md`](../methodology.md).

## Dataset

- **N sources:** 30 public help-center articles
- **N benchmark questions:** 24
- **N issue families:** 13 (missing delivery, missing items, wrong/incomplete order, cancellation fee, cancellation/refund, duplicate or unexpected charge, pending charge, refund status, lost item, missing service / trip not taken, support escalation, membership/subscription charge, wrong or problematic service)
- **Companies:** DoorDash, Uber, Lyft, Instacart
- **Date of source access:** 2026-06-01

## Findings

### 1. The dominant failure is retrieval, not content

`hard_to_retrieve` (10/24 rows, 41.7%) and `query_phrasing_sensitivity` (6/24 rows, 25%) together account for two-thirds of evaluated rows. In nearly every case the correct, agent-safe article was in the public KB — the internal help-center search just did not return it for natural customer wording. Reformulating to a keyword query ("missing item", "refund", "wrong item") frequently surfaced the right article, and Google returned the same article on the first try.

A representative pattern: on Q024 ("I got charged for Instacart+ and I don't want it") the Instacart Help search silently normalized "Instacart+" to "instacart" and returned promotional pages instead of the cancellation article. The cancellation article itself (IC-006) was strong; the search surface stripped the intent out of the query before reaching it.

### 2. The lowest-scoring issue families are charge-shape edge cases, not core flows

The two lowest-scoring families (`duplicate_or_unexpected_charge` and `wrong_or_problematic_service`, both 1.8 avg_total) follow the same pattern: the user's described scenario doesn't map cleanly onto a captured KB article, and the closest article covers an adjacent but distinct policy. DoorDash's "I accidentally placed a duplicate order" article is the nearest match for "DoorDash charged me twice for the same order" but it actually covers two separately-placed orders, not a true duplicate charge. Uber's pricing articles explain why upfront prices can change but do not give a dispute path for "the driver took a weird route." In both cases the safe answer is to route to support — which is not a wrong answer, but it is a thinner one than the user asked for.

`refund_status` (2.2 avg) is the next-weakest family and is where AI overpromising is most likely.

### 3. AI overpromising lives off-source, not on-source

Every source-constrained AI answer in this audit scored 3 on faithfulness. The unsupported-claims risk surfaced in **external** search behavior: Google AI Overview captured during retrieval frequently blended non-official sources (Reddit, JustAnswer, Quora, Facebook, GetHuman) into answers and added:

- **Refund-timing certainty** the captured sources do not commit to ("2–7 business days", "5–10 business days" applied as universal windows) — surfaced on Q011, Q017, Q022, Q023.
- **Fare-adjustment promises** ("you can easily get a fare adjustment", "Uber will typically adjust the fare") — Q008 and Q015.
- **Recovery-action invention** (check the delivery photo, contact the shopper within a 20-minute window) — Q001 and Q021.
- **Cross-issue contamination** (Q003 returned a missing-items refund answer for a cancellation question).

The implication is direct: source-constrained generation against a curated KB is the safe path. Letting an agent fall back to open-web synthesis is where overpromising is introduced.

## Example evaluations

**Where the KB held up — Q009 (Uber cancellation fee, late driver).** The cancellation-fee article (UB-002) ranked first for the natural-language query, gave specific per-product timing thresholds (Shared/UberX 2 min, Premium 5 min), and explicitly stated no-fee exceptions (driver hadn't made progress to pickup, driver 5+ minutes late). It distinguished cancellation fees from temporary authorization holds and provided a review form for disputed fees. Both retrieval and content worked — this row carried no failure-mode tag.

**Where it broke — Q004 (DoorDash, "charged me twice").** Internal search returned no results for "charged twice." The closest official article (DD-005, "I accidentally placed a duplicate order") addresses two separately-placed orders, not a true duplicate charge for one order. The captured public KB does not distinguish a pending duplicate authorization hold from a posted duplicate charge. Public-KB answerability scored 1 — the lowest in the audit — and the agent-safe answer was forced to route to support.

**Where the AI overpromised (off-source) — Q011 (Uber, "when will my refund hit my card").** The captured Uber sources are honest about not publishing a universal refund timeline: UB-007 is a logged-in trip-specific flow and UB-008 covers authorization holds only. The source-constrained AI answer correctly stayed inside that language. Google AI Overview, captured during retrieval, added "2 to 7 business days" and "up to 30 days" citing Reddit and third-party sources — numbers the official Uber pages do not commit to.

## AI-ready content model

The two failure modes that dominate this audit — retrieval failure and missing policy conditions — suggest a small set of structured fields that would lift agent-readiness without rewriting the underlying help articles. Two worked examples are checked in for the highest-severity issue families:

- [`../schemas/missing_delivery_ai_ready_content_model.yaml`](../schemas/missing_delivery_ai_ready_content_model.yaml) — grounded in DD-001 (DoorDash) and IC-002 / IC-003 (Instacart).
- [`../schemas/cancellation_fee_ai_ready_content_model.yaml`](../schemas/cancellation_fee_ai_ready_content_model.yaml) — grounded in UB-002 (Uber) and LY-002 (Lyft).

Both schemas separate two layers explicitly:

1. **Source-backed `policy_observations`.** Each company's section lists only what the captured public article actually states, paired with an explicit `does_not_state` list (e.g., "no guaranteed refund," "no published response timing"). This is the layer an agent can quote from.
2. **`proposed_required_metadata`.** Placeholders (`<TBD by KB owner>`) for the structured fields a KB owner would need to add to make the article reliably agent-answerable — eligibility conditions, response windows, freshness dates, dispute SLAs. These are explicitly *not* claims about current policy; they are the contract a KB owner would have to sign before an agent could resolve cases unconditionally.

The schemas also encode the two retrieval-era risks the audit surfaced. Each one carries a `retrievability_observations` block (what the company's internal search did with the natural-language query) and an `external_search_behavior_caveats` block (specific unsupported claims that off-source AI overlays added during retrieval, logged so an agent constrained to the schema knows what to filter out). The `agent_boundary` block decomposes "can the agent answer?" into per-capability booleans — public-KB guidance is fair game; refund amounts, refund timing, and eligibility decisions are not. A short `do_not_say` list captures the specific phrasings (refund guarantees, invented business-day windows, off-source recovery steps) that an agent grounded in this schema must avoid even when external search produces them fluently.

## Recommendations

**For KB owners:**

- Expose a visible last-updated date on every help article. Every company in this audit scored 1 on freshness signal because no such date was observed on any captured article.
- Treat your internal help-center search as the primary failure surface. Most of the content in this audit was good; the retrieval layer in front of it was not. Semantic search, query expansion, or letting an LLM rewrite the query before searching would lift scores across two-thirds of this benchmark with no content change.
- Author for the edge cases users actually hit. Duplicate-charge vs. authorization hold, dispute-refund timing, and "the driver took a weird route" are concrete intents that currently have no clean public article.

**For agent builders:**

- Constrain generation to the curated KB snapshot. Every source-constrained answer in this audit scored 3 on faithfulness. The overpromising lived in the external-search fallback.
- Refund timing is where agents hallucinate. If your KB does not publish a numeric window, do not let the agent infer one — route to "check status in the app" plus the official escalation path.
- Build a routing step before the answering step for multi-branch questions (unrecognized charges, trip-not-taken charges). The user's question often legitimately maps to two or three different policies.

**For platform teams:**

- Treat retrieval quality and content quality as separate dashboards. They fail differently and they are owned by different teams.
- Capture the gap between "what the user asked" and "what the search surface matched" as a first-class signal. The Instacart+ → instacart normalization on Q024 is the kind of bug that only shows up if you instrument it.

## Limitations

See [`../limitations.md`](../limitations.md).

## Next steps

- Finalize the AI-ready content model schemas for the highest-severity issue families (missing delivery, cancellation fee) and validate each field against the captured source set.
- Re-run the benchmark against an LLM-mediated retrieval layer (semantic search or query rewriting) to quantify how much of the retrieval failure is recoverable without KB changes.
- Expand the benchmark beyond rideshare and delivery into adjacent verticals (financial services, telecom) where the regulatory cost of agent overpromising is higher.
