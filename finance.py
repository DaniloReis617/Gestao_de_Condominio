import streamlit as st
import sqlite3
import pandas as pd

def manage_finance():
    st.query_params.clear()
    st.title("Gerenciar Finanças")

    with st.form("add_financial_record_form"):
        condo_id = st.number_input("ID do Condomínio", min_value=1)
        date = st.date_input("Data")
        description = st.text_input("Descrição")
        amount = st.number_input("Valor", min_value=0.0)
        type = st.selectbox("Tipo", ["receita", "despesa"])
        submitted = st.form_submit_button("Adicionar Registro Financeiro")
        
        if submitted:
            add_financial_record(condo_id, date, description, amount, type)
            st.success("Registro financeiro adicionado com sucesso")

    st.write("## Registros Financeiros")
    financial_data = get_all_financial_data(condo_id)
    if not financial_data.empty:
        st.dataframe(financial_data)
    else:
        st.write("Sem registros financeiros")

def add_financial_record(condo_id, date, description, amount, type):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO financial (condo_id, date, description, amount, type) VALUES (?, ?, ?, ?, ?)",
                   (condo_id, date, description, amount, type))
    conn.commit()
    conn.close()

def get_all_financial_data(condo_id):
    conn = sqlite3.connect('condo.db')
    query = "SELECT * FROM financial WHERE condo_id = ?"
    df = pd.read_sql_query(query, conn, params=(condo_id,))
    conn.close()
    return df
