from utils.pdf_reader import read_pdf
from utils.chunker import create_chunks

text = read_pdf("uploads/ECCU-Catalog-2025.pdf")

chunks = create_chunks(text, chunk_size=100, overlap_size=20)
