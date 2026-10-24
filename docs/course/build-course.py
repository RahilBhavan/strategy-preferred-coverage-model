"""Build a local, offline course reader; finance labs remain Excel exercises."""
from pathlib import Path
import argparse
import base64
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent
ORDER = ["README", "diagnostic", "lesson-1", "lesson-2", "lesson-3", "lesson-4",
         "problem-sets", "excel-labs", "assessments", "sources", "solutions", "solutions-exams"]
BOOK_IDS = {c[0] for part in json.loads((ROOT / "textbook-source/outline.json").read_text())
            for c in part["chapters"]}


def target(link):
    if link == "../economic-plan-source-check.md":
        return "economic-plan-source-check.html"
    if link.endswith(".md"):
        return "index.html" if link == "README.md" else link[:-3] + ".html"
    return link


def inline(raw):
    # Only the course's small Markdown vocabulary is supported. Escape all raw HTML.
    tokens = []

    def keep(value):
        tokens.append(value)
        return f"\x00{len(tokens) - 1}\x00"

    raw = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: keep(
        '<a href="' + html.escape(target(m[2]), quote=True) + '">' +
        html.escape(m[1]) + '</a>'), raw)
    raw = re.sub(r"`([^`]+)`", lambda m: keep(
        f'<a href="textbook.html#{m[1]}"><code>{m[1]}</code></a>'
        if m[1] in BOOK_IDS else '<code>' + html.escape(m[1]) + '</code>'), raw)
    raw = html.escape(raw)
    raw = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", raw)
    for i, token in enumerate(tokens):
        raw = raw.replace(f"\x00{i}\x00", token)
    return raw


def markdown(raw):
    out, paragraph, list_type = [], [], None

    def flush():
        if paragraph:
            out.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()

    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f'</{list_type}>')
            list_type = None

    for line in raw.splitlines() + ['']:
        if not line.strip():
            flush()
            close_list()
            continue
        heading = re.match(r'^(#{1,4}) (.+)', line)
        item = re.match(r'^(?:([-]) |(\d+)\. )(.+)', line)
        if heading:
            flush()
            close_list()
            level = len(heading[1])
            out.append(f'<h{level}>' + inline(heading[2]) + f'</h{level}>')
        elif item:
            flush()
            kind = 'ul' if item[1] else 'ol'
            if list_type != kind:
                close_list()
                list_type = kind
                out.append(f'<{kind}>')
            out.append('<li>' + inline(item[3]) + '</li>')
        else:
            close_list()
            paragraph.append(line.strip())
    return '\n'.join(out)


def build(output):
    output.mkdir(parents=True, exist_ok=True)
    fonts = ''
    for name, file in [('CourseDisplay', 'Anton-Regular.ttf'),
                       ('CourseText', 'IBMPlexSans-Regular.ttf')]:
        encoded = base64.b64encode((ROOT / 'assets/fonts' / file).read_bytes()).decode()
        fonts += f"@font-face{{font-family:{name};src:url(data:font/ttf;base64,{encoded})}}"
    css = fonts + '''
    *{box-sizing:border-box}body{margin:0;background:#151515;color:#eee;
    font:18px/1.65 CourseText,Arial,sans-serif}a{color:#ffe047;text-underline-offset:4px}
    a:focus-visible{outline:3px solid #ffe047;outline-offset:4px}header{padding:22px 5%;
    border-bottom:1px solid #555;font-size:15px}header a{margin-right:24px}
    .layout{display:grid;grid-template-columns:230px minmax(0,800px);gap:48px;
    max-width:1180px;margin:auto;padding:40px 24px}aside{font-size:15px}aside a{
    display:block;padding:7px 0}aside .current{color:#fff;font-weight:bold}
    main{min-width:0}h1{font:clamp(38px,6vw,66px)/1.12 CourseDisplay,Arial,sans-serif;
    font-weight:400;letter-spacing:.2px;margin:0 0 32px}h2{font-size:28px;line-height:1.25;
    margin-top:48px}h3{font-size:22px;margin-top:32px}p,li{overflow-wrap:anywhere}
    li{margin:12px 0}strong{font-weight:bold;color:#fff}code{font-size:.9em}
    .notice{border-left:3px solid #ffe047;padding:14px 18px;background:#242424;
    font-size:15px;margin-bottom:32px}footer{margin-top:56px;padding-top:24px;
    border-top:1px solid #555;font-size:15px;color:#ccc}
    @media(max-width:760px){.layout{display:block;padding:28px 20px}aside{margin-bottom:32px;
    display:flex;gap:4px 20px;flex-wrap:wrap}aside a{padding:5px 0}body{font-size:17px}}
    @media print{body{background:white;color:black}aside,header,.notice{display:none}
    .layout{display:block;max-width:none;padding:0}a,strong{color:black}h1{font-size:36px}
    h2{break-after:avoid}p,li{orphans:3;widows:3}}
    '''
    names = {key: (SOURCE / (key + '.md')).read_text().splitlines()[0][2:] for key in ORDER}
    for key in ORDER + ['economic-plan-source-check', 'verification']:
        source = SOURCE / (key + '.md')
        if not source.exists():
            source = ROOT / 'docs' / (key + '.md')
        title = source.read_text().splitlines()[0][2:]
        nav = ''.join(f'<a class="{"current" if k == key else ""}" href="'
                      f'{"index" if k == "README" else k}.html">{html.escape(names[k])}</a>'
                      for k in ORDER)
        notice = ('Answer key: preserve your first attempt before reading.' if key.startswith('solutions')
                  else 'Study status: not yet assessed. The existing textbook requires the source/correction guide.')
        content = f'''<!doctype html><html lang="en"><meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>{html.escape(title)}</title><style>{css}</style>
        <header><a href="index.html">Strategy economics / course</a>
        <a href="textbook.html">Companion textbook</a><a href="Strategy_Preferred_Coverage_Model.xlsx">Existing Excel model</a></header>
        <div class="layout"><aside aria-label="Course navigation">{nav}</aside><main>
        <div class="notice">{notice} <a href="sources.html">Read the guide</a>.</div>
        {markdown(source.read_text())}<footer>Independent self-study · Version 1 · October 23, 2026.
        Hypothetical exercises are separate from actual-company evidence. No accredited qualification.</footer>
        </main></div></html>'''
        (output / ('index.html' if key == 'README' else key + '.html')).write_text(content)
    textbook = (ROOT / 'site/textbook.html').read_text()
    alert = '''<div style="position:relative;z-index:99999;padding:20px;background:#fff2af;color:#151515;font:16px/1.5 Arial,sans-serif">
    Legacy companion textbook: read the <a style="color:#151515;text-decoration:underline" href="sources.html">course corrections</a>
    before relying on its financing, valuation or legal shortcuts. Historical balances are not refreshed.
    <a style="color:#151515;text-decoration:underline" href="index.html">Return to the course</a>.</div>'''
    textbook = re.sub(r'(<body[^>]*>)', lambda m: m[0] + alert, textbook, count=1)
    (output / 'textbook.html').write_text(textbook)
    shutil.copy2(ROOT / 'Strategy_Preferred_Coverage_Model.xlsx', output)
    shutil.copy2(SOURCE / 'browser-checks.json', output)
    print(f'Built {len(ORDER) + 3} reader pages and copied existing Excel model into {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'verification-previews/course')
    build(parser.parse_args().output.resolve())
