
client = None
collection = None

def get_collection():
    global client, collection

    if collection is None:
        import chromadb

        client = chromadb.PersistentClient(path="database")

        collection = client.get_or_create_collection(
            name="cybersec_docs"
        )

    return collection


def store_chunk(chunk, embedding, metadata):
    collection = get_collection()

    collection.add(
        ids=[...],
        documents=[chunk],
        embeddings=[embedding],
        metadatas=[metadata]
    )

def retrieve(query_embedding, top_k=5):
    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

def count_chunks():
    collection = get_collection()
    return collection.count()













# import chromadb

# client = chromadb.PersistentClient(path="database")
# collection = client.get_or_create_collection(
#     name="cybersec_docs"
# )
# def store_chunk(id, chunk, embedding):
#     collection.add(
#     ids=[id],
#     documents=[chunk],
#     embeddings=[embedding]
# )
#     ##print(f"Stored {id}")

# def count_chunks():
#     return collection.count()

# # from utils.embeddings import embed
# def retrieve(query_embedding):
#     result = collection.query(
#         query_embeddings=[query_embedding],
#         n_results=3
#     )

#     return result