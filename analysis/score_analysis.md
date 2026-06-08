# Score Analysis

Evidence-oriented synthesis of the 24-question benchmark across DoorDash, Uber, Lyft, and Instacart. All numbers below come from `data/processed/evaluation_results.csv` and the three summary CSVs in this directory.

## Headline findings

- **Retrieval, not content, is the dominant failure.** `hard_to_retrieve` (10/24, 41.7%) and `query_phrasing_sensitivity` (6/24, 25%) together account for two-thirds of all evaluated rows. In multiple cases the public KB contained a clear, agent-safe answer that internal help-center search would not surface from natural customer wording — but Google found the same article on the first try.
- **Lowest-scoring issue families are `duplicate_or_unexpected_charge` and `wrong_or_problematic_service` (both avg_total 1.8).** Q004 (DoorDash "charged me twice") and Q008 (Uber "weird route") both fail the same way: the captured public docs do not distinguish the customer's actual scenario (true duplicate post vs. authorization hold; inefficient-route dispute vs. generic upfront-price change), so the agent-safe answer is forced to route to support rather than answer.
- **Instacart had the clearest escalation paths** (avg_escalation_clarity 3.0), with explicit "reach out to Instacart Customer Experience" routing in IC-003 and a dedicated unrecognized-charge form (IC-005). Uber was weakest on escalation (2.3) — UB-010 explicitly states Uber does not offer a rider phone number, so escalation requires logging in and going through trip-specific help.
- **AI overpromising happens off-source, not on-source.** Every source-constrained AI answer scored 3 on faithfulness. The unsupported-claims risk surfaced in **external** search behavior (Google AI Overview), which blended non-official sources (Reddit, JustAnswer, Quora, Facebook, GetHuman) and added specific refund timing, fare-adjustment certainty, or recovery promises that the captured KB does not support.
- **Freshness is uniformly absent.** Every company scored 1 on `freshness_signal` across every question — no visible last-updated date was observed on any captured help-center article.

## By company

See `company_score_summary.csv`.

| Company   | Avg total | Notable strengths                                   | Notable weaknesses                                              |
|-----------|-----------|------------------------------------------------------|-----------------------------------------------------------------|
| Instacart | 2.5       | Strongest answerability (3.0); strongest escalation clarity (3.0); explicit policy conditions (3-day reporting window, same-day refund language, EBT/PayPal handling). | Internal Help search failed on natural wording for 5 of 6 questions; "Instacart+" silently normalized to "instacart" on Q024. |
| DoorDash  | 2.4       | Strong escalation hub (DD-007) with 24/7 chat + phone; clear status-based cancellation refund table (DD-004).                                                            | Weakest single row in the audit (Q004 duplicate-charge, 1.8); internal search returned "No results found" for several natural-language queries.                                                                            |
| Lyft      | 2.3       | Pending-charges article (LY-006) is clean and specific; in-app dispute flow is consistent across rider help.                                                            | Q017 (dispute-refund timing) is the weakest Lyft row at 1.8 — the captured public KB does not state how long an approved dispute refund takes. Driver-facing content sometimes outranks rider-facing content (Q013).                                                                            |
| Uber      | 2.3       | Cancellation-fee article (UB-002) is the most precise policy doc in the audit, with explicit no-fee exceptions.                                                            | Weakest escalation clarity (2.3); unrecognized-charge questions fan into many sub-issues (Q010) before the agent can give a grounded answer; no rider phone number.                                                                            |

Spread across companies is narrow (2.3–2.5). The variation between issue families inside each company is larger than the variation between companies.

## By issue family

See `issue_family_summary.csv`.

- **Lowest-scoring families (avg_total 1.8):** `duplicate_or_unexpected_charge` and `wrong_or_problematic_service`. Both are cases where the user's described scenario does not map cleanly onto a captured KB article and the closest articles cover an adjacent but distinct policy condition.
- **Refund-status (avg_total 2.2)** is the next-weakest family. Across all four companies, captured public docs use qualified language ("typically," "depending on your bank") rather than a fixed business-day window. This is appropriate caution, but it leaves the agent unable to give a numeric timing answer — and as the AI-review notes show, external search will happily invent one.
- **Highest-scoring families:** `missing_items` (2.7) and several single-question families at 2.5 (`cancellation_fee`, `cancellation_or_refund`, `lost_item`, `membership_or_subscription_charge`, `pending_or_unexpected_charge`, `support_escalation`). The pattern is that single, well-bounded scenarios with explicit in-article policy do well; multi-branch scenarios (unexpected charges, refund status) do worse.

## Failure modes

See `failure_mode_summary.csv`.

| Failure mode                       | Count | Share  | Pattern                                                                                                                                                          |
|------------------------------------|-------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hard_to_retrieve                   | 10    | 41.7%  | Affects all four companies. The article exists and is correct, but the internal help-center search does not return it for natural customer phrasing.              |
| query_phrasing_sensitivity         | 6     | 25.0%  | Reformulating to a keyword query ("missing item", "wrong item", "refund") surfaces the correct article that the natural-language question did not.                |
| missing_policy_condition           | 3     | 12.5%  | The captured public KB does not address the user's exact policy condition (duplicate-charge vs. authorization hold; dispute-refund timing; "weird route" dispute). |
| ambiguous_issue_routing            | 2     | 8.3%   | Both Uber rows. A single user question (e.g., "trip not taken and charged") legitimately fans into multiple sub-policies that the agent must route through first. |
| audience_mismatch_retrieval        | 1     | 4.2%   | Lyft Q013: top search result was driver-facing cancellation/no-show policy; the correct rider article ranked 4.                                                   |
| requires_account_specific_data     | 1     | 4.2%   | Uber Q011: the refund-status answer is a logged-in flow keyed to a specific trip and date; no universal answer is publishable.                                    |
| (no failure mode tagged)           | 1     | 4.2%   | Q009 (Uber cancellation fee, late driver) — content and retrieval both strong; included as a positive-control row.                                                |

The first two modes are not bugs in the content. They are bugs in retrieval. An AI agent fronted with a better retrieval layer (semantic search, query expansion, or just letting an LLM rewrite the query before searching) would lift scores across roughly two-thirds of this benchmark without any KB change.

## AI overpromise patterns

Source-constrained AI answers scored 3 on faithfulness for every row — the constraint worked as designed. The interesting overpromising shows up in the `external_search_behavior` column, where Google AI Overview was captured during retrieval. Recurring patterns:

- **Refund-timing certainty without source backing.** Q011 (Uber), Q017 (Lyft), Q022 and Q023 (Instacart) all saw external search produce a "2–7 business days" or "5–10 business days" timeline citing Reddit or third-party sources alongside official pages. None of the captured public articles commit to a universal numeric window for posted-charge refunds.
- **Fare-adjustment promises.** Q008 (Uber inefficient route) and Q015 (Lyft upfront-price dispute) both saw external search produce "you can easily get a fare adjustment" / "Uber will typically adjust the fare" language that the captured pricing articles do not support.
- **Recovery-action invention.** Q001 (DoorDash missing delivery) and Q021 (Instacart missing delivery) both saw external search add steps (check delivery photo, contact the shopper within a 20-minute window) that are not present in the captured sources.
- **Cross-issue contamination.** Q003 (DoorDash canceled-but-charged) saw Google AI Overview return a missing-items refund answer for a cancellation-question — wrong-intent routing.

The implication for agent builders: source-constrained generation against a curated KB is the safe path. Letting the agent fall back to open-web synthesis when the KB doesn't have the answer is where overpromising is introduced.

## What surprised me

- **How narrow the company spread is.** I expected one of the four to be clearly ahead. They are within 0.2 of each other on avg_total. Differentiation shows up at the issue-family level, not the company level.
- **How completely retrieval dominated.** Going in I expected to find more content gaps. Most of the time the article was there and was good — internal search just couldn't find it.
- **The "Instacart+" → "instacart" normalization on Q024.** A search surface that silently rewrites the user's intent into a broader query loses the cancellation question entirely.

## What didn't surprise me

- **Zero freshness signals everywhere.** Public help-center pages rarely expose visible last-updated dates. Every company scored 1 on this dimension.
- **Refund timing is where AI hallucinates.** This was the most predictable failure mode going in, and the evidence confirms it: every refund-timing question (Q005, Q011, Q017, Q023) showed external search inventing a numeric window the official source does not commit to.
- **Multi-branch questions score lower.** Questions that legitimately fan into multiple policy paths (unrecognized charges, trip-not-taken charges) need the agent to route before it can answer, and the captured public docs don't always make the routing obvious.
