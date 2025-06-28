# 🧠 RAG Chat System

A full-stack Retrieval-Augmented Generation (RAG) system using FastAPI (backend) and Streamlit (frontend). Supports user authentication, OpenAI LLM queries, ChromaDB vector search, and history tracking.

---

## 🔧 Project Structure

rag_project/
├── backend/ # FastAPI backend
│ ├── main.py # App entry point
│ ├── routers/ # API routes: auth, query, history
│ ├── services/ # RAG logic, Chroma, OpenAI
│ ├── db/ # SQLAlchemy models and CRUD
│ ├── auth/ # JWT and password handling
│ └── .env # Secrets and config
├── frontend/ # Streamlit frontend
│ ├── app.py # Entry point
│ ├── pages/ # Login, Query, History
│ └── utils/ # Session manager
└── requirements.txt

yaml
Copy
Edit
