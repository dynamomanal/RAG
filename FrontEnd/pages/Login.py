# ✅ File: frontend/pages/Login.py

import streamlit as st
import requests
from utils.session_state import get_session

API_URL = "http://127.0.0.1:8000"  # Local FastAPI server

def render():
    session = get_session()
    st.title("🔐 Login / Register")

    auth_option = st.radio("Choose option:", ("Login", "Register"))
    username = st.text_input("Username")
    email = st.text_input("Email") if auth_option == "Register" else None
    password = st.text_input("Password", type="password")

    if st.button(auth_option):
        try:
            if auth_option == "Register":
                res = requests.post(f"{API_URL}/auth/register", json={
                    "username": username,
                    "email": email,
                    "password": password
                })
                if res.status_code == 200:
                    st.success("✅ Registered successfully!")
                else:
                    try:
                        st.error(res.json().get("detail", "Registration failed"))
                    except:
                        st.error(f"Error: {res.text}")

            else:  # Login
                res = requests.post(f"{API_URL}/auth/login", json={
                    "username": username,
                    "password": password
                })
                if res.status_code == 200:
                    session["token"] = res.json()["access_token"]
                    session["username"] = username
                    st.success("✅ Logged in successfully!")
                    st.experimental_rerun()
                else:
                    try:
                        st.error(res.json().get("detail", "Invalid credentials"))
                    except:
                        st.error(f"Error: {res.text}")

        except Exception as e:
            st.error(f"❌ Request failed: {str(e)}")
