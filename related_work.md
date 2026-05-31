# Related Work

## WixQA

A benchmark of real customer support questions paired with knowledge-base answers. Useful as a precedent for evaluating retrieval-augmented systems against a curated KB rather than open-domain knowledge.

## RAGAS

A framework for evaluating RAG systems on dimensions like faithfulness, context relevance, and answer relevance. This audit borrows the spirit of faithfulness and context relevance, but applies them to the *source documents themselves* — asking whether the KB is even capable of supporting a faithful, relevant answer.

## Amazon agent evaluation

Public writeups from Amazon on evaluating support agents emphasize escalation accuracy and avoiding overpromising. This audit incorporates an explicit "escalation clarity" dimension for the same reason.

## How this differs

Most prior work evaluates the *agent* given a KB. This audit evaluates the *KB* given a hypothetical well-behaved agent. The premise is that even a perfect agent can't recover from missing, stale, or account-dependent source content.
