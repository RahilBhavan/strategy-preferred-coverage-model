"""Apply outline.json to the textbook source: chapter order, numbering and both tables of contents.

Idempotent. Run before model/build-site.mjs. Fails if a chapter file is missing or a section id is wrong.
"""
import json, re, pathlib, sys

SRC = pathlib.Path(__file__).parent
outline = json.loads((SRC / "outline.json").read_text())
tpl_path = SRC / "book.template.html"
tpl = tpl_path.read_text()

side, mobile, slots, n, letter = [], [], [], 0, ord("A")
labels, files = {}, []
for part in outline:
    side.append(f'  <span class="part">{part["part"]}</span>')
    for key, title in part["chapters"]:
        f = SRC / "ch" / f"{key}.html"
        if not f.exists():
            sys.exit(f"missing chapter file: {f}")
        body = f.read_text()
        if not re.search(rf'<section class="chapter" id="{key}"', body):
            sys.exit(f"{f.name}: section id must be {key}")
        if part.get("appendix"):
            label = f"Appendix {chr(letter)}"; num = chr(letter); letter += 1
        else:
            n += 1; label = f"Chapter {n}"; num = str(n)
        body = re.sub(r'(<span class="ch-num">)(?:Chapter \d+|Appendix [A-Z])', rf"\g<1>{label}", body, count=1)
        files.append((f, body))
        labels[key] = label
        side.append(f'  <a href="#{key}"><span>{num}</span>{title}</a>')
        mobile.append(f'<li><a href="#{key}">{title}</a></li>')
        slots.append(f"<!--{key.upper()}-->")

xref = re.compile(r'<a class="xref" href="#(\w+)">[^<]*</a>')
for f, body in files:
    def sub(m):
        if m.group(1) not in labels:
            sys.exit(f"{f.name}: cross-reference to unknown chapter {m.group(1)}")
        return f'<a class="xref" href="#{m.group(1)}">{labels[m.group(1)]}</a>'
    f.write_text(xref.sub(sub, body))

def between(text, start, end, inner):
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        sys.exit(f"template marker not found: {start!r}")
    return pat.sub(lambda _m: start + inner + end, text, count=1)

tpl = between(tpl, '<nav class="toc-side" aria-label="Contents">', "</nav>", "\n" + "\n".join(side) + "\n")
tpl = between(tpl, '<details class="toc-mobile"><summary>Contents</summary>\n<ol>', "</ol></details>", "\n" + "\n".join(mobile) + "\n")
tpl = between(tpl, '<div class="chapters">', "</div>\n</div>", "\n" + "\n".join(slots) + "\n")
tpl_path.write_text(tpl)
print(f"{n} chapters + {letter - ord('A')} appendices")
