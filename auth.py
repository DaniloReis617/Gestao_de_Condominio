import streamlit as st
import sqlite3

def login():
    st.title("Login")
    with st.form("login_form"):
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if validate_login(email, password):
                st.session_state.logged_in = True
                st.session_state.user = email
                st.experimental_rerun()
            else:
                st.error("E-mail ou senha inválidos")

def validate_login(email, password):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def get_user_profile(email):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT profile FROM users WHERE email=?", (email,))
    profile = cursor.fetchone()
    conn.close()
    return profile[0] if profile else None
