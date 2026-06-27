from utils.pdf_reader import read_pdf
from utils.chunker import create_chunks

text = read_pdf("uploads/100 Essential Linux Commands.pdf")

chunks = create_chunks(text, chunk_size=100, overlap_size=20)

print(f"Total Chunks: {len(chunks)}")

for i in range(5):
    print(f"\n{'=' * 20} Chunk {i+1} {'=' * 20}")
    print(chunks[i])