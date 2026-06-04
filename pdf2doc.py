from pdf2docx import Converter
from pathlib import Path

current_dir = Path(".")
docx_dir = current_dir / "docx"

docx_dir.mkdir(exist_ok=True)

pdf_files = list(current_dir.glob("*.pdf"))

if not pdf_files:
    print("PDF-файлы не найдены.")
    exit()

for pdf_file in pdf_files:
    docx_file = docx_dir / f"{pdf_file.stem}.docx"

    try:
        cv = Converter(str(pdf_file))
        cv.convert(str(docx_file))
        cv.close()

        print(f"[OK] {pdf_file.name} -> {docx_file.name}")

    except Exception as e:
        print(f"[ERROR] {pdf_file.name}: {e}")

print("\nГотово!")
