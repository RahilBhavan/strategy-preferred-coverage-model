# Lesson 2. A payment's price depends on time and risk

**Question:** if a preferred promises 10 each year, what is that promise worth?

Prerequisite: Lesson 1 and percentage arithmetic. Keep dollars, dates and rates explicit. This lesson covers valuation models, not a prediction of any security's price.

## 1. A dollar now and a dollar later are different assets

If 100 can earn 10% for one year, it becomes 110. Two years produce 121, not 120, because the second year's return applies to 110.

Future value = present value × (1 + annual rate)^years. Reverse the operation to discount a future payment: PV = future payment / (1 + required return)^years.

At 10%, 121 in two years has a present value of 100. The discount rate is an assumption about compensation for time and risk. It is not a guaranteed return you can choose independently of the investment.

Nominal and real values also differ. A 10% nominal return with 4% inflation gives a real return of 1.10 / 1.04 − 1 = 5.769%. Subtracting rates gives a useful approximation, not the exact compounded result.

## 2. Price each dated payment once

A two-year bond pays 5 in one year and 105 in two years. At a 10% required return, its price is 5 / 1.10 + 105 / 1.10² = 91.3223.

The coupon is 5% of 100 face. Current yield is 5 / 91.3223 = 5.4751%. The modeled yield to maturity is 10%, given the specified payments. Those are three different quantities.

Why does current yield understate yield to maturity here? It omits the modeled gain from the purchase price to the 100 principal repayment. Actual realized return still depends on payment, reinvestment, sale timing and costs.

In Excel, put each year in its own row. Calculate the payment, discount factor and discounted payment. Sum the discounted payments. Never use a closed-form formula before you can reproduce its cash schedule.

## 3. A perpetuity is an assumption, not a maturity date

If a security pays a constant 10 every year forever, starting one year from now, its model price at required return r is 10 / r. At 12.5%, that is 80.

The result assumes the payment stream continues, the required return is appropriate and constant, and the first payment occurs at the stated time. Credit risk, payment discretion, variable rates, optional redemption and taxes can require a different model.

At an 80 market price, a $100 stated claim can still exist. Market price, claim at liquidation and accounting carrying amount answer different questions.

This matters when someone calls issuance at 80 an immediate 20 economic loss. A stated-claim residual falls by 20 if proceeds are 80 and the claim deducted is 100. But if a fairly priced perpetual's market value is 80, new assets of 80 and a new market-valued claim of 80 offset at inception before costs. The two calculations use different claim bases.

You cannot mix the favorable parts of both bases. Nor can you subtract both the preferred's market value and the present value of the same distributions in one residual calculation.

## 4. Carry is not the entire transaction

Take the 100 stated claim issued for 80, paying 10 per year. The annual payout / gross proceeds is 12.5%. After fees of 2, net proceeds are 78 and the same payout is 12.8205% of net funding.

Suppose the net proceeds buy BTC. To ask about common holders' benefit, specify a horizon, BTC price path, distribution funding, terminal claim basis and the alternative. “BTC must rise 12.5%” does not specify enough.

For a deliberately narrow one-year calculation with no fees, assets become 80 × (1 + g). Deduct the stated claim 100 and payout 10. The residual is 80 × (1 + g) − 110. It reaches zero at g = 37.5%.

That 37.5% is not a perpetual annual requirement or a fair-value estimate. It is a one-year stated-claim residual calculation. A different horizon, market-valued terminal claim or payout funding method changes the answer.

## 5. Opportunity cost belongs in the analysis

A BTC investment may appreciate enough to cover distributions and still offer inadequate compensation for risk. The relevant question compares its discounted benefits with its full costs and an alternative.

Net present value, NPV, is the sum of discounted inflows less the initial investment and other discounted uses. Use a return requirement consistent with the risk of the cash flows. A coupon is a contractual term, not automatically the appropriate discount rate for risky BTC exposure.

Do not apply an ordinary operating-company WACC formula to a crypto treasury without examining its cash flows, changing leverage, taxes and claim structure. Learn the model's assumptions before using its output.

## 6. Why a zero-coupon convertible is not free

Imagine a three-year claim to 100 with no coupons. In a toy straight-debt model using an 8% annual required return, its value is 100 / 1.08³ = 79.3832.

If a convertible sells for 100, a simplified decomposition could allocate 79.3832 to straight debt and 20.6168 to the equity option. That allocation is illustrative. Actual convert pricing couples credit, optionality, volatility, rates and contract terms.

The issuer's zero cash coupon does not erase the option granted to investors, issue fees, principal needs or possible dilution. A coupon comparison alone does not rank financing choices.

## Sources and practice

Read selected [MIT Finance Theory I PV and fixed-income lectures](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/). For later extensions, use [Finance Theory II capital structure and valuation notes](https://ocw.mit.edu/courses/15-402-finance-theory-ii-spring-2003/pages/lecture-notes/). These are graduate materials; start with the assigned sections, not every proof.

The examples and explanations here are independently authored. MIT's material is supporting reading, not a certification of this course. Complete A3–A4 and Lab 2 before consulting the worked solutions.
