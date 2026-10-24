# Strategy economics: a complete study course

Version 1, October 23, 2026. This replaces the topic-only plan with a course you can work through. It is an independently authored study course, not an accredited degree or an MIT course.

[Verification and delivery limits](verification.md) records what was checked and remains unassessed. Build a local browser reader with `python3 docs/course/build-course.py`; its entry is `verification-previews/course/index.html` from the project root. The Markdown files remain the editable course source.

## Start here

1. Take [the diagnostic](diagnostic.md), closed book. It takes about 25–35 minutes.
2. Read [Lesson 1: assets, claims and cash](lesson-1.md).
3. Complete Lab 1 and Problem Set A before opening the solutions.
4. Use the 16 units below as the route through the existing textbook and the new lessons.

The workload estimate is **16 units × 7 hours = 112 hours**. Treat one unit as a week if that suits you. This is a planning assumption, not a measured completion time. No calendar events are created. Units can take longer, and a unit is complete only when you pass its check.

Each unit: about two hours of reading/lecture, two hours in Excel, one hour solving problems, one hour of closed-book retrieval, and one hour on a company case. Exam and capstone work replace those activities in the relevant units.

## What completing this should let you do

- Reconcile a transaction across assets, claims, shares, cash and accounting income.
- Explain why each investor would choose a particular security over direct BTC or a fund.
- Price basic cash flows and distinguish cash cost, option cost, credit risk and required return.
- Reconstruct gross and net bitcoin-per-share measures without double-counting conversions.
- Build a dated financing schedule with puts, distributions, fees, FX and limited capital access.
- Separate a per-share improvement from liquidity improvement and economic value creation.
- Defend an allocation decision against explicit alternatives using contemporaneous evidence.

Learning status is initially **not assessed**. Reading the files, passing software checks or receiving an agent explanation does not establish these abilities.

## What is already included

Four new foundation lessons, a 10-question diagnostic, four six-question problem sets, 16 Excel lab briefs, a midterm, a final, a capstone and separate worked solutions. Later units use assigned sections of the existing 30-chapter textbook and primary documents; they are not represented as 16 newly written lectures.

- [Lesson 1: assets, claims and cash](lesson-1.md)
- [Lesson 2: time, price and financing cost](lesson-2.md)
- [Lesson 3: risk, sequence and liquidity](lesson-3.md)
- [Lesson 4: claims, optionality and capital structure](lesson-4.md)
- [Problem sets A–D](problem-sets.md)
- [Excel labs 1–16](excel-labs.md)
- [Midterm, final and capstone](assessments.md)
- [Answer key](solutions.md), open only after attempting the questions
- [Source and textbook correction guide](sources.md)

## The 16-unit syllabus

### Stage I. The finance underneath Strategy

**1. Assets, claims and the cash account.** No finance prerequisite. Read Lesson 1 and textbook `f1`, `ch4`, `ch7`. Rebuild the opening balance sheet and classify every transaction in Lab 1. Pass when cash and total claims reconcile and you can explain why financing receipts are not revenue. Submit A1–A2.

**2. Time value, yield and present value.** Requires Unit 1 and percentage arithmetic. Read Lesson 2 and selected MIT Finance Theory I “Present Value Relations” and “Fixed-Income Securities.” Build Lab 2. Pass when you can price dated payments and explain the assumptions behind a perpetuity. Submit A3–A4.

**3. Risk, compounding and path dependence.** Requires Units 1–2. Read Lesson 3 and MIT “Risk and Return” selections. Build Lab 3. Pass when you can explain why the same ending BTC price can leave different remaining holdings. Submit A5–A6. Review Set A against the key.

**4. Bitcoin economics and the corporate wrapper.** Requires Units 1–3. Read textbook `f2`, `ch1`, `ch16` and Bitcoin Developer Guide sections on transactions, wallets and mining. Build Lab 4. Explain supply rules, custody, market demand and why scarcity does not determine price. Compare direct BTC, a fund and MSTR on matched assumptions. Gate I: all Set A errors corrected, at least 80% on a fresh variant, no confusion between income and financing.

### Stage II. What each security sells

**5. Common issuance and the denominator.** Requires Gate I. Read textbook `ch3`, `ch8`, `ch12` with the correction guide. Build Lab 5. Derive per-share accretion from assets, claims and new shares. Identify how the use of proceeds changes the answer. Submit B1–B2.

**6. Preferred stock and the price of a promise.** Requires Units 2 and 5. Read Lesson 4, textbook `ch5`, `t1`, `n1`. Build Lab 6. Distinguish stated amount, proceeds, market value, cumulative rights, legal payment constraints and redemption. Submit B3–B4. Do not treat the textbook's “break-even BTC growth” shortcut as a general valuation rule.

**7. Convertibles, options and volatility.** Requires Units 2–3 and 6. Read Lesson 4, MIT “Options” introduction and the issuer debt note. Build Lab 7. Draw payoffs and identify when a simple terminal payoff model does not represent actual exercise/settlement terms. Submit B5–B6. Know the difference between conversion parity, intrinsic value and option value.

**8. Who buys these instruments, and why?** Requires Units 5–7. Read textbook `e1`, `n1` with the correction guide. Complete Lab 8's investor-choice memo. Treat mandate, tax and hedging explanations as hypotheses until evidenced. Take the midterm. Gate II: at least 80%, every critical concept corrected, and one unseen issuance example solved without the key.

### Stage III. Can the company keep paying?

**9. Stock-flow consistent treasury planning.** Requires Gate II. Read textbook `ch7`, `n5`, `ch11`. Build Lab 9, using the existing model as a reference only after building your own cash roll-forward. Submit C1–C2. A negative balance must remain an unmet financing need, not an invisible plug.

**10. STRC resets, duration and market demand.** Requires Units 2, 6 and 9. Read textbook `ch6`, `n4` and dated issuer announcements. Build Lab 10. Separate historic guidance, current declared rates and contractual authority. Analyze the cash cost of a reset without assuming it restores the market price. Submit C3–C4.

**11. Currency, taxes and accounting.** Requires Units 1–2 and 9. Read textbook `ch15` and filing notes. Build Lab 11. Translate STRE payouts, distinguish revenue from free cash flow, and explain fair-value income versus cash. Treat return-of-capital reporting as a holder-tax matter. Submit C5–C6.

**12. The financing feedback loop.** Requires Units 5–11. Read textbook `s1`, `ch9`, `v1`. Build Lab 12. Model BTC, premium and demand jointly, with an explicit no-financing case. Identify the first payment shortfall. Gate III: at least 80% on Set C and a reconciled cash schedule under both ordinary and adverse assumptions.

### Stage IV. Value, control and capital allocation

**13. Capital structure and economic value.** Requires Gate III. Read MIT Finance Theory II “Capital Structure” and “Informational and Dynamic Considerations,” plus textbook `v1` with the correction guide. Build Lab 13. Use a frictionless benchmark before adding taxes, distress, investor constraints and information. Explain why changing claim labels alone does not manufacture asset cash flows. Submit D1–D2.

**14. Software, franchise value and the premium.** Requires Units 2, 8 and 13. Read textbook `ch15`, `v1`, `ch16`, filing segment information and MIT “Valuation of Free Cash Flows.” Build Lab 14. Value software separately under stated assumptions, then analyze the financing franchise without counting future issuance accretion twice. Submit D3–D4.

**15. Governance and decisions in historical context.** Requires Units 8–14. Read textbook `g1`, `d1`, `n2`, `n3`, `n4` and contemporaneous documents. Build Lab 15. Separate stated rationale, analyst inference and later outcome. Explain distributional conflicts between common, preferred, debt and management. Submit D5–D6.

**16. Investment committee.** Requires corrected Sets A–D and Gates I–III. Complete Lab 16, final exam and capstone. Defend a financing/allocation recommendation for the hypothetical committee case, with a credible alternative and a disconfirming test. This is an academic corporate decision exercise, not a personal trading recommendation.

## Assessment and progression

Proposed grade weights: four problem sets, 10% each; midterm 20%; final 15%; capstone 20%; oral defense 5%. Total 100%. These are learning standards, not institution-issued grades.

For each six-question set, score each question out of five: method 2, arithmetic/logic 2, units and assumptions 1. The key gives result anchors. A self-mark is provisional; keep the raw attempt and request review if the reasoning is uncertain. An essay with a plausible conclusion but no evidence does not receive full marks.

Critical errors override a numerical passing grade until corrected: treating unrealized gains as spendable cash; counting financing as operating revenue; double-counting converted debt; treating ATM capacity as promised funding; treating a per-share metric as proof of economic value; claiming a legal right without its source.

After a missed check: record the wrong claim, identify its cause, read the relevant worked lesson, solve a changed example, and explain why the earlier answer failed. Repeat the key question after roughly two days and again after a week. Those are suggested retrieval intervals, not calendar commitments.

## How to use an assistant as a tutor

Bring your attempt first. Ask: “Grade this against the rubric. Identify my first incorrect step. Give one hint, not the answer.” After revising, ask for a new example with different numbers. Finally, teach the result back in plain language.

Use an assistant to challenge assumptions and locate primary documents. Do not use its polished explanation as evidence that you could produce the reasoning yourself. For unsourced claims, record “unknown” and name the document needed.

## The first session

Take the diagnostic, read Lesson 1, and build Lab 1 in Excel. Write a 150-word explanation of why a company can report a gain while losing payment capacity. Save the untouched first attempt before checking the key. This session supplies the baseline for deciding which foundations you need.
