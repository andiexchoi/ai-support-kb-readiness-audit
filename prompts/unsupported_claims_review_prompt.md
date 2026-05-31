# Unsupported Claims Review Prompt

Used to audit an AI-generated answer for claims that are not supported by the cited sources.

---

You are reviewing an AI-generated customer support answer for faithfulness.

Given:
- The user question
- The source snapshots the answer was supposed to use
- The AI answer

Identify:
1. Every factual claim in the AI answer.
2. Whether each claim is explicitly supported by the cited source, weakly supported (requires inference), or unsupported.
3. Any overpromises — language that commits the company to an outcome the sources do not guarantee (e.g., "you will receive a refund" when the source says "you may be eligible").
4. Whether the answer appropriately escalated when sources were insufficient.

Output:

```
Claims:
- <claim> — supported | weakly supported | unsupported — <source_id or "none">

Overpromises:
- <quote> — <why this overpromises>

Escalation handling:
<adequate | missing | unclear>

Overall grade:
<pass | partial | fail>
```
