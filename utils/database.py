import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="cybersec_docs"
)
def store_chunk(id, chunk, embedding):
    collection.add(
    ids=[id],
    documents=[chunk],
    embeddings=[embedding]
)
    ##print(f"Stored {id}")

def count_chunks():
    return collection.count()