from pdf2docx import Converter
from pathlib import Path

pdf_dir = Path("pdf")
docx_dir = Path("docx")

docx_dir.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob("*.pdf"):
    docx_file = docx_dir / f"{pdf_file.stem}.docx"

    try:
        cv = Converter(str(pdf_file))
        cv.convert(str(docx_file))
        cv.close()

        print(f"[OK] {pdf_file.name}")
    except Exception as e:
        print(f"[ERROR] {pdf_file.name}: {e}")