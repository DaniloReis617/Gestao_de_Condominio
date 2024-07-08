import streamlit as st
import sqlite3

def complete_registration():
    st.query_params.clear()
    st.title("Completar Cadastro")
    
    query_params = st.query_params.to_dict()
    condo_id = query_params.get('condo_id', None)
    email = st.text_input("E-mail")
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Completar Cadastro"):
        if condo_id:
            conn = sqlite3.connect('condo.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET username=?, password=? WHERE email=? AND condo_id=?", 
                           (username, password, email, condo_id))
            conn.commit()
            conn.close()
            st.success("Cadastro completado com sucesso")
        else:
            st.error("ID do Condomínio inválido")
