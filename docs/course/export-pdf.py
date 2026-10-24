"""Print the consolidated handbook with WeasyPrint; attach its Excel reference.

Dependencies: weasyprint and pypdf. This exports content; it does not run Excel.
"""
from pathlib import Path
import argparse
import re
from weasyprint import HTML, CSS
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[2]
PRINT_CSS = '''
@page { size: A4; margin: 18mm 16mm 20mm;
 @bottom-left { content: "Strategy Company and Economics Handbook"; font: 8pt sans-serif; color: #555; }
 @bottom-right { content: counter(page) " / " counter(pages); font: 8pt sans-serif; color: #555; }
}
:root { --color-canvas: #fff !important; --color-ink: #161616 !important; --color-secondary: #444 !important;
 --color-surface: #f1f1ed !important; --color-border: #bbb !important; --color-accent: #ffe047 !important; }
html,body { background: white !important; color: #161616 !important; font-size: 10.5pt !important; line-height: 1.5 !important; }
.page.handbook { width: auto !important; max-width: none !important; padding: 0 !important; }
.handbook .hero { padding: 12mm 0 8mm; }
.handbook .hero h1 { font-size: 38pt !important; max-width: 18ch; line-height: 1.15; }
h2 { font-size: 27pt !important; line-height: 1.15; break-after: avoid; }
h3,.handbook .course h3 { font-size: 17pt !important; line-height: 1.3; break-after: avoid; }
h4,.handbook .course h4 { font-size: 12pt !important; line-height: 1.35; break-after: avoid; }
p,li { orphans: 3; widows: 3; }
.handbook .chapter { padding: 6mm 0 0 !important; break-before: page; }
.handbook .course { max-width: none; }
.handbook-toc { columns: 2; column-gap: 9mm; }
.handbook-toc h3 { font-size: 13pt !important; }
.handbook-toc ol { font-size: 9pt; }
.handbook-tools,.skip,input,button,noscript { display: none !important; }
.editor-note { padding: 4mm !important; margin: 5mm 0 !important; font-size: 9.5pt !important; border-color: #555 !important; }
.lede-big { font-size: 13pt !important; line-height: 1.5; }
.figure { padding: 4mm !important; margin: 5mm 0 !important; break-inside: avoid; }
.figure h4 { font-size: 12pt !important; }
.fl,figcaption,.meta,.sources,.check,.key { font-size: 9pt !important; line-height: 1.5; }
.card { padding: 4mm !important; break-inside: avoid; }
.card .tk { font-size: 25pt; }
.card dl>div { grid-template-columns: 22mm minmax(0,1fr); font-size: 9pt; }
.card dt { font-size: 8pt; }
.cards { gap: 4mm; }
table { font-size: 9pt !important; min-width: 0 !important; }
th { font-size: 8pt !important; } td,th { padding: 2mm !important; }
tr { break-inside: avoid; } thead { display: table-header-group; }
.formula { white-space: pre-wrap !important; overflow-wrap: anywhere; font-size: 9pt !important; }
.cols3 { gap: 2mm; grid-template-columns: minmax(0,1fr) 6mm minmax(0,1fr) 6mm minmax(0,1fr); }
.node { padding: 3mm !important; } .node b { font-size: 11pt !important; }
.node p,.node small { font-size: 8pt !important; } .node .v { font-size: 13pt !important; }
.hbar { grid-template-columns: 34mm minmax(0,1fr) 19mm; gap: 3mm; font-size: 9pt; }
.hbar .b { height: 4mm; }
.gloss { grid-template-columns: 38mm minmax(0,1fr); gap: 0 5mm; }
.print-summary { font-size: 12pt; font-weight: bold; margin-top: 5mm; }
.print-details.answers { break-before: page; }
.print-details.answers .chapter { break-before: auto; }
a { color: inherit !important; text-decoration-thickness: .4pt; }
.handbook h1,.handbook h2,.handbook h3,.handbook h4,.handbook h5,
.handbook p,.handbook span,.handbook small,.handbook strong,.handbook b,
.handbook li,.handbook dt,.handbook dd,.handbook summary { color: #161616 !important; }
.handbook .node.dark,.handbook .node.dark * { color: white !important; }
.handbook .warn,.handbook .key { color: #161616 !important; }
'''


def export(scratch):
    source = ROOT / 'verification-previews/Strategy_Company_and_Economics_Handbook.html'
    text = source.read_text()
    # PDFs show all answers, including material collapsed in the HTML reader.
    text = re.sub(r'<details([^>]*)>', r'<div\1>', text).replace('</details>', '</div>')
    text = re.sub(r'<summary([^>]*)>', '<div class="print-summary">', text).replace('</summary>', '</div>')
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.S)
    # SVG fragments need presentation attributes in the PDF renderer.
    text = re.sub(r'<(polyline|path) class="ln"', r'<\1 style="fill:none;stroke:#161616;stroke-width:2.5" class="ln"', text)
    text = text.replace('<line class="ax"', '<line style="stroke:#666;stroke-width:1" class="ax"')
    text = text.replace('<line class="ref"', '<line style="stroke:#666;stroke-dasharray:4 4" class="ref"')
    text = text.replace('<circle class="dot"', '<circle style="fill:#ffe047;stroke:#161616;stroke-width:2" class="dot"')
    text = re.sub(r'href="data:application/[^\"]+" download="[^"]+"', 'href="#document-status"', text)
    text = text.replace('Download embedded Excel workbook', 'Excel workbook in PDF attachments')
    text = text.replace('The original Excel workbook is embedded as a download.',
                        'The original Excel workbook is included as a PDF attachment.')
    scratch.mkdir(parents=True, exist_ok=True)
    intermediate = scratch / 'printed.pdf'
    HTML(string=text, base_url=str(source.parent)).write_pdf(intermediate, stylesheets=[CSS(string=PRINT_CSS)])
    writer = PdfWriter()
    writer.clone_document_from_reader(PdfReader(intermediate))
    writer.add_attachment('Strategy_Preferred_Coverage_Model.xlsx', (ROOT / 'Strategy_Preferred_Coverage_Model.xlsx').read_bytes())
    writer.add_metadata({'/Title': 'Strategy Company and Economics Handbook', '/Author': 'Rahil Bhavan',
                         '/Subject': 'Company reference and economics self-study course'})
    output = ROOT / 'verification-previews/Strategy_Company_and_Economics_Handbook.pdf'
    writer.write(output)
    print(f'Created {output} ({len(writer.pages)} pages, {output.stat().st_size:,} bytes)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scratch', required=True, type=Path)
    export(parser.parse_args().scratch)
