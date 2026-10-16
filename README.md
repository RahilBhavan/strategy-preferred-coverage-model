# Strategy preferred dividend coverage in Excel

How long can Strategy fund dividends on STRF, STRC, STRE, STRK and STRD, and what changes when convertible holders can demand cash?

[Download workbook](Strategy_Preferred_Coverage_Model.xlsx) · [Project page](https://rahilbhavan.github.io/strategy-preferred-coverage-model/) · [Textbook](https://rahilbhavan.github.io/strategy-preferred-coverage-model/textbook.html)

The financial model runs through Excel formulas. JavaScript authors the workbook and reproduces a limited snapshot calculator for the website. Python is used only for XLSX metadata and an independent test harness, not the financial model.

## What changed

- Replaced EV mNAV in the coverage model with an estimated net-mNAV bridge, including in-money conversion dilution and out-of-money claims.
- Added 20 quarters of cash charges, dated puts, issuance demand, fees, ATM consumption and common dilution. The first quarter is an October 16 stub.
- Added an optional STRC VWAP-band stress rule. The declared rate remains the default because subsequent issuer policy holds it near par. This is discretionary guidance, not automatic pricing.
- Added two native What-If Data Tables linked to model inputs. Portable formula grids remain available.
- Expanded the textbook to 16 chapters and added an accessible snapshot calculator, source links, tax/accounting/market-yield material and peer comparison.

## Dated result

At October 15 prices, using balance-sheet observations through October 11: annual cash charges are $1,559.7M, the $4,880M Reserve covers 37.5 months before principal, and reconstructed net mNAV is 1.175x. The 15.2-year static capacity result assumes sufficient demand to consume the $18,807.6M common ATM and excludes principal.

The Base path has no unmet financing need under its assumptions. The Severe case (BTC −70%, net mNAV 0.8x, STRC 15%, EUR/USD +10%) produces unmet funding needs. This is scenario arithmetic, not a probability or forecast. See [verification](docs/formula-verification.json).

## Verification and remaining work

Ten disposable input-change cases recalculated in LibreOffice 26.8 with no formula errors. Cash equations reconcile, the put schedule sums to $6,713.659M, the gate stops issuance, depleted ATM capacity produces unmet needs, and the optional rate rule responds at its boundaries. The exported XLSX contains two native Data Table definitions and four charts. Browser checks cover mobile layout, internal links and calculator changes.

**Still pending:** Microsoft Excel for Mac, a real recorded native Goal Seek run, Q3 filing refresh and Rahil’s reader responses. See [Excel review](docs/excel-review.md), [Q3 refresh](docs/q3-refresh.md) and [reader test](docs/reader-test.md). The November 10 draft remains blocked for refresh and native verification. No social post has been published.

Artifact Tool produced errors when changing native-table drivers after reimport. Independent LibreOffice recalculation was used for the behavior checks. Saved caches are not input-change evidence. A small metadata pass requests automatic full recalculation on opening in Excel.

## Use and rebuild

Start on Dashboard. Change blue inputs and the scenario selector. Read Quarterly path for principal and actual financing needs; snapshot coverage excludes principal. Negative cash is shown as an explicit unmet funding need. After the first unmet need, the path is a required-financing schedule rather than a continuing-solvency forecast.

The builders require Node and `@oai/artifact-tool` in the runtime. Dependencies are supplied by the artifact runtime and are not vendored. From this directory:

```sh
node model/build.mjs
python3 model/finalize.py
node model/check-calculator.mjs
node model/build-site.mjs
```

`model/template.xlsx` preserves the original layout and public input sources; the builder applies the v2 changes. Public textbook sources and licensed font assets are included. To verify with LibreOffice and openpyxl available, run `python3 model/test-libreoffice.py`; it uses a temporary directory and does not overwrite the deliverable.

## Limits

STRC and basic common shares are reconstructed; awards are anchored to Q2. Model FX is not a certified issuer Friday BFIX. The 1x issuance gate, demand coefficients, rate-band limits and put election assumptions are editable judgments. Snapshot sensitivities freeze observed moneyness; the quarterly path uses prior-period prices to avoid circular classification. It assumes no new preferreds or refinancing. Sources and observation dates are retained in Inputs and Net NAV.

This is an educational analysis from public information. It does not describe Strategy’s internal forecast or recommend a security.
