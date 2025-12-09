from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'scripts' / 'import_shipping_data.py'
OUT = ROOT / 'import_shipping_data.pdf'


def main():
    text = SRC.read_text(encoding='utf-8')

    c = canvas.Canvas(str(OUT), pagesize=letter)
    width, height = letter
    left_margin = 40
    top = height - 40
    line_height = 12

    y = top
    for line in text.splitlines():
        # wrap long lines manually
        if len(line) == 0:
            y -= line_height
            if y < 40:
                c.showPage()
                y = top
            continue
        while line:
            # approx max chars per line
            max_chars = 100
            chunk = line[:max_chars]
            c.drawString(left_margin, y, chunk)
            line = line[max_chars:]
            y -= line_height
            if y < 40:
                c.showPage()
                y = top

    c.save()


if __name__ == '__main__':
    main()
