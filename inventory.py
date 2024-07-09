import streamlit as st
import sqlite3
import pandas as pd

def get_condos():
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM condos")
    condos = cursor.fetchall()
    conn.close()
    return condos

def manage_inventory():
    st.query_params.clear()
    st.title("Gerenciar Estoque")

    condos = get_condos()
    condo_names = [condo[1] for condo in condos]
    condo_dict = {condo[1]: condo[0] for condo in condos}

    with st.form("add_inventory_item_form"):
        selected_condo = st.selectbox("Selecione o Condomínio", condo_names)
        condo_id = condo_dict[selected_condo]
        item_name = st.text_input("Nome do Item")
        quantity = st.number_input("Quantidade", min_value=0)
        date_added = st.date_input("Data de Adição")
        submitted = st.form_submit_button("Adicionar Item ao Estoque")
        
        if submitted:
            add_inventory_item(condo_id, item_name, quantity, date_added)
            st.success("Item adicionado ao estoque com sucesso")

    st.write("## Estoque Atual")
    inventory_data = get_all_inventory_data(condo_id)
    if not inventory_data.empty:
        st.dataframe(inventory_data)
    else:
        st.write("Sem itens no estoque")

def add_inventory_item(condo_id, item_name, quantity, date_added):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (condo_id, item_name, quantity, date_added) VALUES (?, ?, ?, ?)",
                   (condo_id, item_name, quantity, date_added))
    conn.commit()
    conn.close()

def get_all_inventory_data(condo_id):
    conn = sqlite3.connect('condo.db')
    query = "SELECT * FROM inventory WHERE condo_id = ?"
    df = pd.read_sql_query(query, conn, params=(condo_id,))
    conn.close()
    return df
