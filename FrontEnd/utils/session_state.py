def get_session():
    import streamlit as st
    if 'session_state' not in st.session_state:
        st.session_state.session_state = {
            "token": None,
            "username": None,
        }
    return st.session_state.session_state
