# Sixteen Excel labs

Build these in Excel. This file specifies the work; it is not a claim that you have already built or tested it. Keep source actuals, assumptions, formulas and checks separate. Use one workbook with coherent supporting sheets rather than sixteen disconnected models. Use no macros for the core labs.

For each lab submit: the workbook, a short written answer, one changed-input check and an unresolved-assumptions list. A formula that produces the expected number once is insufficient.

## 1. Transaction ledger

Use Lesson 1. Build columns for BTC, cash, total assets, debt, preferred stated claims, common residual, shares and residual/share. Put each event on a new row. Reconcile assets to all modeled claims. Run the lower-price share issue at 6 instead of 8. Explain the dilution direction before opening the formula result.

## 2. Dated cash flows

Build A3 and A4 from individual year rows. Add discount factors and PV, then compare the sum with a formula-based result. Change required return and payment timing. Explain the price sensitivity. Keep the infinite-perpetuity formula's assumptions visible; do not pretend a finite truncation is identical.

## 3. Return and liquidity paths

Build both Lesson 3 paths. Calculate cash uses, BTC sales, holdings and endpoint value. Reconcile every payment. Repeat with zero opening cash. Check that higher required sales never increase remaining BTC in the same path.

## 4. Ownership-wrapper comparison

Create a matched starting-investment comparison for direct BTC, a hypothetical BTC fund and a hypothetical treasury common share. Inputs: fee, claims, shares, distribution funding and assumed market multiple. Do not insert historical Strategy returns into hypothetical alternatives. State where tax, custody and investor mandate conclusions need source evidence.

## 5. Issuance and dilution

Rebuild B1 and B2. Keep basic shares, awards, in-money conversion shares and out-of-money debt separate. Test a conversion-price equality boundary consistent with the selected issuer definition. Check that a note never appears both as deducted principal and converted shares in that metric.

## 6. Preferred funding cost

For each preferred, record net proceeds, stated claim, annual cash rate, payout currency and rights source. Compute payout/net proceeds and a one-year residual under explicit terminal treatment. Compare with a market-valued perpetuity example. Do not label either a universal funding cost. Leave missing quote/source fields unavailable rather than zero.

## 7. Convertible payoff and funding dates

Plot B5 using one stock-price axis and clearly labelled payoff series. Then add real note dates, puts, coupons and conversion terms from a dated filing. Show where the toy payoff ceases to describe actual terms. Do not extrapolate the toy note into a real note valuation.

## 8. Investor choice memo

Create a security comparison sheet supporting a one-page memo. Consider a cash-income investor, a directional equity investor and an investor allowed to hedge. For each, identify payoff, risks, alternative and evidence needed. Investor personas are hypothetical, not documented Strategy buyer identities. Complete Set B and the midterm.

## 9. Quarterly cash engine

Build C1. Opening cash plus net proceeds less all cash uses equals ending cash. Separate distributions, coupon, principal and fees. Track registered capacity consumption. Display unmet financing needs explicitly. Test zero remaining ATM capacity. Compare with the existing coverage workbook only after your independent build works.

## 10. STRC policy scenarios

Separate declared-rate actuals, historic monthly VWAP guidance and an explicitly hypothetical stress rule. Compute C3. Add assumed preferred-price and rate paths without claiming a mechanical market-price peg. Show a higher dividend expense even when demand does not recover. Source each contract/policy date.

## 11. FX, tax and operating cash

Build C5–C6. Keep euro amounts and dollar translation visible. Reconcile software cash generation from a real filing, keeping accruals, working capital, capex and taxes separate. Create a holder-tax note for ROC. Do not deduct a hypothetical investor tax bill from issuer cash.

## 12. Joint stress and reverse stress

Combine BTC, premium, rate, FX and execution demand. Include a no-new-financing case. Define a concrete failure condition: the first unmet dated payment. Solve for a boundary under fixed assumptions and verify points on either side. Use a native Excel Data Table or recorded Goal Seek only when its setting and behavior have actually been exercised.

## 13. Value bridges

Build D1. Compare stated-claim residual and market-valued residual. Reconcile all claims to enterprise/asset value under one consistent basis. Add a cost and an independently justified benefit. Show that an allocation label alone does not create incremental operating cash flows.

## 14. Operating business plus treasury

Build D3 with separate operating free cash flow and terminal value. Add non-operating treasury assets once. Deduct debt and preferred values once. Change required return and terminal assumptions. Explain why the residual cannot be equated automatically with the issuer's net-BTC KPI.

## 15. Historical decision file

Choose one event in textbook d1 or n2–n4. Freeze an observation date. Capture the contemporaneous filing, terms and prices. Compare at least two feasible alternatives with the same obligations. Record stated rationale, your interpretation and later observations separately. Mark missing counterfactual evidence as missing.

## 16. Committee model

Combine the case inputs in assessments.md into a versioned model. Present per-share, cash and value conclusions separately. Include one disconfirming case, a source-to-cell register and a model-limit note. Reopen the saved workbook and rerun the changed-input check before submitting.

## Minimum modeling standards

- Typed values, consistent units, real dates and explicit observation cutoffs.
- Inputs in blue, formulas distinct, sources adjacent to actuals.
- Calculated outputs remain formulas, not pasted answers.
- No hidden “funding” plug, missing-as-zero assumption or silent circular calculation.
- Checks reconcile claims, cash, shares and aggregation independently.
- Recorded native Excel behavior remains separate from authoring/export checks.

The existing workbook still has its own native-Excel verification limits. Completing these lab instructions does not remove those limits without actual checks.
