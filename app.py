from pypdf import PdfReader
reader = PdfReader("uploads/ECCU-Catalog-2025.pdf")
print(len(reader.pages))
#page = reader.pages[0]
for page in reader.pages:
    text = page.extract_text()
    print(text)