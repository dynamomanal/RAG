from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Backend.db.database import get_db
from Backend.auth.jwt_handlers import decode_access_token
from Backend.db import crud

router = APIRouter()

@router.get("/")
def get_user_history(token: str, db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("user_id")
    history = crud.get_user_history(db, user_id=user_id)
    return {"user_id": user_id, "history": history}