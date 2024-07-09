import streamlit as st
import sqlite3
from database import get_condos

def complete_registration():
    st.query_params.clear()
    st.title("Completar Cadastro")
    
    query_params = st.query_params.to_dict()
    condos = get_condos()
    condo_names = [condo[1] for condo in condos]
    condo_dict = {condo[1]: condo[0] for condo in condos}
    
    # Verificar se o condo_id está nos parâmetros da URL
    if 'condo_id' in query_params:
        condo_id = query_params['condo_id']
        selected_condo = next((name for name, id in condo_dict.items() if str(id) == condo_id), None)
    else:
        selected_condo = None

    email = st.text_input("E-mail")
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type="password")
    
    if selected_condo:
        st.write(f"Condomínio: {selected_condo}")
    else:
        selected_condo = st.selectbox("Selecione o Condomínio", condo_names)
        condo_id = condo_dict[selected_condo]

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
