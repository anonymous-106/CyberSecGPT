# 🛡️ CyberSecGPT

> A Retrieval-Augmented Generation (RAG) assistant that answers cybersecurity questions using uploaded PDF documents by combining semantic search with Large Language Models (LLMs).

---

## 🚀 Features

* ✅ PDF Reader
* ✅ Intelligent Text Chunking
* ✅ Configurable Chunk Overlap
* ✅ Input Validation & Edge Case Handling
* ✅ Embedding Generation (Sentence Transformers)
* 🔄 Vector Database Integration (In Progress)
* ⏳ Semantic Search
* ⏳ AI Question Answering

---

## 🏗️ Project Structure

```text
CyberSecGPT/
│
├── uploads/              # Uploaded PDF files
├── utils/
│   ├── pdf_reader.py     # Extract text from PDFs
│   ├── chunker.py        # Chunk creation with overlap & validation
│   └── embeddings.py     # Generate vector embeddings
│
├── app.py                # Main application
├── requirements.txt
└── README.md
```

---

## 📅 Development Progress

### ✅ Day 1

* Project setup
* GitHub repository initialization
* Python virtual environment

### ✅ Day 2

* Implemented PDF Reader
* Extracted text from uploaded PDF files

### ✅ Day 3

* Built configurable text chunking
* Added overlap support
* Implemented validation and edge case handling
* Tested chunk generation with different configurations

### ✅ Day 4

* Integrated Sentence Transformers
* Generated embeddings using `all-MiniLM-L6-v2`
* Successfully converted text chunks into 384-dimensional vectors
* Verified embedding generation and output format
* Prepared architecture for vector database integration

---

## 🛠️ Tech Stack

### Current

* Python
* PyPDF
* NumPy
* Sentence Transformers
* Git
* GitHub

### Coming Soon

* ChromaDB
* Ollama
* Semantic Search Pipeline

---

## 🎯 Goal

Build a production-quality Retrieval-Augmented Generation (RAG) application completely from scratch to deeply understand:

* PDF Processing
* Text Chunking
* Embedding Generation
* Vector Databases
* Semantic Search
* LLM Integration

Instead of relying solely on high-level frameworks, this project focuses on understanding how every component works under the hood.

---

## 🚧 Current Progress

```text
PDF
 │
 ▼
Read Text
 │
 ▼
Chunk Text
 │
 ▼
Generate Embeddings ✅
 │
 ▼
Store in ChromaDB ⏳
 │
 ▼
Semantic Search ⏳
 │
 ▼
LLM Response ⏳
```
