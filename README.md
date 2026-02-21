# 🚀 Hybrid RAG Knowledge Assistant

A production-ready Hybrid Retrieval-Augmented Generation (RAG) system that allows users to upload PowerPoint documents and ask natural language questions about their content.

The system combines semantic search (FAISS) and keyword search (BM25) to improve retrieval quality and reduce hallucinations in LLM responses.

🌐 Live Demo: [https://ragknowledgeassistent-mggdbnszfrb8jgu4dzkmjv.streamlit.app/](https://ragknowledgeassistent-mggdbnszfrb8jgu4dzkmjv.streamlit.app/)

---

## 📌 Problem Statement

Large Language Models (LLMs) often hallucinate when they lack domain-specific context.  
This project aims to ground LLM responses strictly in uploaded document content using a hybrid retrieval strategy.

---

## 🧠 System Architecture

User Query  
↓  
Hybrid Retriever (FAISS + BM25)  
↓  
Top-K Relevant Chunks  
↓  
Groq LLM (Context-Constrained Prompt)  
↓  
Final Answer + Source Transparency  

---

## ⚙️ Tech Stack

- Python
- Streamlit
- FAISS (Vector Search)
- SentenceTransformers (Embeddings)
- BM25 (Keyword Retrieval)
- Groq LLM
- python-pptx

---

## 🔎 How It Works

### 1️⃣ Document Ingestion
- Upload PPT file
- Extract text using `python-pptx`
- Perform smart chunking (500 characters with 50 overlap)

### 2️⃣ Hybrid Retrieval
- Semantic similarity search using FAISS
- Keyword relevance scoring using BM25
- Weighted combination of both results

### 3️⃣ Answer Generation
- Retrieved chunks are passed to a Groq-hosted LLM
- LLM is instructed to answer strictly from provided context
- If information is not found:
  > "Information not available in document."

### 4️⃣ Transparency
- Retrieved source chunks are displayed with each answer

---

## 🛡️ Hallucination Reduction Strategy

- Context-constrained prompting
- Hybrid retrieval for improved recall
- Explicit fallback response when answer not found

---

## 🚀 Deployment

The application is deployed on **Streamlit Cloud** for real-time interaction.

Users can:
- Upload their own PowerPoint documents
- Ask natural language questions
- View retrieved source chunks

---

## 📂 Project Structure

RAG-App/
│
├── app.py
├── rag_chatbot.py
├── requirements.txt
└── README.md

---

## 🧪 Future Improvements

- Retrieval evaluation metrics (Hit@K)
- Reranking model integration
- Multi-document indexing
- Persistent vector storage
- Docker containerization

---

## 💡 Key Learning Outcomes

- Built end-to-end Hybrid RAG pipeline
- Implemented vector + keyword search integration
- Applied prompt engineering for hallucination control
- Deployed interactive AI application to cloud

---

## 👩‍💻 Author

Akankshi Dubey  
B.Tech CSE (IoT & Cyber Security)  
Generative AI & ML Enthusiast

