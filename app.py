from utils.pdf_reader import read_pdf
from utils.chunker import create_chunks
from utils.embeddings import embed

text = read_pdf("uploads/ECCU-Catalog-2025.pdf")

chunks = create_chunks(text, chunk_size=100, overlap_size=20)

# print(f"Total Chunks: {len(chunks)}")

# for i in range(5):
#     print(f"\n{'=' * 20} Chunk {i+1} {'=' * 20}")
#     print(chunks[i])

embedding = embed(chunks[0])

print(type(embedding))
print(len(embedding))
print(embedding[:10])