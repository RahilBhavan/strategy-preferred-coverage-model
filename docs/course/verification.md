# Course verification and limits

October 23, 2026. This concerns the new learning materials, not a refreshed valuation or a completed student assessment.

## Delivered

Sixteen units, four original foundation lessons, ten diagnostic questions, 24 problem-set questions, sixteen Excel lab briefs, two exams and a two-part capstone. Worked answers are separate. Twelve substantive Markdown documents total about 13,500 words, excluding scripts and this report.

The local reader builds fifteen HTML pages, including this report, the legacy textbook with a correction notice and the bounded source-check memo. It copies the existing Excel workbook for reference. The course map is saved separately as course-map.html for inline display. The builder does not alter the workbook or publish the course.

## Checks exercised

Run the builder, then verify-course.py. The final check produced **473 arithmetic and local-navigation checks passed**. It covers bond PV, issuance effects, compounding, timing-limited financing and ten distinct capstone action/deployment/stress combinations. Each capstone path checks interest and dated BTC sales. It also checks question/lab/unit counts, grade weights, local link destinations and textbook anchors. External availability and every legacy textbook number are outside this check.

DOM/JavaScript execution exercised all four course-map buttons: each displayed four units, selected one stage and began at unit 01, 05, 09 or 13. The reader DOM had its expected title, one main heading and twelve navigation links. Raw results: [browser-checks.json](browser-checks.json).

The collaborative preview had no automation-capable tab. Opening returned “Too many server browser tabs are open. Close one with t3_preview_close, or reuse a tabId from preview_status tabs.” There was no tab owned by this task to close. Screenshot preview returned “Headless Chrome could not render the page: the page did not finish loading within 20 seconds.”

Fallback DOM execution succeeded but reported zero viewport width. It supports JavaScript/navigation assertions only. **Screenshot inspection, responsive overflow/contrast measurement and a visual five-second test remain unverified.** No real-reader success is claimed.

## Remaining work belongs to the learning process

Labs are instructions to build and exercise Excel models, not sixteen completed workbooks. No native Excel session, Data Table, Goal Seek or Mac behavior was verified by this authoring work. Existing workbook gates remain separate.

Your diagnostic, reader explanations, problems, exams and capstone are **not assessed**. Software checks establish internal arithmetic/navigation consistency, not learning. Submit your own first attempt to begin the human feedback loop.

Current quotes, outstanding balances, rates and later amendments need their own dated refresh before live-company decisions. The historical textbook has not become current evidence merely by inclusion here.
