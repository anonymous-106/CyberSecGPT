# 🛡️ CyberSecGPT

> A Retrieval-Augmented Generation (RAG) application built completely from scratch to understand how modern AI assistants retrieve information from documents using embeddings, vector databases, and semantic search.

---

# 🚀 Features

- ✅ PDF Text Extraction
- ✅ Intelligent Text Chunking
- ✅ Configurable Chunk Overlap
- ✅ Input Validation & Edge Case Handling
- ✅ Embedding Generation using Sentence Transformers
- ✅ ChromaDB Vector Database Integration
- ✅ Semantic Search using Vector Similarity
- ⏳ Persistent Vector Storage
- ⏳ LLM Response Generation
- ⏳ Interactive Chat Interface

---

# 🏗️ Project Structure

```text
CyberSecGPT/
│
├── uploads/
│   └── PDF Documents
│
├── database/
│   └── ChromaDB Storage
│
├── utils/
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── embeddings.py
│   └── database.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📅 Development Progress

## ✅ Day 1
- Created project structure
- Initialized GitHub repository
- Configured Python virtual environment
- Installed project dependencies

---

## ✅ Day 2
- Built PDF Reader
- Extracted text from uploaded PDF documents
- Verified complete document extraction

---

## ✅ Day 3
- Built intelligent chunking algorithm
- Added configurable chunk overlap
- Implemented validation for:
  - Invalid chunk size
  - Invalid overlap size
  - Empty documents
- Tested multiple edge cases

---

## ✅ Day 4
- Integrated Sentence Transformers
- Loaded `all-MiniLM-L6-v2`
- Generated 384-dimensional embeddings
- Verified embedding output and datatype

---

## ✅ Day 5
- Integrated ChromaDB
- Created vector database
- Created document collection
- Stored:
  - Chunk IDs
  - Document chunks
  - Embeddings
- Successfully indexed the complete PDF

---

## ✅ Day 6
- Implemented semantic retrieval
- Embedded user questions
- Queried ChromaDB using vector similarity
- Retrieved the most relevant document chunks
- Verified end-to-end retrieval pipeline
- Identified improvements for persistent storage

---

# ⚙️ Tech Stack

### Languages

- Python

### Libraries

- PyPDF
- NumPy
- Sentence Transformers
- ChromaDB

### Tools

- Git
- GitHub
- VS Code

---

# 📌 Current Pipeline

```text
PDF
 │
 ▼
Read Text ✅
 │
 ▼
Chunk Text ✅
 │
 ▼
Generate Embeddings ✅
 │
 ▼
Store in ChromaDB ✅
 │
 ▼
Semantic Retrieval ✅
 │
 ▼
LLM Response ⏳
```

---

# 🎯 Learning Objectives

This project is being developed to gain a deep understanding of:

- PDF Processing
- Intelligent Text Chunking
- Embedding Generation
- Vector Databases
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Large Language Model Integration

Every component is implemented manually to understand the underlying concepts instead of relying solely on high-level frameworks.

---

# 🗺️ Roadmap

- ✅ PDF Processing
- ✅ Intelligent Chunking
- ✅ Embedding Generation
- ✅ ChromaDB Integration
- ✅ Semantic Retrieval
- 🔄 Persistent ChromaDB Storage
- 🔄 LLM Integration
- 🔄 Conversational Chat Interface
- 🔄 Multi-PDF Support
- 🔄 Web Interface

---

# 🌟 Future Improvements

- Persistent vector database storage
- Upload multiple PDFs
- Support multiple embedding models
- Conversation memory
- Source citation for answers
- Streamlit/Flask web interface
- Docker deployment

---

## 🤝 Contributing

Suggestions and feedback are always welcome. Feel free to fork the repository, open issues, or submit pull requests.

---

## 📄 License

This project is developed for learning and educational purposes.