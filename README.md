# 🛡️ CyberSecGPT

> A Retrieval-Augmented Generation (RAG) assistant that answers cybersecurity questions using uploaded PDF documents by combining semantic search with Large Language Models (LLMs).

---

## 🚀 Features

* ✅ PDF Reader
* ✅ Intelligent Text Chunking
* ✅ Configurable Chunk Overlap
* ✅ Input Validation & Edge Case Handling
* ✅ Embedding Generation (Sentence Transformers)
* ✅ ChromaDB Integration
* 🔄 Semantic Search (In Progress)
* ⏳ AI Question Answering

---

## 🏗️ Project Structure

```text
CyberSecGPT/
│
├── uploads/
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

## 📅 Development Progress

### ✅ Day 1

* Project setup
* GitHub repository
* Python virtual environment

### ✅ Day 2

* Built PDF Reader
* Extracted text from uploaded PDF files

### ✅ Day 3

* Implemented intelligent text chunking
* Added configurable overlap support
* Implemented validation and edge case handling
* Tested multiple chunking scenarios

### ✅ Day 4

* Integrated Sentence Transformers
* Generated embeddings using `all-MiniLM-L6-v2`
* Converted text chunks into 384-dimensional vectors
* Verified embedding generation and output format

### ✅ Day 5

* Integrated ChromaDB
* Created vector database client
* Created document collection
* Stored chunk IDs, documents, and embeddings
* Successfully indexed all generated chunks
* Prepared retrieval pipeline for semantic search

---

## 🛠️ Tech Stack

### Current

* Python
* PyPDF
* NumPy
* Sentence Transformers
* ChromaDB
* Git
* GitHub

### Coming Soon

* Semantic Search
* Ollama Integration
* Retrieval-Augmented Generation (RAG) Pipeline

---

## 🎯 Goal

Build a production-quality Retrieval-Augmented Generation (RAG) application completely from scratch to deeply understand:

* PDF Processing
* Intelligent Chunking
* Embedding Generation
* Vector Databases
* Semantic Search
* LLM Integration

The objective is to understand every component under the hood instead of relying only on high-level frameworks.

---

## 🚧 Current Pipeline

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
Semantic Search 🔄
 │
 ▼
LLM Response ⏳
```
