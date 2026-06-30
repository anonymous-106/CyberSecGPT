from utils.database import retrieve
from utils.pdf_reader import read_pdf
from utils.chunker import create_chunks
from utils.embeddings import embed
from utils.database import store_chunk
from utils.database import count_chunks
from utils.database import retrieve


def index_pdf():
    text = read_pdf("uploads/ECCU-Catalog-2025.pdf")

    chunks = create_chunks(text, chunk_size=100, overlap_size=20)

    for i, chunk in enumerate(chunks):
        embedding = embed(chunk)

        store_chunk(
            id=f"chunk_{i}",
            chunk=chunk,
            embedding=embedding
        )

    print("PDF Indexed Successfully!")
    print(f"Total chunks stored: {count_chunks()}")


def ask_question():
    question = input("Ask a CyberSecurity question: ")

    question_embedding = embed(question)

    result = retrieve(question_embedding)

    print(result)


while True:
    print("\n===== CyberSecGPT =====")
    print("1. Index PDF")
    print("2. Ask Question")
    print("3. Exit")

    choice = input("Enter choice: ")