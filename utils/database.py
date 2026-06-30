
import chromadb

client = chromadb.PersistentClient(path="database")
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

from utils.embeddings import embed
def retrieve(query):
    query_embedding = embed(query)
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return result