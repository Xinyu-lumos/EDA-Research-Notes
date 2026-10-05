#!/usr/bin/env python3
"""Find caption candidates or export confirmed crops. Requires PyMuPDF.

Inventory is not a completeness audit. Page numbers are 1-based.
"""
import argparse
import json
import re
from pathlib import Path
import fitz

CAPTION = re.compile(r'^\s*(?:Fig(?:ure)?\.?\s*|图\s*)(\d+[A-Za-z]?)(?:\s*[:：.、]|\s+)', re.I)


def inventory(args):
    rows = []
    with fitz.open(args.source) as doc:
        empty = []
        for idx, page in enumerate(doc):
            if not page.get_text().strip():
                empty.append(idx + 1)
            for block in page.get_text('blocks'):
                if len(block) > 6 and block[6] != 0:
                    continue
                match = CAPTION.match(block[4])
                if match:
                    rows.append({'candidate_id': match[1], 'source_page': idx + 1,
                                 'caption_bbox': list(block[:4]), 'caption': block[4].strip(),
                                 'status': 'needs_visual_review'})
        result = {'source': str(Path(args.source).resolve()), 'page_count': len(doc),
                  'candidate_captions': rows, 'pages_without_text': empty,
                  'warning': 'Visually audit all figures and panels. Candidates can miss split/scanned captions or include references.'}
    dst = Path(args.out)
    if dst.resolve() == Path(args.source).resolve():
        raise ValueError('Output must differ from source.')
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'candidate_count': len(rows), 'inventory': str(dst), 'pages_without_text': empty}))


def crop(args):
    src = Path(args.source).resolve()
    dst = Path(args.out).resolve()
    if src == dst:
        raise ValueError('Output must differ from source PDF.')
    with fitz.open(src) as doc:
        if not 1 <= args.page <= len(doc):
            raise ValueError('Page out of range.')
        page = doc[args.page - 1]
        rect = fitz.Rect(args.rect)
        if rect.is_empty or rect.is_infinite or not page.rect.contains(rect):
            raise ValueError('Rectangle must be nonempty and within page.rect; visually verify rotated pages.')
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.suffix.lower() == '.pdf':
            with fitz.open() as out:
                target = out.new_page(width=rect.width, height=rect.height)
                target.show_pdf_page(target.rect, doc, args.page - 1, clip=rect)
                out.save(dst, garbage=4, deflate=True)
        elif dst.suffix.lower() == '.png':
            if args.dpi <= 0:
                raise ValueError('DPI must be positive.')
            page.get_pixmap(clip=rect, dpi=args.dpi, alpha=False).save(dst)
        else:
            raise ValueError('Output must be .pdf or .png.')
    print(json.dumps({'source_page': args.page, 'rect': args.rect, 'output': str(dst), 'visually_verified': False}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    inv = sub.add_parser('inventory')
    inv.add_argument('source')
    inv.add_argument('--out', required=True)
    inv.set_defaults(run=inventory)
    exp = sub.add_parser('crop')
    exp.add_argument('source')
    exp.add_argument('--page', type=int, required=True)
    exp.add_argument('--rect', nargs=4, type=float, required=True, metavar=('X0', 'Y0', 'X1', 'Y1'))
    exp.add_argument('--out', required=True)
    exp.add_argument('--dpi', type=int, default=300)
    exp.set_defaults(run=crop)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
