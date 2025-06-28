# ✅ Project: RAG System Backend using FastAPI
# 📁 File: backend/routers/query.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.db.database import get_db
from Backend.auth.jwt_handlers import decode_access_token
from Backend.db import crud
from Backend.services.rag_engine import run_rag_pipeline

router = APIRouter()

@router.post("/")
def query_rag_system(query: str, token: str, db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("user_id")
    response = run_rag_pipeline(query)
    crud.create_query_history(db, user_id=user_id, query=query, response=response)
    return {"query": query, "response": response}