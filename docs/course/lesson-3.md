# Lesson 3. The path can matter as much as the destination

**Question:** can two identical ending BTC prices leave different amounts of BTC behind?

Prerequisites: Lessons 1–2. This lesson assumes fixed cash obligations in its examples. Actual payment rights depend on each contract.

## 1. Arithmetic averages can mislead

An asset rises 50% and then falls 50%. The arithmetic average of the two returns is zero. But 100 becomes 150 and then 75, a 25% loss.

Returns compound multiplicatively. For two annual periods, the geometric annual return is (75 / 100)^(1/2) − 1 = −13.3975%. A quoted average should name the method and period.

Volatility is variation, not a complete description of risk. A payment shortfall, custody loss, poor execution or tax liability can matter even when a historical volatility estimate looks modest.

## 2. Leverage changes the residual's sensitivity

Suppose assets are worth 200 and fixed senior stated claims are 120. The common teaching residual is 80. A 10% asset decline removes 20 from that residual, a 25% decline.

At that starting point, the asset-value-to-residual ratio is 200 / 80 = 2.5. It describes a local sensitivity under fixed claims. It is not a stable prediction of the stock's market return.

Market premiums, option moneyness, fees, distributions and future issuance can change the relationship. Near distress, common's limited liability also makes a simple linear sensitivity inadequate.

## 3. The same endpoint can leave different holdings

Illustration. Start with 10 BTC and 20 cash. Three cash payments of 20 are due at dates 1, 2 and 3. Use cash first. At each date, sell only enough BTC to cover any remaining payment. No fees, taxes or new financing.

Path A prices are 100, 50 and 100. The first payment exhausts cash. At date 2, sell 20 / 50 = 0.4 BTC. At date 3, sell 20 / 100 = 0.2 BTC. Remaining BTC is 9.4, worth 940 at the endpoint.

Path B prices are 100, 150 and 100. Cash is exhausted at date 1. At date 2, sell 20 / 150 = 0.133333 BTC. At date 3, sell 0.2 BTC. Remaining BTC is 9.666667, worth 966.6667.

Both paths end at 100. Both pay 60. The path that requires a sale at the lower price sacrifices more BTC. “BTC recovers by the end” does not undo the earlier sale.

This is not a claim that every price decline forces a sale. It shows the effect of the particular cash rule and the absence of other funding.

## 4. Coverage ratios need a dated denominator

Cash of 50 and annual payouts of 10 suggest five years of payout coverage under flat annual payments. Add a 40 principal payment tomorrow and that statement no longer describes all uses of cash.

After the principal payment, only 10 remains. Timing, reserves for other purposes and execution windows matter. A reserve earmark may describe management's intent rather than a legally segregated trust; verify the actual arrangements.

Build the schedule: opening cash + available receipts − payments = ending cash. Show a negative required balance as unmet funding. Do not insert “new issuance” simply to make ending cash nonnegative.

## 5. Funding authorization is not investor demand

An issuer can have registered capacity to issue securities and still obtain poor prices, insufficient demand or no timely execution. Model capacity, placement volume, price and costs separately.

The common price and financing demand may also weaken when BTC falls. Treat their relationship as a scenario assumption or an empirical estimate. Do not call it a law.

A favorable loop might be: demand supports a premium; premium issuance changes the per-share metric; reported growth supports demand. Each causal link requires evidence. The reverse loop can involve dilution, reduced liquidity and a lower price.

## 6. Distinguish risk types before adding scenarios

- Asset risk: BTC's price and realizable value.
- Market-access risk: ability to execute issuance at usable prices.
- Payment risk: ability and legal obligation to make dated payments.
- Refinancing risk: replacement funding for puts or maturities.
- FX risk: dollar cost of foreign-currency obligations.
- Operational/legal risk: custody, settlement, restrictions and enforceability.

Different risks can arrive together. Four isolated single-variable shocks do not establish resilience to a joint shock.

## Exit check

Rebuild both paths in Excel and verify every payment is funded. Then replace the initial cash with zero and recompute. Explain why the endpoint still cannot determine the answer on its own.

Read the issuer's [metric limitations](https://www.strategy.com/notes) alongside its [capital framework](https://www.strategy.com/press/strategy-announces-digital-credit-capital-framework_06-29-2026). Those documents distinguish several cash, reserve and asset metrics. All amounts in this lesson are hypothetical.
