# Lesson 4. Securities distribute risk; they do not manufacture assets

**Question:** why would investors accept different contracts against the same company?

Prerequisites: Lessons 1–3. Treat every payoff diagram as a model with stated assumptions. It does not override the certificate or indenture.

## 1. Start with a frictionless benchmark

Before discussing financial innovation, imagine no taxes, transaction costs, distress costs, information gaps or investor constraints. The operating assets and their cash flows remain fixed.

Changing how investors divide those cash flows does not, by itself, add another operating asset. This capital-structure benchmark is useful because it forces the next question: which real friction or capability creates value?

Possible mechanisms include tax effects, lower execution costs, access to constrained investors or improved allocation. Opposing effects include distress costs, fees, conflicts and reduced flexibility. A story must identify the mechanism and its cost, not merely rename the claim.

For the formal theory and qualifications, read selected [MIT Finance Theory II capital-structure notes](https://ocw.mit.edu/courses/15-402-finance-theory-ii-spring-2003/pages/lecture-notes/).

## 2. A simplified priority waterfall

Assume debt has a 100 claim and preferreds have a 100 claim. Common receives the remaining assets. Ignore competing liabilities, costs and instrument options.

If assets realize 300: debt receives 100, preferred receives 100 and common receives 100. At 150: debt receives 100, preferred receives 50 and common receives zero. At 80: debt receives 80 and the junior layers receive zero.

Each payout is limited by what remains after the prior layer. Total payouts equal realizable assets in this simplified liquidation. This is not an assertion that the issuer can immediately liquidate all assets at a displayed quote.

Actual bankruptcy/recovery analysis must account for secured claims, subsidiary liabilities, priority rules, costs and the contractual definition of each claim. A published “BTC cover” ratio is not a complete recovery model.

## 3. Preferred stock is a collection of rights

Record the stated amount, payout currency, cumulative treatment, ranking, conversion, issuer redemption and holder repurchase rights. Read the conditions on payment, deferral and remedies.

“Perpetual” usually identifies no scheduled maturity. It does not mean no redemption or repurchase provisions exist. “Cumulative” means unpaid amounts are treated under the specified accumulation rules; it does not make every missed payment a debt default.

Preferred stock does not automatically confer a lien over BTC or a fixed BTC redemption right. Separate collateral ownership from a priority claim against a company. Inspect the security documents before using “backed by bitcoin” as a legal description.

## 4. A convertible includes an option

Toy contract: principal 100, conversion price 20, so conversion delivers five shares. At maturity, assume the holder can choose cash 100 or five shares, and assume cash repayment is certain.

At a stock price of 10, conversion parity is 50 and the holder chooses 100 cash. At a stock price of 30, parity is 150 and the holder chooses conversion. The simplified terminal payoff is max(100, 5 × stock price).

That diagram assumes away default and many settlement terms. Real notes may have conditional exercise, issuer settlement choices, puts and calls. A price above the conversion price does not, alone, prove immediate legal exercise is available.

Conversion parity is shares × current stock price. It is not the option's full value. Before maturity, time and uncertainty can give the option value even when immediate conversion would be unattractive. Higher volatility can increase option value in standard models while creating other credit and liquidity risks.

## 5. The issuer and investor do not face identical questions

An investor asks about purchase price, distributions, possible sale price, credit outcomes and required return. The issuer asks about net proceeds, option cost, payout flexibility, claim priority, dilution and future cash needs.

An investor's high current yield does not prove cheap funding for the issuer. A low issuer coupon does not prove a low investor required return. Prices, rights, fees and timing connect both sides.

Convertible-arbitrage investors may hedge the stock exposure and trade volatility. Other holders may pursue different objectives. Without evidence, investor motives belong in the hypothesis column.

## 6. Apply this to Strategy's products

Build one contract record for MSTR, each note tranche and each of STRF, STRC, STRE, STRK and STRD. Use the observation date and amendment history. Do not assume all series have the same payment rights.

Then explain each buyer's alternative: direct BTC, a fund, another fixed-income security, common equity or another preferred. What feature does this contract supply? What risk or restriction pays for it?

Read the [Q2 filing](https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm) and the certificates/indentures it references. Consult [current metric definitions](https://www.strategy.com/notes) for the distinction between modeled claims and legal ownership. These sources constrain the company application; they do not turn our toy payoff into an exact description of a real instrument.

## Exit check

Draw the recovery waterfall and toy convertible payoff without notes. Explain what changes when the cash repayment is not certain. Identify three contractual facts you need before replacing the toy payoff with a real Strategy note.
