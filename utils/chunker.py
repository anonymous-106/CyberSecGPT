def create_chunks(all_text, chunk_size, overlap_size):
    chunks = []
    start = 0
    words = all_text.split()
    text_length = len(words)
    while start < text_length:
        chunk_words = words[start:start + chunk_size]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        start += chunk_size - overlap_size
    return chunks   