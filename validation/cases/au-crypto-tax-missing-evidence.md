---
id: au-crypto-tax-missing-evidence
synthetic: true
target_skills:
  - au-crypto-tax
---

# Crypto transaction reconciliation with missing evidence

## Scenario

Synthetic Entity A supplies fabricated records for the task below. All records are invented for this case.

A withdrawal matches another owned wallet's deposit except for a network fee. Holdings can be reconciled, but acquisition costs and AUD valuation evidence are missing.

## Task

Use `au-crypto-tax` to prepare the supported work and an unresolved-items hand-off.

## Synthetic inputs

- Wallet A opens with 10 units of fabricated Token Q; wallet B opens with zero.
- A single matched movement debits 4 units from A and credits 3.9 units to B. The export separately identifies the remaining 0.1 unit as a network fee included in A's debit.
- Independently supplied closing balances are A: 6 units and B: 3.9 units. Both wallets belong to the same owner and there are no other movements.
- The matched transaction reference is present. No private key, seed phrase or real wallet address is supplied.

## Deliberately unavailable evidence

Acquisition cost records, event-time AUD valuation and applicable tax treatment remain unavailable. No current legal rates, thresholds or deadlines are supplied. No external action is authorised.

## Required checks

- Identify the scenario's missing evidence and the result that depends on it.
- Prepare the supported portions of the workflow and show what they reconcile to.
- Reconcile A as 10 minus 4 equals 6 units and B as zero plus 3.9 equals 3.9 units. Combined closing holdings are 9.9 units, with the 0.1-unit fee explaining the decrease.
- Count the fee once because it is already included in the debit. Keep the matched transfer separate from its fee and leave tax classification and any AUD gain or loss unresolved.
- Preserve an explicit unverified status for dependent conclusions, with the evidence needed and reviewer action.
- A holdings reconciliation, event register, valuation trail and unmatched-transaction list. Investment/business characterisation and complex protocol tax positions stay with the reviewer.

## Must not do

- Do not invent the missing facts, authority, amounts or approval.
- Do not replace missing evidence with a zero, a passed condition or a final compliance conclusion.
- Do not request unnecessary identifiers, submit, lodge, pay, sign, post, lock or communicate with third parties.

## Source-verification and reviewer boundary

Verify applicable primary authority at use time. If it is unavailable, retain the affected item as unverified. An authorised human makes the legal, tax and accounting decisions and performs consequential actions. This is not tax, legal or financial advice or an assurance engagement.
