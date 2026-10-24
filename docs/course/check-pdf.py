"""Render every PDF page and create contact sheets for visual inspection."""
from pathlib import Path
import argparse
import json
import hashlib
import pymupdf
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]


def check(scratch):
    path = ROOT / 'verification-previews/Strategy_Company_and_Economics_Handbook.pdf'
    doc = pymupdf.open(path)
    images, outside = [], []
    for i, page in enumerate(doc):
        assert len(page.get_text().strip()) > 90, ('Unexpected near-empty page', i + 1)
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    x0, y0, x1, y1 = span['bbox']
                    if min(x0, y0) < -1 or x1 > page.rect.width + 1 or y1 > page.rect.height + 1:
                        outside.append(i + 1)
        image = scratch / f'page-{i+1:03}.png'
        page.get_pixmap(matrix=pymupdf.Matrix(1, 1), alpha=False).save(image)
        images.append(image)
    for start in range(0, len(images), 12):
        sheet = Image.new('RGB', (1120, 1260), '#bbb')
        draw = ImageDraw.Draw(sheet)
        for j, image in enumerate(images[start:start+12]):
            thumb = Image.open(image)
            thumb.thumbnail((268, 380))
            sheet.paste(thumb, ((j % 4)*280+(280-thumb.width)//2, (j//4)*420+25))
            draw.text(((j % 4)*280+10, (j//4)*420+6), f'Page {start+j+1}', fill='black')
        sheet.save(scratch / f'contact-{start//12+1:02}.png')
    assert not outside, outside
    text = '\n'.join(p.get_text() for p in doc)
    for term in ['Midterm', 'Capstone', 'Set A', 'Set D', 'Edition and learning status']:
        assert term.casefold() in text.casefold(), term
    reader = PdfReader(path)
    assert reader.attachments['Strategy_Preferred_Coverage_Model.xlsx'][0] == (ROOT / 'Strategy_Preferred_Coverage_Model.xlsx').read_bytes()
    result = {'pages': len(doc), 'text_characters': len(text), 'outside_page_text': outside,
              'workbook_attachment_matches': True, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    (scratch / 'checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scratch', required=True, type=Path)
    check(parser.parse_args().scratch)
