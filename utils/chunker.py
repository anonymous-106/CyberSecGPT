def create_chunks(all_text, chunk_size, overlap_size):
    chunks = []
    start = 0
    words = all_text.split()

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    elif overlap_size < 0:
        raise ValueError("overlap_size must be greater than or equal to 0")
    elif overlap_size >= chunk_size:
        raise ValueError("overlap_size must be less than chunk_size")
    if len(words) == 0:
        return [] 
    
    text_length = len(words)
    while start < text_length:
        chunk_words = words[start:start + chunk_size]
    chunk = " ".join(chunk_words)
    chunks.append(chunk)
    start += chunk_size - overlap_size
    return chunks   