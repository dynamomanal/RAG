# ✅ Project: RAG System Frontend using Streamlit
# 📁 File: frontend/pages/Query.py

import streamlit as st
import requests
from FrontEnd.utils.session_state import get_session

API_URL = "http://localhost:8000"

def render():
    session = get_session()
    st.title("🤖 Ask the RAG System")

    user_query = st.text_area("Enter your query:")

    if st.button("Submit"):
        if not user_query:
            st.warning("Please enter a question.")
            return

        res = requests.post(
            f"{API_URL}/query/",
            params={"query": user_query, "token": session["token"]},
        )

        if res.status_code == 200:
            st.success("✅ Answer generated:")
            st.markdown(res.json()["response"])
        else:
            try:
                 st.error(res.json().get("detail", "Failed to generate answer"))
            except Exception:
                 st.error(f"Error: {res.text}")
