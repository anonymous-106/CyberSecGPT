from utils.pdf_reader import read_pdf
from utils.chunker import create_chunks
from utils.embeddings import embed
from utils.database import store_chunk
from utils.database import count_chunks
from utils.database import retrieve

text = read_pdf("uploads/ECCU-Catalog-2025.pdf")

chunks = create_chunks(text, chunk_size=100, overlap_size=20)

# print(f"Total Chunks: {len(chunks)}")

# for i in range(5):
#     print(f"\n{'=' * 20} Chunk {i+1} {'=' * 20}")
#     print(chunks[i])

embedding = embed(chunks[0])

# print(type(embedding))
# print(len(embedding))
# print(embedding[:10])

for i, chunk in enumerate(chunks):
    embedding = embed(chunk)

    store_chunk(
        id=f"chunk_{i}",
        chunk=chunk,
        embedding=embedding
    )

# print("Finished storing all chunks!")
print(f"Total chunks stored: {count_chunks()}")

question = input("Ask a CyberSecurity question: ")
result = retrieve(question)
print (result)