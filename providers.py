import streamlit as st
import sqlite3
import pandas as pd

def manage_providers():
    st.query_params.clear()
    st.title("Gerenciar Prestadores de Serviços")

    with st.form("add_provider_form"):
        condo_id = st.number_input("ID do Condomínio", min_value=1)
        provider_name = st.text_input("Nome do Prestador")
        service = st.text_input("Serviço Prestado")
        contact_info = st.text_input("Informações de Contato")
        submitted = st.form_submit_button("Adicionar Prestador")
        
        if submitted:
            add_provider(condo_id, provider_name, service, contact_info)
            st.success("Prestador adicionado com sucesso")

    st.write("## Prestadores de Serviços")
    providers_data = get_all_providers_data(condo_id)
    if not providers_data.empty:
        st.dataframe(providers_data)
    else:
        st.write("Sem prestadores de serviços registrados")

def add_provider(condo_id, provider_name, service, contact_info):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO providers (condo_id, provider_name, service, contact_info) VALUES (?, ?, ?, ?)",
                   (condo_id, provider_name, service, contact_info))
    conn.commit()
    conn.close()

def get_all_providers_data(condo_id):
    conn = sqlite3.connect('condo.db')
    query = "SELECT * FROM providers WHERE condo_id = ?"
    df = pd.read_sql_query(query, conn, params=(condo_id,))
    conn.close()
    return df
