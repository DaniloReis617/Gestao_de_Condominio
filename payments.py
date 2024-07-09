import streamlit as st
import sqlite3
import pandas as pd
from database import get_condos, get_users

def manage_payments():
    st.query_params.clear()
    st.title("Gerenciar Pagamentos")

    condos = get_condos()
    condo_names = [condo[1] for condo in condos]
    condo_dict = {condo[1]: condo[0] for condo in condos}

    with st.form("add_payment_form"):
        selected_condo = st.selectbox("Selecione o Condomínio", condo_names)
        condo_id = condo_dict[selected_condo]

        users = get_users(condo_id)
        user_names = [user[1] for user in users]
        user_dict = {user[1]: user[0] for user in users}

        selected_resident = st.selectbox("Selecione o Morador", user_names)
        resident_id = user_dict[selected_resident]

        amount = st.number_input("Valor", min_value=0.0)
        payment_date = st.date_input("Data de Pagamento")
        submitted = st.form_submit_button("Registrar Pagamento")
        
        if submitted:
            add_payment(condo_id, resident_id, amount, payment_date)
            st.success("Pagamento registrado com sucesso")

    st.write("## Pagamentos Registrados")
    payments_data = get_all_payments_data(condo_id)
    if not payments_data.empty:
        st.dataframe(payments_data)
    else:
        st.write("Sem pagamentos registrados")

def add_payment(condo_id, resident_id, amount, payment_date):
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (condo_id, resident_id, amount, payment_date) VALUES (?, ?, ?, ?)",
                   (condo_id, resident_id, amount, payment_date))
    conn.commit()
    conn.close()

def get_all_payments_data(condo_id):
    conn = sqlite3.connect('condo.db')
    query = "SELECT * FROM payments WHERE condo_id = ?"
    df = pd.read_sql_query(query, conn, params=(condo_id,))
    conn.close()
    return df
