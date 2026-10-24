"""Assemble the company textbook and course as one offline HTML document."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import base64
import html
import json
import re
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DEST = ROOT / 'verification-previews/Strategy_Company_and_Economics_Handbook.html'
spec = importlib.util.spec_from_file_location('course_renderer', HERE / 'build-course.py')
course = importlib.util.module_from_spec(spec)
spec.loader.exec_module(course)
OUTLINE = json.loads((ROOT / 'textbook-source/outline.json').read_text())

# These edits apply only to the consolidated edition, preserving historical sources.
EDITS = {
    'e1': [
        ('Strategy takes one asset, bitcoin, and sells different slices of it to different investors, each at the price that investor will pay. It makes money when the slices sell for more, in total, than the bitcoin behind them costs.',
         'Strategy holds bitcoin and issues securities with different payment rights, priorities and exposures. Issuing those securities raises financing and creates claims; it is not operating revenue. Whether a financing benefits existing common holders depends on price, fees, deployment, future payments, risk and the alternative.'),
        ('The converts are almost free in cash terms, which is exactly why they carry the put risk. The preferreds cost far more but never mature.',
         'A low coupon measures only current cash interest. Conversion options, fees and principal puts still matter. Preferreds have no scheduled maturity but can carry redemption or repurchase provisions.'),
    ],
    'n1': [
        ('<b>Break-even bitcoin growth:</b> roughly how fast bitcoin must rise for the trade to help common holders. For a preferred spent on bitcoin, it\'s about the yearly cost on cash raised.',
         '<b>Cash carry on proceeds:</b> annual payout divided by funds raised. This ratio is not a universal BTC return hurdle or full economic financing cost. Specify fees, payment dates, terminal claims and a counterfactual.'),
        ('Perpetual money: no repayment, ever', 'Funding with no scheduled maturity; redemption and holder repurchase rights must still be checked'),
        ('At $151 MSTR that option is worth about $15 against a $100 face, so today STRK is effectively a plain 8% preferred',
         'At the historical $151 MSTR price, immediate conversion parity is about $15 per STRK. That is not the embedded option\'s full value; time, volatility, credit and contractual rights matter'),
        ('That premium is the price of the option to skip',
         'The issue discount alone does not isolate the value of non-cumulative payment rights; credit, liquidity, demand and other terms also matter'),
        ('Strategy pays more cash for money that never has to be repaid.',
         'Different structures exchange different cash obligations, options and risks.'),
        ('Converts cost almost nothing yearly but come back as puts.',
         'A small coupon does not erase option cost or principal needs; puts and conversion depend on contract terms.'),
        ('Choosing between them is choosing which risk to hold.',
         'Compare full costs, payment timing and alternatives, rather than ranking securities by cash coupon alone.'),
        ('At 1.19x that\'s $0.84 per $1, so existing holders gain $0.16. At 0.8x it\'s $1.25, so they lose $0.25',
         'At a fixed 1.19x, the simplified asset amount associated with each dollar issued is about $0.84; at 0.8x it is $1.25. These are metric comparisons, not guaranteed shareholder profits. New shares, fees and actual use of proceeds determine the final per-share result'),
        ('That\'s the price of introducing a new kind of security to buyers who had never seen one.',
         'This is the difference between stated claims and gross proceeds, not an independently established explanation of investor motives or fair-value loss.'),
    ],
    'v1': [
        ('above 1.0x Strategy can fund itself with stock; below it, it can\'t.',
         'issuance above a defined net-asset metric can be accretive under fixed assumptions. Below-one issuance remains possible but can dilute that metric; actual execution depends on demand, price and policy.'),
        ('<b>A simple way to value it</b>Value = net assets × a multiple you believe is sustainable.',
         '<b>A price scenario rather than a valuation proof</b>Net assets times an assumed multiple gives a price scenario. Justifying that multiple requires a coherent valuation, investor-demand evidence and a feasible financing counterfactual.'),
    ],
}
NOTES = {
    'e1': 'Financing receipts are not revenue. Investor categories here are analytical possibilities. Preferred holders do not automatically own or hold a lien on BTC. Cash carry, per-share accretion and economic value are three different tests.',
    'n1': 'The product prices and rates below retain their historical dates. Cash-carry ratios do not price the full security. Perpetual status does not remove redemption or repurchase rights; conversion parity is not full option value.',
    'v1': 'A premium multiple is an assumption requiring evidence. A local leverage calculation is not a market-return forecast. Do not deduct both preferred market value and the present value of the same distributions.',
    'ch6': 'Separate a dated STRC rate declaration, historical guidance and contractual authority. A higher declared rate does not guarantee a particular market price. Model stress resets are assumptions.',
    'ch8': 'Reproduce the issuer definition applicable on the observation date. Gross BTC/share, net BTC/share and economic value/share differ. Do not count the same note as both deducted principal and conversion shares in an alternative-treatment metric.',
    'k1': 'Asset coverage is not pledged collateral or a guaranteed recovery. Rights, other liabilities, realization costs and legal process matter.',
    's1': 'These are assumed paths, not forecasts. A cash shortfall is separate from an asset-coverage threshold. After a first unmet payment the schedule is a funding diagnostic, not proof of continuing solvency.',
    'ch15': 'Unrealized value changes do not fund cash payments. Separate issuer cash/accounting from holder tax classification, and verify jurisdiction and reporting period.',
}


def chapter(key):
    text = (ROOT / 'textbook-source/ch' / (key + '.html')).read_text()
    if key == 'ch11':
        compiled = (ROOT / 'site/textbook.html').read_text()
        widget = re.search(r'<figure class="figure" id="calculator">.*?</figure>', compiled, re.S)
        assert widget, 'Compiled textbook calculator missing'
        text = text.rsplit('</section>', 1)[0] + widget[0] + '</section>'
    for old, new in EDITS.get(key, []):
        assert old in text, (key, old)
        text = text.replace(old, new)
    if key == 'e1':
        start = text.index('<h3>The hurdle bitcoin has to clear</h3>')
        stop = text.index('<h3>', start + 6)
        text = text[:start] + '''<h3>Cash carry and economic return answer different questions</h3>
        <div class="prose"><p>Using the historical illustration, annual charges of about $1.56 billion divided by $69.7 billion of BTC equal about 2.2%. This is a cash-charge-to-asset ratio, not proof that 2.2% BTC appreciation makes common holders economically better off or supplies payment cash.</p>
        <p>A hypothetical $1 billion raised at par with a 12% annual payout produces a $120 million annual payment before fees. The payout divided by proceeds is cash carry. A full economic analysis also needs the issue discount, fees, timing, terminal claim, payout funding and an alternative. Lesson 2 and the worked problems derive explicit one-year examples.</p></div>\n''' + text[stop:]
        text = text.replace('Why is the 2.2% hurdle so much lower than STRC\'s 12%?',
                            'Why do the 2.2% and 12% cash ratios differ?')
    if key == 'n1':
        text = text.replace('<dt>Break-even</dt><dd>Bitcoin ≈ +',
                            '<dt>Cash carry</dt><dd>Annual payout / gross proceeds: ')
    if key in NOTES:
        note = '<div class="editor-note"><b>Reading qualification</b><p>' + html.escape(NOTES[key]) + '</p><a href="#course-sources">Source and correction guide</a></div>'
        text = re.sub(r'(</h2>)', lambda m: m[0] + note, text, count=1)
    return text


def course_section(key):
    text = (HERE / (key + '.md')).read_text()
    # Remove obsolete directions that describe the separate multi-page delivery.
    if key == 'README':
        text = '\n'.join(l for l in text.splitlines() if not l.startswith('[Verification and delivery limits]'))
        text = text.replace('Later units use assigned sections of the existing 30-chapter textbook',
                            'Later units use assigned sections of the 30 company chapters included below')
    body = course.markdown(text)
    body = re.sub(r'<(/?)h([1-4])>', lambda m: f'<{m[1]}h{int(m[2])+1}>', body)
    return f'<section class="chapter course" id="course-{key}">{body}</section>'


def rewrite_links(text):
    def change(m):
        link = html.unescape(m[1])
        if link.startswith('textbook.html#'):
            link = '#' + link.split('#', 1)[1]
        elif link in ['index.html', 'textbook.html']:
            link = '#course-README' if link == 'index.html' else '#f1'
        elif link == 'economic-plan-source-check.html':
            link = '#source-review'
        elif link == 'verification.html':
            link = '#document-status'
        elif link.endswith('.html') and link[:-5] in course.ORDER:
            link = '#course-' + link[:-5]
        if Path(link).name == 'Strategy_Preferred_Coverage_Model.xlsx':
            encoded = base64.b64encode((ROOT / 'Strategy_Preferred_Coverage_Model.xlsx').read_bytes()).decode()
            return 'href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,' + encoded + '" download="Strategy_Preferred_Coverage_Model.xlsx"'
        return 'href="' + html.escape(link, quote=True) + '"'
    return re.sub(r'href="([^"]*)"', change, text)


class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.dependencies, self.headings = [], [], [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag in ['script', 'img', 'link', 'iframe']:
            for attr in ['src', 'href']:
                if attr in a and not a[attr].startswith('data:'):
                    self.dependencies.append(a[attr])
        self.headings += tag == 'h1'


def build():
    sections, contents = [], []

    def group(title, entries):
        contents.append('<h3>' + html.escape(title) + '</h3><ol>' + ''.join(
            f'<li><a href="#{key}">{html.escape(label)}</a></li>' for key, label in entries) + '</ol>')

    first = ['README', 'diagnostic', 'sources']
    group('Start here', [('course-' + k, (HERE / (k + '.md')).read_text().splitlines()[0][2:]) for k in first])
    sections.extend(course_section(k) for k in first)
    lessons = ['lesson-' + str(i) for i in range(1, 5)]
    group('Finance lessons', [('course-' + k, (HERE / (k + '.md')).read_text().splitlines()[0][2:]) for k in lessons])
    sections.extend(course_section(k) for k in lessons)
    for part in OUTLINE:
        if part.get('appendix'):
            continue
        group(part['part'], part['chapters'])
        sections.extend(chapter(k) for k, title in part['chapters'])
    work = ['excel-labs', 'problem-sets', 'assessments', 'solutions', 'solutions-exams']
    group('Practice and assessment', [('course-' + k, (HERE / (k + '.md')).read_text().splitlines()[0][2:]) for k in work])
    for key in work:
        block = course_section(key)
        if key.startswith('solutions'):
            # Keep the anchor outside the disclosure so direct links reach it.
            block = block.replace(f'id="course-{key}"', '')
            block = f'<details id="course-{key}" class="answers"><summary>Open {html.escape(key.replace("-", " "))} after your attempt</summary>{block}</details>'
        sections.append(block)
    appendix = OUTLINE[-1]['chapters']
    group('Reference appendices', appendix + [['source-review', 'Bounded primary source review'], ['document-status', 'Edition and learning status']])
    sections.extend(chapter(k) for k, title in appendix)
    memo = course.markdown((ROOT / 'docs/economic-plan-source-check.md').read_text())
    memo = re.sub(r'<(/?)h([1-4])>', lambda m: f'<{m[1]}h{int(m[2])+1}>', memo)
    sections.append('<section class="chapter" id="source-review">' + memo + '</section>')
    sections.append('''<section class="chapter" id="document-status"><h2>Edition and learning status</h2>
    <p>Consolidated October 24, 2026. Company snapshot figures keep their original October 11–15 or other stated dates. The source review and course were prepared October 23. This edition does not refresh balances, quotes, declared rates or contract amendments.</p>
    <p>All 30 company chapters, three reference appendices and the twelve course readings are included. The original Excel workbook is embedded as a download. Its formulas remain in Excel; lab briefs are learning assignments rather than completed models.</p>
    <p>The course has independent arithmetic and navigation checks. Native Excel verification and your diagnostic, reader responses, exams and capstone remain unassessed. A self-study course is not an accredited degree. Corrected passages and adjacent reading qualifications take precedence over historical shorthand.</p></section>''')
    old = (ROOT / 'site/textbook.html').read_text()
    styles = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', old, re.S))
    scripts = '\n'.join(re.findall(r'<script[^>]*>(.*?)</script>', old, re.S))
    styles += '''
    .handbook{max-width:1100px}.handbook .chapter{padding:44px 0}.handbook .course{max-width:78ch}
    .handbook .course h3{font:600 25px/1.3 'Rahil Plex',sans-serif;text-transform:none;margin-top:38px}
    .handbook .course h4{font:600 20px/1.4 'Rahil Plex',sans-serif;text-transform:none}
    .handbook p,.handbook li{overflow-wrap:anywhere}.handbook li{margin-bottom:10px}
    .handbook-toc{columns:2;column-gap:56px;margin:32px 0}.handbook-toc h3{break-after:avoid;font-size:24px}
    .handbook-toc ol{padding-left:22px;font-size:16px}.handbook-toc li{break-inside:avoid}
    .editor-note{border-left:3px solid var(--color-accent);background:var(--color-surface);padding:18px 22px;margin:28px 0;font-size:16px;max-width:78ch}
    .editor-note p{margin:8px 0}.answers{margin:48px 0}.answers>summary{font-size:22px}
    .handbook .hero h1{max-width:20ch}.handbook .chapter>h2{scroll-margin-top:20px}
    .handbook-tools{display:flex;flex-wrap:wrap;gap:16px;padding:16px 0;font-size:16px}
    @media(max-width:680px){.handbook-toc{columns:1}.handbook{padding-left:20px;padding-right:20px}.handbook .hero h1{font-size:48px}.handbook .course h3{font-size:23px}}
    @media print{html,body{background:white!important;color:#111!important}.handbook{max-width:none}
    .handbook-tools{display:none}.chapter{break-before:page}.editor-note{border-color:#555;background:#eee;color:#111}
    .handbook a{color:inherit}.handbook-toc{columns:2}.handbook p,.handbook li{orphans:3;widows:3}}
    '''
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Strategy Company and Economics Handbook</title><style>{styles}</style></head><body>
    <a class="skip" href="#main">Skip to contents</a><main class="page handbook" id="top">
    <section class="hero"><p class="issue-line">A student trynna learn · Consolidated edition · October 24, 2026</p>
    <h1>Strategy Company and Economics Handbook</h1>
    <p class="lede-big">Understand the company, its bitcoin strategy, software business, securities, financing decisions, cash obligations, valuation and risks. Then use the included finance course and Excel exercises to test your own reasoning.</p>
    <p>Read it straight through or follow the sixteen-unit syllabus. Company chapters retain their historical numbering; the new finance lessons and assessments are separate sections in this same document. Use the contents links or your browser's Find command.</p>
    <div class="editor-note"><b>Read dates and assumptions with every figure.</b><p>Company figures retain their original observation dates. Hypothetical exercises are labelled. This is an educational handbook, not a current valuation. Read the source guide before applying historical examples to today's company.</p></div>
    <div class="handbook-tools"><a href="#course-README">Study route</a><a href="#course-diagnostic">Take the diagnostic</a><a href="#ch1">Company overview</a><a href="Strategy_Preferred_Coverage_Model.xlsx">Download embedded Excel workbook</a><button id="print-handbook" type="button">Print the full document</button></div></section>
    <section id="main"><h2>Contents</h2><nav class="handbook-toc" aria-label="Document contents">{''.join(contents)}</nav></section>
    {''.join(sections)}<footer class="footer"><a href="#top">Back to the beginning</a> · Independent self-study · Human understanding remains unassessed</footer></main>
    <script>{scripts}</script><script>
    let previouslyOpen=[];window.addEventListener('beforeprint',()=>{{previouslyOpen=[...document.querySelectorAll('details')].map(d=>[d,d.open]);previouslyOpen.forEach(([d])=>d.open=true)}});
    window.addEventListener('afterprint',()=>previouslyOpen.forEach(([d,open])=>d.open=open));
    document.getElementById('print-handbook').addEventListener('click',()=>window.print());
    document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{{const d=document.getElementById(decodeURIComponent(a.hash.slice(1)));if(d&&d.tagName==='DETAILS')d.open=true}}));
    </script></body></html>'''
    doc = rewrite_links(doc)
    audit = Audit()
    audit.feed(doc)
    assert audit.headings == 1
    assert {'btc-input', 'mnav-input', 'rate-input', 'calc-reset'} <= set(audit.ids)
    assert len(audit.ids) == len(set(audit.ids)), 'Duplicate section IDs'
    assert not audit.dependencies, audit.dependencies
    for link in audit.links:
        url = urlsplit(link)
        if url.scheme:
            continue
        assert not url.path, ('Non-contained link', link)
        assert unquote(url.fragment) in audit.ids, ('Missing anchor', link)
    assert 'no repayment, ever' not in chapter('n1')
    assert "below it, it can't" not in chapter('v1')
    assert 'that option is worth about $15' not in chapter('n1')
    DEST.parent.mkdir(exist_ok=True, parents=True)
    DEST.write_text(doc)
    print(json.dumps({'output': str(DEST), 'bytes': DEST.stat().st_size,
                      'company_chapters': 30, 'course_documents': len(course.ORDER),
                      'anchors': len(audit.ids), 'links_checked': len(audit.links),
                      'runtime_dependencies': audit.dependencies}, indent=2))


if __name__ == '__main__':
    build()
