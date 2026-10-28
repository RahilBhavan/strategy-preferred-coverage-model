# Strategy economics: the learning and textbook plan

**Expanded course:** [Start the 16-unit course](course/README.md) for prerequisite lessons, problems, Excel labs, exams and worked keys. This earlier document remains the economic blueprint; use the course for the study sequence.

Prepared October 23, 2026. This is a learning blueprint, not a new set of market quotes or a forecast.

## The outcome

Understand how Strategy obtains capital, allocates it, creates contractual claims and distributes risk. Be able to explain a decision using a balance-sheet change, a cash schedule and an alternative management could have chosen.

“Tokenomics” is useful shorthand for supply, incentives and value flows here. The subject also includes corporate finance and security design: bitcoin has protocol rules; MSTR, notes and preferreds have issuer-controlled issuance and contractual rights. A company's marketing term is not a legal asset class.

The existing book has 30 numbered chapters. More chapters alone will not establish understanding. The next revision should connect the existing material in the order below and replace misleading shortcuts. Open [the interactive economic map](economic-map.html) for the worked examples. An [independent primary-source memo](economic-plan-source-check.md) records eight caveats.

Method: stock-flow accounting, contingent-claim analysis, investor segmentation, capital-allocation counterfactuals and dated liquidity stress. Original evidence: issuer filings, security terms, disclosures and dated transaction prices. Independent checks: reconcile transactions and ask Rahil to solve new examples without the answer key. Stop when the blueprint and worked examples are verified. Learning remains unobserved until Rahil answers.

## The organizing idea: every action faces three tests

1. **Per-share test:** what happens to net bitcoin per diluted share under the stated definition?
2. **Cash test:** can the company meet payments on their actual dates without assuming unavailable financing?
3. **Value test:** does the risk-adjusted benefit exceed the full economic cost and the next-best alternative?

Passing one does not imply passing the others. A repurchase can raise a per-share metric while consuming scarce cash. Issuance can secure liquidity while diluting a metric. Bitcoin appreciation can raise asset value without paying a dollar obligation.

Strategy explicitly limits what its net-BTC metrics establish; they are not traditional NAV, liquidity or general transaction-value measures. [Issuer metric definitions](https://www.strategy.com/notes).

## Learning sequence

### 1. Bitcoin, dollars and the scarcity question

Explain supply rules, custody, ownership, price formation, volatility and the difference between scarcity and a valuation. Direct BTC ownership does not itself create dollar cash flows. Dollar-denominated obligations create a sale-or-finance requirement even if bitcoin's long-run price rises.

Translate token vocabulary carefully: bitcoin supply versus corporate dilution; distributions versus protocol rewards; share buybacks versus token burns; legal claims versus protocol redemption. MSTR shares do not give holders a standing right to redeem a fixed quantity of bitcoin.

Question to answer: why can bitcoin be scarce while bitcoin per MSTR share falls?

Existing reading: f1, f2, ch1. Add a one-page vocabulary bridge and a no-issuance baseline. Verify the technical bitcoin discussion against protocol documentation before adding exact supply claims to the revised book.

### 2. Why put bitcoin inside a company?

Compare holding BTC directly, holding a spot fund, holding MSTR common and holding a preferred. Compare upside, fees, custody, permitted investment mandates, taxation, liquidity, options access and control over capital allocation.

Treat explanations for investor demand as hypotheses. Do not assume all institutions face the same mandate or every convertible buyer runs an arbitrage strategy. Explain which investor receives which payoff and which risk it accepts. Any durable premium requires a reason investors continue to value the wrapper.

Question: what service or exposure would a buyer pay Strategy for, and could an alternative provide it at lower cost?

Existing reading: e1, n1, v1, ch16. Add an investor-choice comparison grounded in actual terms.

### 3. Build the balance sheet before discussing the flywheel

Separate assets, cash, debt principal, preferred claims, common shares and potential conversion shares. Separate financing receipts, operating cash flows, distributions and accounting gains. Include software assets and liabilities, taxes and costs when the question requires an economic valuation.

Use a simplified residual only as a teaching model: assets less senior claims. Label the claim basis (face, liquidation preference, accounting amount or market value). These are different quantities. Do not subtract the present value of preferred payments and the preferred market value again in the same valuation.

Question: bitcoin rises on paper; which balance-sheet accounts move, and which cash accounts do not?

Existing reading: ch4, ch7, ch15, x1. Reconcile one filing across statements rather than reading each statement in isolation. [Q2 filing](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm).

### 4. Price every security as a bilateral trade

For MSTR, every note tranche, STRF, STRC, STRE, STRK and STRD, record: net proceeds, claim created, payout currency, payment discretion, cumulative rights, seniority, conversion rights, puts, redemption provisions, investor objective and issuer cost.

Separate zero cash coupon from zero economic cost. A convertible embeds an equity option and creates contingent repayment and dilution outcomes. A perpetual preferred lacks a scheduled maturity; that does not erase distributions, liquidation rights or contractual redemption provisions. Check each instrument independently. Immediate conversion parity (shares received × stock price) is not the embedded option’s full value.

Separate a security's stated amount from an investor's purchase price. A 10% dividend on $100 issued at $80 costs $10 a year on $80 of gross funding, or 12.5% before fees. That ratio does not include every economic cost.

Question: what feature compensates an investor for accepting a lower coupon?

Existing reading: ch5, t1, ch6, n1. Replace “no repayment, ever,” “free money” and guaranteed-price language. [Security and debt terms in the Q2 filing](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm).

### 5. Common issuance and the denominator

Define basic shares, dilution and the net-BTC metric before using mNAV. State which instruments are treated as shares and which as claims. Treat a published definition as dated; never splice older and newer mNAV series without adjustment.

Work the common-issuance example below. Then change the use of proceeds from BTC acquisition to funding distributions. More bitcoin on the balance sheet and more bitcoin per share are distinct results.

Question: why can issuance at the same stock price have different effects depending on what the proceeds fund?

Existing reading: ch3, ch8, ch12. The issuer's net metric treats in-money instruments differently from out-of-money instruments and omits some liabilities. [Current definitions and transaction caveats](https://www.strategy.com/notes).

### 6. Financing cost, carry and investment return

Teach four separate measures: coupon on stated amount; annual cash cost on net proceeds; the change in a stated-claim residual; and risk-adjusted value over time. Include issue discounts, fees, payout changes, FX, tax and embedded options when material.

The preferred example below shows why coupon divided by proceeds is not a universal BTC growth hurdle. For longer horizons, use a dated cash-flow schedule and explicit terminal claim treatment. A single constant annual rate cannot summarize every path.

Question: what additional return must compensate common holders for taking more downside risk, beyond merely covering a coupon?

Existing reading: e1, n1, x1. Add the one-year discount example before discussing any multi-year hurdle.

### 7. Liquidity, asset coverage and the sequence of events

Distinguish solvency, market-value asset coverage, a management reserve target and payment liquidity. For each quarter, start with opening cash, add actual receipts, deduct dated uses and show unmet funding needs. ATM authorization is a permission to issue, not a commitment from a buyer.

Show the paths with no new financing, limited common demand and continued market access. Test convertible puts separately from interest. Preferred distributions are not equivalent to debt coupons in every legal circumstance. Describe a breach, arrears or default only under the relevant contract.

Question: how can a company hold assets worth more than its claims and still face a payment problem?

Existing reading: ch7, k1, n5, s1, ch11. The issuer's USD Duration definition itself excludes some other uses such as convertible puts and maturities. [Definitions](https://www.strategy.com/notes).

### 8. Reflexivity and the demand feedback loop

Trace both directions: investor demand affects prices; prices affect net proceeds and dilution; allocation affects cash and per-share metrics; those outcomes may affect investor demand. Add price impact and competing financing supply. These are causal hypotheses to test, not automatic loops.

A premium is not cash until issuance executes. Higher equity volatility can make conversion optionality more valuable while also increasing distress risk. A rate reset may support preferred demand while increasing the issuer's cash bill. Neither channel guarantees a particular market price.

Question: which link fails first if BTC, common premium and preferred demand all weaken?

Existing reading: ch3, ch6, e1, v1, ch9. Add a causal map with each arrow labelled as accounting, contractual or empirical.

### 9. Management's capital-allocation menu

For every date, compare acquiring BTC, retaining cash, issuing common, issuing a preferred, issuing/refinancing notes, repurchasing a security, paying obligations and reducing leverage. An authorization does not force execution.

Use the same decision record every time: information available then; stated objective; alternatives; net proceeds and costs; per-share effect; cash effect; risk transferred; constraints; later observation. Keep management's stated rationale separate from our interpretation. Do not use a later price to claim an earlier choice was obvious.

The 2026 capital framework provides issuer explanations for reserve policy, rate policy, repurchases, BTC monetization and issuance discipline. It retains discretion near 1x; it does not establish the workbook's hard gate as a universal rule. The $1.25B reserve-building authorization is one part of the BTC monetization framework, not a blanket cap on every permitted BTC sale. [Capital framework](https://www.strategy.com/press/strategy-announces-digital-credit-capital-framework_06-29-2026).

Question: can an action reduce net BTC per share yet be necessary to meet obligations?

Existing reading: d1, n2–n5. Audit each historical rationale back to its contemporaneous source.

### 10. The software and financing franchises

Understand the software business's customers, pricing, recurring revenue, cloud transition, operating costs and actual cash contribution. Separate revenue from cash available for distributions. Ask whether treasury financing has a durable distribution advantage: scale, liquidity, investor reach, execution or trusted payment history.

Compare those explanations with competition, fund alternatives, fees, saturation and a falling premium. Issuing a security does not itself recognize operating revenue. Changing fair-value accounting does not create operating cash.

Question: if Strategy could not issue securities for two years, what would software contribute, and how would we prove it?

Existing reading: ch15, v1, ch16. Build a source-backed operating-cash bridge from the financial statements. [Q2 results](https://www.strategy.com/press/strategy-announces-second-quarter-2026-financial-results_07-30-2026).

### 11. Governance, taxes, legal constraints and custody

Study control and voting, board discretion, differences between investor groups, conflicts between payout support and common accretion, disclosure incentives and the role of compensation. Check authorized issuance, securities restrictions, contractual terms and tax capacity against actual documents.

Include currency exposure, custody/key risks and operational concentration. Do not infer a collateral lien from “bitcoin-backed” language or a cash guarantee from a price-stability objective. Tax return-of-capital treatment concerns holder taxation; it does not fund the issuer's distribution.

Question: who has the power to change the decision, who bears the cost, and what can an investor enforce?

Existing reading: g1, t1, ch15, ch9. [Q2 filing](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm), [issuer tax reporting and explanation](https://www.strategy.com/press/strategy-announces-fourth-quarter-2025-financial-results_02-05-2026).

### 12. Evaluate the complete system against alternatives

Reconstruct one historical decision and one hypothetical adverse case. Compare identical starting assets and investor capital, use the same dates and account for distributions. Separate realized observations from assumptions and unobservable alternatives.

Finish with three verdicts about the calculation, not the security: per-share metric increased/decreased; payments funded/unfunded; value conclusion supported/undetermined under the assumptions. A favorable conclusion on one metric is not an investment recommendation.

Existing reading: s1, ch11–ch14. Keep a source ledger and an error log beside the capstone.

## Two worked examples to anchor the book

### Common issuance: the use of proceeds matters

Illustration. Start with $100 of net assets and 100 common shares. Each share represents $1. Issue 20 shares at $1.25 and raise $25. Assume no taxes, fees or price change.

- Retain the cash or acquire BTC at unchanged prices: $125 / 120 = $1.04167 per share, up 4.17%.
- Use the entire $25 to pay preferred distributions: $100 / 120 = $0.83333 per share, down 16.67% versus the pre-issuance value.

The second result compares with the starting state. Its proper decision alternative is funding the same obligation another way, not pretending no obligation exists. Paying from the original cash would leave $75 / 100 = $0.75 per share. Issuance can therefore preserve more per-share value than that alternative while still reducing it from the starting level.

This example uses a simplified net-asset measure, not a full replication of Strategy's diluted net-BTC definition or a stock-price forecast.

### Preferred issuance: an annual cost ratio is not a full break-even

Illustration. Issue a preferred with a $100 stated claim for $80, buy $80 of BTC and pay a $10 distribution at year-end. Keep the claim at $100 in the teaching residual; exclude fees and taxes.

- Annual cash payout / gross proceeds = $10 / $80 = 12.5%.
- Initial stated-claim residual change = $80 − $100 = −$20.
- After one year, residual change versus no issuance is $80 × (1 + BTC return) − $100 − $10.
- At a 12.5% BTC return: $90 − $100 − $10 = −$20.
- This one-year residual reaches zero at a 37.5% BTC return: $110 − $100 − $10 = $0.

37.5% is not a perpetual annual hurdle or a fair-value conclusion. It is the answer to one explicit one-year question using a stated claim. A preferred's market value can differ from its stated claim. Discounted future distributions, investor required returns and terminal treatment belong in a separate economic valuation.

## The next textbook revision, in order

1. Correct conceptual shortcuts in e1, n1 and v1 before adding new material: no universal carry hurdle, no guarantee of self-funding above 1x, no zero-cost convert, no perpetual-as-no-obligations claim, no slices-as-secured-collateral implication.
2. Add a start-here map connecting the 12 units to existing chapter IDs. Define every metric before the first worked example.
3. Add transaction sheets and the two examples above. Every transaction must reconcile its assets, claims, cash and shares.
4. Add decision case sheets with stated reasons, counterfactuals and liquidity constraints. Source economic motives rather than inventing them.
5. Add the cash/return stress paths and compare them with direct ownership and a fund wrapper on matched assumptions.
6. Run a closed-book teach-back and a new numerical exercise. Rewrite the concepts that fail; do not infer comprehension from time spent reading.

No new recurring job, portfolio recommendation or public posting is part of this plan. Exact current market inputs, unsupported historical motives and native Excel checks remain separate work.

## Independent learning check

Without the book, Rahil should be able to:

- Trace $100 raised through assets, claims, shares and the first payment date.
- Explain why a zero coupon has an economic cost and a perpetual has continuing rights.
- Calculate both common-issuance cases and name their different comparison bases.
- Explain the 12.5% versus 37.5% preferred example without calling either a universal hurdle.
- Distinguish a per-share result, a liquidity result and a value judgment.
- Defend one decision against two alternatives using only information available at that date.
- Identify the assumptions needed for a favorable path and the first unmet payment in an adverse path.

Learning status: untested. This document's existence and an agent's arithmetic checks do not establish that these outcomes have been achieved.
