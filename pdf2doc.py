from pdf2docx import Converter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

current_dir = Path(".")
docx_dir = current_dir / "docx"

docx_dir.mkdir(exist_ok=True)

pdf_files = list(current_dir.glob("*.pdf"))

if not pdf_files:
    print("PDF-файлы не найдены.")
    exit()

def convert_pdf(pdf_file):
    docx_file = docx_dir / f"{pdf_file.stem}.docx"

    try:
        cv = Converter(str(pdf_file))
        cv.convert(str(docx_file))
        cv.close()

        return f"[OK] {pdf_file.name}"
    except Exception as e:
        return f"[ERROR] {pdf_file.name}: {e}"

workers = 4

print(f"Найдено PDF: {len(pdf_files)}")
print(f"Потоков: {workers}")

with ThreadPoolExecutor(max_workers=workers) as executor:
    futures = [executor.submit(convert_pdf, pdf) for pdf in pdf_files]

    for future in as_completed(futures):
        print(future.result())

print("\nГотово!")
