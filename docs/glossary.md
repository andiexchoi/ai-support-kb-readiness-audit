# Glossary

**agent-safe answerability** — whether a well-behaved AI agent grounded only in a given source can give a complete, faithful, escalation-aware answer to a target customer question.

**account-specific dependency** — the degree to which a correct answer depends on authenticated state (order ID, account tier, region) that the agent may not have at the moment of response.

**faithfulness** — the property of an answer that every factual claim is directly supported by the cited source, with no inference or outside knowledge.

**context relevance** — the property that the retrieved sources actually contain information relevant to the user's question.

**escalation clarity** — the degree to which a source specifies *where* a user should go next when the article cannot resolve the issue, including channel and prerequisites.

**source dependency type** — the kind of authenticated or contextual state a given answer depends on (e.g., order ID, prior claim history, region).

**failure mode** — a recurring way the KB-plus-agent system breaks down: stale content, missing freshness signal, vague eligibility, missing escalation, account-state gap, overpromise, etc.
