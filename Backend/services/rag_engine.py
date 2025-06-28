# ✅ Project: RAG System Backend using FastAPI
# 📁 File: backend/services/rag_engine.py

# This file will define the core Retrieval-Augmented Generation logic

from Backend.services.chroma_client import get_similar_documents
from Backend.services.openai_client import generate_answer

def run_rag_pipeline(user_query: str):
    # Step 1: Retrieve relevant chunks from Chroma
    context_docs = get_similar_documents(user_query)

    # Step 2: Combine them into a context string
    context = "\n".join([doc.page_content for doc in context_docs])

    # Step 3: Pass context + question to LLM
    answer = generate_answer(user_query, context)

    return answer
