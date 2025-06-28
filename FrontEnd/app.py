import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from FrontEnd.pages import Login, Query, History
from FrontEnd.utils.session_state import get_session

st.set_page_config(page_title="RAG Chat App", layout="wide")

# Initialize session state
session = get_session()

# Sidebar navigation
st.sidebar.title("🔍 RAG Chat System")
page = st.sidebar.radio("Navigate", ("Login", "Query", "History"))

if page == "Login":
    Login.render()
elif page == "Query":
    if session.get("token"):
        Query.render()
    else:
        st.warning("🔐 Please login first!")
elif page == "History":
    if session.get("token"):
        History.render()
    else:
        st.warning("🔐 Please login first!")
