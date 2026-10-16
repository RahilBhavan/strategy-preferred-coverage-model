# Improvement checklist, October 16, 2026

| Original item | Result |
|---|---|
| 1. Net mNAV | Implemented. Net NAV bridge uses conversion prices, dated awards and estimated basic shares. The 1x gate remains an assumption. |
| 2. Open in Excel | Pending Mac access. Exact checks and editable receipts prepared. |
| 3. Sourcing | Overclaim removed; chapter links added. Timeline context remains labelled as not independently reverified in full. |
| 4. Q3 counts | Pending release/access to Q3 filing. Refresh procedure prevents duplicate roll-forwards. |
| 5. Five-year stress | Implemented 20-quarter path with correlated premium sensitivity, demand scaling, puts, fees, dilution and ATM consumption. Coefficients are assumptions. |
| 6. STRC rate rule | Optional VWAP-based illustration implemented and boundary-tested. Declared rate stays default because current hold policy supersedes older bands. |
| 7. Convertible puts | Conversion prices, actual put dates, moneyness indicator and cash needs implemented. Full cash puts are the default; no automatic conversion is assumed. |
| 8. Data Tables / Goal Seek | Two native Data Tables authored and independently recalculated. Native Excel behavior and a recorded native Goal Seek run remain pending. Analytical target and exact exercise prepared. |
| 9. Missing textbook topics | Market yields, ROC, fair-value accounting, software scale and peer mechanisms added. Yield examples are labelled illustrations, not fresh quotes. |
| 10. Calculator | Implemented in textbook and project page; snapshot equations match the workbook. Principal and fees are excluded and labelled. |
| 11. Reader test | Protocol prepared; Rahil volunteered. Responses and follow-up revision remain pending. |
| 12. Public repo/site | Packaged for GitHub and GitHub Pages. Deployment result is recorded separately. |
| 13. Nov 10 post | Draft and replacement fields prepared. Dated October rehearsal passes preflight; November version remains blocked on Q3 and native Excel receipts. Nothing posted to X. |

The prior assertion that mNAV alone “decides coverage” is replaced by a conditional explanation. The snapshot is dominated by an assumed gate and registered capacity. The dated path measures when those assumptions cease to fund cash needs.
