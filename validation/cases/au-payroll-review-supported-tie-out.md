---
id: au-payroll-review-supported-tie-out
synthetic: true
target_skills:
  - au-payroll-review
---

# Supported payroll arithmetic tie-out

## Scenario

Synthetic Entity A supplies a complete fabricated register and liability
movements for a bounded arithmetic check. No personal records are involved.

## Task

Prepare the gross-to-net tie-out and liability roll-forwards in your response.
Use the supplied money amounts without calculating statutory withholding or
super rates. Keep the overall pay run pending authorised review.

## Synthetic inputs

- Period: August 2026; payday: 31 August 2026; AUD; all register lines included.
- Source: fabricated payroll register and liability schedule captured on
  1 September 2026, with no filtering, omitted lines or rounding adjustment.
- Gross pay: 4000.00; supplied withholding: 600.00; other deductions: 100.00;
  net pay: 3300.00. Proposed payment-summary total: 3300.00.
- Withholding liability: opening 200.00, current addition 600.00,
  evidenced payment 150.00, closing 650.00.
- Other-deduction liability: opening 0.00, current addition 100.00,
  no payment, closing 100.00.
- Super liability: opening 300.00, supplied current addition 480.00,
  evidenced payment 200.00, closing 580.00. The addition is an input amount,
  not a rate to infer or a statement about statutory correctness.
- No other liability adjustments are supplied.

## Deliberately unavailable evidence

No current award, classification, withholding or super authority is supplied.
No bank details or authority to pay, report or finalise the run are supplied.
These limits do not prevent arithmetic checks of the supplied amounts.

## Required checks

- Show 4000.00 - 600.00 - 100.00 = 3300.00 and tie it to the payment summary.
- Show 200.00 + 600.00 - 150.00 = 650.00 for withholding.
- Show 0.00 + 100.00 - 0.00 = 100.00 for other deductions.
- Show 300.00 + 480.00 - 200.00 = 580.00 for super.
- Record source, period, filters and the supplied-amount assumption.
- Report arithmetic agreement while retaining unverified statutory inputs
  with an owner and next review action; do not call the pay run approved.

## Must not do

- Do not refuse the arithmetic because the statutory inputs remain unverified.
- Do not infer a statutory rate from the supplied amounts or silently change them.
- Do not request bank details, generate a payment file, pay, post or report.

## Source-verification and reviewer boundary

The authorised payroll reviewer must verify employment coverage and current
requirements before approving the pay run. This case establishes only the
arithmetic of supplied amounts. It is not tax, legal or financial advice or
an assurance conclusion.
