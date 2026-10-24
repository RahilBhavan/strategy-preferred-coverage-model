# Readings, source discipline and textbook corrections

Access/review cutoff: October 23, 2026. This guide supplies the bridge between finance theory and the existing textbook. It does not certify every historical balance in that textbook or refresh October quotes, outstanding shares or declared rates. The numerical exercises are hypothetical unless specifically labelled otherwise.

## Which source answers which question?

**Finance theory.** [MIT 15.401 Finance Theory I, Fall 2008](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/) provides present value, fixed income, equities, options and risk/return. Use the [lecture videos and slides](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/) by topic. The original MIT assignments/exams are optional further practice; our questions and prose are independently authored. The course does not award MIT credit or imply affiliation.

**Corporate finance.** [MIT 15.402 Finance Theory II, Spring 2003](https://ocw.mit.edu/courses/15-402-finance-theory-ii-spring-2003/) develops investment and financing decisions. The [lecture notes](https://ocw.mit.edu/courses/15-402-finance-theory-ii-spring-2003/pages/lecture-notes/) cover capital structure, informational/dynamic considerations, free-cash-flow valuation and real options. These are graduate materials. Learn the prerequisite arithmetic before advancing; a sophisticated label does not replace understanding the payment stream.

**Bitcoin protocol.** The [Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/) explains transactions, wallets, mining and protocol mechanics. Use it for how ownership and transfers work. It cannot establish a BTC fair price, expected return or the market demand for Strategy securities. Add a dated, explicit demand model before making economic predictions.

**Issuer definitions.** [Strategy Notes](https://www.strategy.com/notes) explains issuer KPIs, limitations and methodology changes. A live page may change. Save the observation date and definition used. Reproduce the definition before comparing dates. A definition is evidence of how a KPI is calculated, not independent validation of its economic merits.

**Financial position and commitments.** Use the [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000020/mstr-20251231.htm) and [June 30, 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm) for the periods they report, then bridge subsequent dated filings. Read the statements, liquidity discussion, debt notes, preferred notes, commitments and risks together. These historical filings do not prove today's balance.

**Policy versus obligation.** The [June 29, 2026 capital framework](https://www.strategy.com/press/strategy-announces-digital-credit-capital-framework_06-29-2026) records announced policy at that date. Read its conditions/exceptions. A policy is not a bond indenture, a funded bank facility or guaranteed ATM demand.

**Legal rights.** Read final prospectuses, filed certificates, indentures and all applicable amendments. The [original STRK certificate](https://www.sec.gov/Archives/edgar/data/1050446/000119312525020868/d791994dex31.htm) is historical; do not assume it incorporates later amendments. The [June 2026 amended STRC certificate](https://www.sec.gov/Archives/edgar/data/1050446/000119312526270366/d144149dex31.htm) is a starting document for that version. For every live analysis establish whether later documents supersede it. Source each series separately: STRK, STRF, STRD, STRC and STRE.

**Governance.** Obtain the proxy and relevant compensation/board disclosures for the actual decision date. The syllabus does not supply a verified compensation-motive conclusion. A management interview supports what management said; it cannot establish every private intention.

## Read the existing textbook with these corrections

Chapter references use stable IDs because displayed chapter numbers have changed. The companion reader links these IDs directly. The full bounded review is in [the source-check memo](../economic-plan-source-check.md).

**e1 — financing and the “machine.”** Selling a security raises financing and creates a claim. It is not operating revenue or automatically profit. Preferred securities are not fractional BTC ownership or automatically secured by a BTC lien. Buyer categories are analytical possibilities unless supported by actual investor evidence. The company can sell BTC to fund needs under applicable decisions; do not teach sales as categorically unavailable.

**e1 and n1 — funding cost.** Annual distribution divided by stated amount is a cash rate on that denominator. Divided by gross/net proceeds it is a different carry measure. Neither alone is the complete economic cost. Replace an unqualified “BTC growth break-even” with a dated scenario naming fees, payout funding, horizon, terminal claim and alternative. A capital gain does not supply cash unless monetized.

**n1 — perpetuals and conversion.** “No scheduled maturity” does not eliminate issuer redemption or holder repurchase provisions. Zero coupon does not erase the conversion option or puts. Immediate conversion value is not full option value. Terminal stock price alone does not establish whether a real note was exercisable or how it settles. Use series-specific contracts.

**ch8, e1 and v1 — per-share measures.** Gross BTC/share, net BTC/share, GAAP equity/share and intrinsic value/share are different. Specify cash/USD Assets, senior claims, awards and conversion treatment. The issuer's mNAV methodology changed in 2026; bridge definitions before comparing historical values. Avoid deducting a note and simultaneously counting its conversion shares in a metric that treats those as alternatives.

**v1 — a premium is not permission to print value.** Above-one issuance can increase a defined per-share metric under fixed prices and deployment assumptions. Below-one issuance is not mechanically impossible. Registration is not executed demand. A local leverage calculation is not a common-stock return forecast, and a chosen multiple is not independent valuation evidence. Model the possible financing franchise against a feasible no-franchise alternative.

**ch6 and n4 — STRC.** Keep the board's contractual authority, dated rate declaration and historical price/VWAP guidance distinct. A stress rule in your spreadsheet is an assumption. Do not describe a higher rate as a guaranteed price peg or an automatic legal response to a BTC decline.

**k1, s1 and the coverage model — recovery and cash.** Asset coverage does not establish collateral ownership or guarantee recovery. Include other claims, realization costs, distribution treatment and execution limits. The first dated cash shortfall is different from the date that a static BTC/claim ratio crosses one.

**ch15 — accounts and taxes.** Fair-value income is not software cash flow. An investor's return-of-capital classification does not by itself remove issuer distributions or prove their sustainability. Keep holder and issuer tax/accounting analyses separate and establish jurisdiction and reporting period.

When a legacy textbook sentence conflicts with a primary document, record the conflict and use the applicable primary document. Treat unverified historical numbers as reading examples, not current model inputs. The companion course adds correction guidance; it does not claim that the entire legacy textbook has been rewritten or independently audited.

## A source-to-cell register you can audit

For every actual input record: source title and URL, filing/publication date, financial observation date, access date, page/section, currency/units, exact field, workbook cell and any transformation. Keep assumptions in separate rows with their rationale. A historical issuance price cannot silently become today's execution price.

For each contractual claim record the original instrument, amendments, applicable effective date and operative section. If the latest amendment or current notional is missing, mark the field **unverified**, identify what is needed and limit the conclusion. Do not fill missing rates, balances or rights with zero.

## Beyond this course

The 112-hour course is concentrated training on this company and its financing. A finance degree also spans broader accounting, microeconomics, macroeconomics, statistics/econometrics, investments, institutions and many other cases. Further depth would add probability and regression, a proper option-pricing model, term structures/credit spreads, empirical identification and legal/tax specialist work. Finish the core cash/claims models before using that machinery.

The human reader test remains **untested until you submit your own answers**. Begin with: where does dividend cash come from; who has priority; why can STRC's rate change? Later gates demand calculation and a defense as well as explanation.
