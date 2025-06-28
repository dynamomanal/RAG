# ✅ File: backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.routers import auth, query, history  # ✅ Use fully-qualified imports

app = FastAPI(title="RAG System API", version="1.0.0")

# ✅ Allow Streamlit frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with actual frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Attach routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(history.router, prefix="/history", tags=["history"])
