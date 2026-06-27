
from pypdf import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    page_count = len(reader.pages)
    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text()
    return all_text