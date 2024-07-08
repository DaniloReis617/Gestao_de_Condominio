import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_financial_data

def show_dashboard():
    st.query_params.clear()
    st.title("Dashboard Financeiro")
    
    condo_id = st.number_input("ID do Condomínio", min_value=1)
    year = st.selectbox("Selecione o Ano", options=[2021, 2022, 2023, 2024])
    
    data = get_financial_data(condo_id, year)
    if not data.empty:
        st.write("## Receita, Despesa e Saldo")
        st.dataframe(data)
        
        fig, ax = plt.subplots()
        data.plot(kind='bar', stacked=True, x='month', y=['receita', 'despesa', 'saldo'], ax=ax)
        ax.set_title("Receita, Despesa e Saldo Mensal")
        ax.set_xlabel("Mês")
        ax.set_ylabel("Valor")
        st.pyplot(fig)
    else:
        st.write("Sem dados para exibir")
