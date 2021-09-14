import io
from pathlib import Path

from chess import pgn, svg
from PyPDF2 import PdfFileReader, PdfFileWriter

from reportlab.pdfgen import canvas

from .pdfutils import PdfImage

if __name__ == "__main__":
    template_path = Path("..") / "templates" / "Proposition2.pdf"
    
    
    pdf = PdfFileReader(template_path.open("rb"))
    out = PdfFileWriter()

    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    puzzle_path = Path("..") / "chess-latex" / "main.pdf"
    puzzle = PdfImage(puzzle_path)
    puzzle.drawOn(can, 0,0)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    out.addPage(pdf.getPage(5))

    page = pdf.getPage(6)
    page.mergePage(new_pdf.getPage(0))
    out.addPage(page)

    with (Path("..") / "out.pdf").open("wb") as file:
        out.write(file)
