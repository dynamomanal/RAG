# # ✅ Project: RAG System Frontend using Streamlit
# # 📁 File: frontend/pages/History.py

# import streamlit as st
# import requests
# from FrontEnd.utils.session_state import get_session

# API_URL = "http://localhost:8000"

# def render():
#     session = get_session()
#     st.title("📜 Query History")

#     res = requests.get(f"{API_URL}/history/", params={"token": session["token"]})

#     if res.status_code == 200:
#         history = res.json().get("history", [])
#         if not history:
#             st.info("No history available.")
#             return

#         for item in history:
#             st.write(f"🕒 {item['timestamp']}")
#             st.markdown(f"**You asked:** {item['query']}")
#             st.markdown(f"**Answer:** {item['response']}")
#             st.markdown("---")
#     else:
#         st.error("Failed to fetch history.")

import streamlit as st
import requests
from FrontEnd.utils.session_state import get_session

API_URL = "http://localhost:8000"

def render():
    session = get_session()
    st.title("📜 Query History")

    res = requests.get(f"{API_URL}/history/", params={"token": session["token"]})

    if res.status_code == 200:
        history = res.json().get("history", [])
        if not history:
            st.info("No history available.")
            return

        for item in history:
            st.write(f"🕒 {item['timestamp']}")
            st.markdown(f"**You asked:** {item['query']}")
            st.markdown(f"**Answer:** {item['response']}")
            st.markdown("---")
    else:
        st.error("Failed to fetch history.")
