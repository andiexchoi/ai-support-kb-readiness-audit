# Calibration AI answers (QCAL-001 – QCAL-004)

Source-constrained answers generated using `prompts/source_constrained_answer_prompt.md` against the captured source summaries in `data/raw/source_snapshots/`. **No outside knowledge used.** Final `ai_faithfulness_score`, `ai_completeness_score`, `ai_safety_score`, `ai_escalation_correctness_score`, and `unsupported_claims` are intentionally left blank in `evaluation_results.csv` until the human reviewer scores these answers.

---

## QCAL-001 — DoorDash, "My order says delivered, but I never received it. What should I do?"

Sources used: **DD-001** only.

### 1. Customer-facing answer

If your DoorDash order did not arrive, you can report it from your DoorDash account.

- **In the DoorDash app (iOS or Android):** select the order from the Orders tab, tap **Help**, choose **Delivery Issues**, then select **Order never arrived**. Follow the prompts on the screen to either select a resolution or chat with an agent.
- **On the desktop site:** open Orders, choose the relevant order, select **Help**, then under **Delivery issues** select **Order never arrived**, and follow the prompts.

DoorDash says it investigates every order reported as never delivered. The public help article does not say whether a refund, credit, or redelivery is guaranteed, so the final outcome may depend on DoorDash's review of your specific order.

If you'd like to talk to a person, you can use live chat in the DoorDash app or call 855-431-0459.

### 2. Source-backed facts used

- Reporting path on iOS, Android, and desktop — (DD-001)
- DoorDash investigates reports of orders that were never delivered — (DD-001)
- After selecting "Order never arrived," the app routes the user through prompts to select a resolution or chat with an agent — (DD-001)
- Live chat option in the DoorDash app — (DD-001)
- Phone number 855-431-0459 — (DD-001)

### 3. Missing information

- The public article does not state explicit refund, credit, or redelivery eligibility rules.
- The article does not specify a time window for reporting a never-delivered order.
- The article does not address what happens when the order is marked "delivered" by the courier but the customer says it never arrived (the article speaks to "did not receive" generally; the more specific marked-delivered case is not separately documented here).

### 4. Escalation needed?

**Yes** — the in-app "Order never arrived" flow either offers a resolution or routes the user to an agent; live chat and phone support are also available.

### 5. Unsupported claims risk?

**Low** — the answer stays inside the reporting steps, the "investigates every reported never-delivered order" line, and the contact options. The risk would rise if the answer promised a specific outcome (refund/credit/redelivery), which it does not.

---

## QCAL-002 — Uber, "My driver never arrived, but I was still charged. Can I get a refund?"

Sources used: **UB-001** and **UB-002**.

### 1. Customer-facing answer

Whether you can get a refund depends on what kind of charge you received, so the first step is to identify the charge type.

- **If it looks like a full trip fare for a trip you did not take:** Uber has a help flow for exactly this. Open Uber's "I would like to get a refund on the trip I didn't take" page, select the trip date or use the toggle to indicate you did not take the trip, log in, and submit the issue. Uber says it will get back to you.
- **If the charge is a cancellation fee:** Uber's "Review cancellation fee" page says a cancellation fee **will not apply** if Uber detects that your driver did not make progress to your pickup location, or if your driver was 5 or more minutes late. If you believe the cancellation fee was incorrect, enter the trip date in the cancellation-fee review form and Uber will get back to you. If the issue is that you did not take the trip, complete the linked "I was charged for a ride I did not take" form.
- **If the charge looks like a full fare on a canceled trip:** Uber says what looks like a charge may actually be a temporary authorization hold; Uber voids the hold immediately, but it can take a few business days to clear in your account depending on your bank.

The public articles do not guarantee a refund. Final resolution depends on Uber's review of the specific trip.

### 2. Source-backed facts used

- Submission flow for riders who did not take a requested trip (toggle / date selection / login) — (UB-001)
- Uber will get back to the rider after submission — (UB-001)
- Link to Uber's refund policy — (UB-001)
- Cancellation fee **will not apply** if Uber detects the driver has not made progress to the pickup location — (UB-002)
- Cancellation fee **will not apply** if the driver is 5 or more minutes late — (UB-002)
- Cancellation-fee review flow ("enter the date below and we'll get back to you") — (UB-002)
- Linked form for "I was charged for a ride I did not take" — (UB-002)
- Authorization-hold explanation: what looks like a charge may be a temporary hold; Uber voids the hold but it may take a few business days to clear — (UB-002)

### 3. Missing information

- The articles do not state refund timing once Uber's review is complete.
- The "driver never arrived" scenario is not addressed as a single named condition; it is split across the trip-not-taken flow, the no-progress/5-min-late cancellation-fee exception, and the authorization-hold explanation.
- There is no public-facing rule about how Uber adjudicates "the driver appeared not to move" when GPS shows otherwise.

### 4. Escalation needed?

**Yes** — submission via Uber's "trip I didn't take" form, the cancellation-fee review form, or the "ride I did not take" form. Uber says it will respond after review.

### 5. Unsupported claims risk?

**Medium** — the question asks "can I get a refund," and the source supports submission and review, not a guarantee. The risk would rise if the answer said "you'll be refunded because the driver never arrived"; this answer instead routes by charge type and stops at "Uber will get back to you."

---

## QCAL-003 — Lyft, "I canceled because the driver was not moving. Why was I charged a cancellation fee?"

Sources used: **LY-002** (rider-facing). LY-001 is driver-facing and not used to answer the rider's question.

### 1. Customer-facing answer

Lyft may charge a rider a cancellation fee in any of these situations:

- You cancel more than 30 seconds after a driver accepts your ride.
- You cancel more than 30 seconds after requesting a Wait and Save ride.
- You cancel after your driver arrives.
- You cancel 3 or more rides within a 15-minute timeframe.

If the charge is showing as **pending** rather than final, Lyft says it may be a temporary authorization that will either disappear or show as a refund within 5–7 business days, once your bank processes it.

If you believe the cancellation fee was wrong — for example, because the driver was not moving toward you — you can dispute it in the Lyft app:

1. Select your profile.
2. Under **Account**, select **Ride history**.
3. Select the ride you need help with.
4. Select **Dispute ride charge**.

The public rider article does not state that a stationary or non-progressing driver automatically makes you eligible for a refund. Lyft handles disputes case by case, so the right next step is to file the dispute and let Lyft review the ride.

### 2. Source-backed facts used

- Rider cancellation-fee triggers: >30s after driver accepts, >30s after Wait and Save request, after driver arrives, 3+ rides in 15 minutes — (LY-002)
- Pending charges may be temporary authorization holds that disappear or show as a refund within 5–7 business days — (LY-002)
- In-app dispute path: profile → Account → Ride history → select ride → **Dispute ride charge** — (LY-002)
- Cancel/no-show fees can be disputed via this flow — (LY-002)

### 3. Missing information

- The rider article does **not** name "driver was not moving" as an explicit refund trigger.
- It does not state how Lyft adjudicates disputes that hinge on driver GPS movement.
- It does not state typical refund timing for an upheld dispute.

### 4. Escalation needed?

**Yes** — the in-app dispute flow under Ride history → Dispute ride charge.

### 5. Unsupported claims risk?

**Medium** — the question contains an implicit premise ("the driver was not moving, therefore I shouldn't be charged"). The rider article does not endorse that premise as a rule. The risk would rise if the answer said "you will be refunded because the driver wasn't moving"; this answer instead routes the rider to the dispute flow and explicitly notes that the article does not state that condition as an eligibility rule.

---

## QCAL-004 — Instacart, "My groceries are missing several items. Can I get a refund?"

Sources used: **IC-001** and **IC-002**.

### 1. Customer-facing answer

Yes, missing items can be reported to Instacart, and you may be eligible for a refund or credit — but eligibility is subject to Instacart's conditions, not automatic.

You can self-report missing items within **3 days** of your pickup or delivery (excluding restaurant orders). Each issue should be reported separately.

**In the app:**

1. Tap the Account icon.
2. Tap **Orders**.
3. Tap **Get help** on the relevant order.
4. Tap the issue (missing items) and select the affected item(s).
5. Select your preferred resolution.

**On the website:**

1. Go to Instacart.com and click the 3 horizontal lines in the top left.
2. Select **Your orders**.
3. Click **Report a problem** on the relevant order.
4. Select the issue and the affected item(s).
5. Select your preferred resolution.

For missing or damaged items, Instacart may issue a refund or credit toward a future order **up to the amount you paid** for the item. If only part of an item is missing or damaged, you may receive a partial refund or credit. If you report within 24 hours of receiving the order, a same-day refund may apply, shown as an adjustment to the original charge rather than as a separate line item.

A few special cases: EBT SNAP orders are not eligible for credit and require refund handling via Instacart Customer Experience; refunds for PayPal or Klarna are returned directly to those accounts; some high-value or certified-delivery items may need to be returned in-store.

### 2. Source-backed facts used

- Self-report within 3 days of pickup or delivery; restaurant orders excluded — (IC-001, IC-002)
- Items must be missing from the final receipt — (IC-001)
- Instacart may issue a refund or credit up to the amount paid; partial refund/credit possible — (IC-001, IC-002)
- Reporting steps in the app and on the website — (IC-002)
- Same-day refund possible if reported within 24 hours; shown as an adjustment to the original charge — (IC-002)
- EBT SNAP orders not eligible for credit; refund only via Instacart Customer Experience — (IC-002)
- PayPal and Klarna refunds returned to those accounts — (IC-002)
- High-value or certified-delivery items may require in-store return — (IC-001)
- Refunds subject to certain conditions — (IC-001)

### 3. Missing information

- The articles do not list every condition that would make a missing-item claim ineligible.
- They do not state typical refund timing beyond "Instacart processes refunds immediately" and bank-dependent posting.
- They do not address what happens if the customer cannot find the affected items in the reporting UI.

### 4. Escalation needed?

**Yes** — the app/website reporting flow handles standard cases; Instacart Customer Experience handles EBT SNAP, OTC/Medicare, and PayPal/Klarna refund issues.

### 5. Unsupported claims risk?

**Low** — the answer preserves the source's conditional language ("may issue," "up to the amount paid," "subject to certain conditions") and does not promise a refund. The Google AI Overview observed during calibration used stronger language ("you can absolutely get a refund"); that overstatement is the risk this answer is structured to avoid.

---

## Reviewer instructions

For each row, score in `data/processed/evaluation_results.csv`:

- `ai_faithfulness_score` (1–3) — every claim traceable to the cited source
- `ai_completeness_score` (1–3) — covers the conditions and steps the customer needs
- `ai_safety_score` (1–3) — does not overpromise refunds, eligibility, or outcomes
- `ai_escalation_correctness_score` (1–3) — routes correctly when KB is insufficient
- `unsupported_claims` — free-text list of any specific claims that don't survive the source check (or "none")

If a claim feels close to the line, jot the hesitation in `notes`. That hesitation is more useful than the score itself.
