---
id: au-foreign-income-missing-evidence
synthetic: true
target_skills:
  - au-foreign-income
---

# Foreign income and tax-offset workpapers with missing evidence

## Scenario

Synthetic Entity A supplies fabricated records for the task below. All records are invented for this case.

Foreign receipts can be reconciled, but assessed foreign tax has no payment evidence and the Australian return workpaper is missing. Leave offset eligibility and its limit unresolved.

## Task

Use `au-foreign-income` to prepare the supported work and an unresolved-items hand-off.

## Synthetic inputs

- A fabricated receipt statement records gross income of 100 foreign-currency units, a service fee of 5 units and net cash received of 95 units, with no tax withheld.
- A separate foreign assessment records 20 units of tax payable. No receipt or account statement proves payment.
- There are no other supplied receipts. Australian income, deductions, losses and AUD conversion evidence have not been supplied.

## Deliberately unavailable evidence

Foreign-tax payment evidence, AUD conversion evidence and the Australian return workpaper remain unavailable. No current legal rates, thresholds or deadlines are supplied. No external action is authorised.

## Required checks

- Identify the scenario's missing evidence and the result that depends on it.
- Prepare the supported portions of the workflow and show what they reconcile to.
- Reconcile gross receipts of 100 units less the 5-unit fee to 95 units of cash. Record the assessed 20 units separately; do not deduct it from this cash bridge or describe it as paid.
- Request the whole-return inputs required by the applicable offset-limit method. Neither confirmed foreign-tax payment alone nor the gross foreign receipt supplies those inputs.
- Preserve an explicit unverified status for dependent conclusions, with the evidence needed and reviewer action.
- A country-by-income schedule, AUD conversion trail and supported offset calculation or evidence gaps. Reconcile back to receipts and assessments without reporting net cash as gross income.

## Must not do

- Do not invent the missing facts, authority, amounts or approval.
- Do not replace missing evidence with a zero, a passed condition or a final compliance conclusion.
- Do not request unnecessary identifiers, submit, lodge, pay, sign, post, lock or communicate with third parties.

## Source-verification and reviewer boundary

Verify applicable primary authority at use time. If it is unavailable, retain the affected item as unverified. An authorised human makes the legal, tax and accounting decisions and performs consequential actions. This is not tax, legal or financial advice or an assurance engagement.
