# ✅ File: backend/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from Backend.db import crud
from Backend.db.database import get_db
from Backend.auth.password import hash_password, verify_password
from Backend.auth.jwt_handlers import create_access_token

router = APIRouter()

# ✅ Request models
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register_user(payload: RegisterRequest, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, username=payload.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    if crud.get_user_by_email(db, email=payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(payload.password)
    user = crud.create_user(db, username=payload.username, email=payload.email, hashed_password=hashed_pw)
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/login")
def login_user(payload: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=payload.username)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user.username, "user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
