from sentence_transformers import SentenceTransformer

model = None

def embed(text):
    global model

    if model is None:
        print("Loading embedding model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model.encode(text)