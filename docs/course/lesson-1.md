# Lesson 1. Assets, claims and cash

**Question:** how can a company get richer on paper and still run out of money?

By the end, you should be able to trace every transaction through assets, cash and claims. You should also distinguish financing from profit. The examples use simplified economic residuals, not a complete GAAP presentation.

## 1. Start with what exists

Imagine a treasury company owns 100 of BTC and 20 of cash. It owes 30 of debt principal. Preferred holders have a stated claim of 20.

Assets total 120. Deducting those senior stated claims leaves a common residual of 70. If there are ten common shares, the residual is 7 per share.

This is a claim-basis calculation. It does not establish the stock price. A market price can reflect future growth, distributions, taxes, options, control and risk. Preferred stated claims need not equal their market value or their accounting carrying amount.

The accounting identity is assets = liabilities + equity, with additional presentation categories where applicable. Do not put every preferred mechanically into GAAP liabilities. Our simplified identity is assets = debt claim + preferred claim + common residual, provided all terms use the stated teaching basis.

**Checkpoint:** if BTC falls by 20, which residual absorbs that loss in this simplified solvent stack? Common falls from 70 to 50. The cash balance remains 20.

## 2. Financing changes who has a claim

The company issues two new common shares at 8 each. Investors provide 16 cash.

Assets rise to 136. Cash rises to 36. Debt and preferred claims remain 30 and 20. The common residual rises to 86. Shares rise to 12. Residual per share becomes 86 / 12 = 7.1667.

Why did per-share value rise? The initial teaching residual was 7 per share. New investors paid 8. Under fixed assumptions, the existing holders' denominator grew more slowly than their residual assets.

Was the 16 operating revenue? No. The company obtained financing from owners. It did not sell software or earn an investment gain. The source belongs in financing analysis.

Now imagine borrowing 16 instead. Cash and assets still rise by 16, but the debt claim also rises by 16. The common residual does not rise at inception under this simplified basis. Future benefits and costs depend on deployment and financing terms.

**Checkpoint:** “The company raised 16, so it earned 16.” Correct the statement before continuing.

## 3. Changing the asset mix does not create an immediate gain

After the common issue, use 20 cash to acquire BTC at its current market price. Cash falls from 36 to 16. BTC rises from 100 to 120. Total assets remain 136.

The common residual remains 86. No new shares appear. The asset risk has changed: a larger share of assets now depends on BTC's price. The initial total value has not increased merely because dollars were converted into BTC.

The next question is forward-looking: does the expected benefit justify the risk and the alternative use of cash? The accounting bridge alone cannot answer it.

## 4. A gain is not necessarily a receipt

BTC now appreciates 25%, from 120 to 150. Cash remains 16. Total assets rise to 166. The teaching common residual rises to 116.

An accounting regime can recognize that asset remeasurement in income, subject to its rules and related tax effects. Recognition does not deposit 30 into the cash account. To turn some appreciation into dollars, the company needs a transaction, such as an asset sale or financing.

That transaction has consequences: fewer BTC, fees, tax, additional claims or dilution. A higher BTC price expands some options; it does not eliminate the cash schedule.

## 5. A distribution consumes cash

Pay a 6 preferred distribution from the 16 cash. Cash becomes 10. Assets become 160. Assume the preferred stated claim remains 20 after this current-period payment. The common residual falls to 110.

The distribution differs from repaying principal. A principal repayment reduces both cash and a debt claim by the same amount, before fees or extinguishment effects. A current distribution generally consumes assets without reducing that stated principal-like claim.

Do not deduct a dividend twice. If you start with cash already reduced by payment, you cannot subtract the same payment again from the resulting residual.

**Checkpoint:** what happens if the company repays 6 debt principal instead? Cash becomes 10 and debt becomes 24. Assets become 160; the common residual remains 116 under this model.

## 6. The cash schedule overrides the headline

The company now has BTC worth 150 and cash of 10. A 20 debt payment is due tomorrow. It has assets above its senior claims. Nevertheless, existing cash cannot meet that payment.

Possible responses include selling some BTC, arranging funding, reducing another permitted use or negotiating a contractual solution. None is automatic. Execution time, legal restrictions, market conditions and contractual rights matter.

Use two questions:

1. What are the claims worth relative to realizable assets?
2. What exact funds are available by the payment date?

The first is an asset/recovery question. The second is a payment-liquidity question. A company can pass the first and fail the second.

## 7. A clean transaction ledger

For each event, record these columns in Excel: event; BTC value; cash; total assets; debt principal; preferred stated claim; common residual; common shares; residual per share. Add a reconciliation cell for total assets minus all modeled claims and residual.

For cash, use opening balance + receipts − uses = closing balance. List financing receipts separately from operating cash. Add dates before you compare the balance with a payment requirement.

If the reconciliation is zero, the ledger is internally consistent. It is not proof that the assumptions, sources or valuation are correct.

## 8. Transfer this to Strategy

Use the issuer filing to distinguish software cash flows, security issuance, BTC purchases/sales, distributions, debt payments and fair-value movements. Follow the company's actual security terms. Do not replace them with our toy debt/preferred hierarchy.

For Strategy's net-BTC measure, consult the dated definition and diluted share rules. Our ten-share model deliberately omits conversions and awards so you can learn the cash/claim mechanics first.

Sources for the actual company boundaries: [issuer definitions](https://www.strategy.com/notes) and [Q2 2026 filing](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm). The numerical sequence above is an original hypothetical, not a reported Strategy transaction.

## Closed-book exit check

Reconstruct the sequence from opening assets through the distribution. Explain why common issuance, debt issuance, BTC purchases, BTC appreciation and distributions affect different columns.

Then change the share issue to two shares at 6. Predict the direction of dilution before calculating it. Complete [Lab 1](excel-labs.md) and A1–A2. If you cannot classify the receipts correctly, repeat this lesson before studying the premium loop.
