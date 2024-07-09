import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from database import get_financial_data, get_user_profile, get_users, get_condos, get_user_id

def show_dashboard():
    st.query_params.clear()

    col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
    
    with col1:
        st.title("Dashboard Financeiro")
    
    # Botão de atualizar dados
    with col4:
        if st.button("Atualizar Dados"):
            st.session_state.update_data = True
    
    # Obter o perfil do usuário logado
    logged_in_user_email = st.session_state.get('user')
    profile = get_user_profile(logged_in_user_email)
    
    # Obter a lista de condomínios do banco de dados
    condos = get_condos()
    condo_names = [condo[1] for condo in condos]
    condo_dict = {condo[1]: condo[0] for condo in condos}
    
    # Permitir que o usuário selecione o condomínio pelo nome
    selected_condo = st.selectbox("Selecione o Condomínio", condo_names)
    condo_id = condo_dict[selected_condo]

    # Se o usuário é ADM, Síndico ou Subsíndico, adicionar filtro por usuário
    if profile in ["ADM", "Síndico", "Subsindico"]:
        users = get_users(condo_id)
        user_names = [user[1] for user in users]
        user_dict = {user[1]: user[0] for user in users}
        selected_user = st.selectbox("Selecione o Usuário", user_names)
        user_id = user_dict[selected_user]
    else:
        # Se o perfil é Morador, mostrar apenas seus próprios dados
        user_id = get_user_id(logged_in_user_email)

    year = st.selectbox("Selecione o Ano", options=[2021, 2022, 2023, 2024])
    
    if 'update_data' not in st.session_state:
        st.session_state.update_data = False
    
    if st.session_state.update_data:
        data = get_financial_data(condo_id, year, user_id)
        st.session_state.update_data = False
    else:
        data = get_financial_data(condo_id, year, user_id)
    
    if not data.empty:
        st.write("## Receita, Despesa e Saldo")
        st.dataframe(data)

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=data['month'],
            y=data['receita'],
            name='Receita',
            marker_color='rgb(55, 83, 109)'
        ))

        fig.add_trace(go.Bar(
            x=data['month'],
            y=data['despesa'],
            name='Despesa',
            marker_color='rgb(26, 118, 255)'
        ))

        fig.add_trace(go.Bar(
            x=data['month'],
            y=data['saldo'],
            name='Saldo',
            marker_color='rgb(255, 153, 51)'
        ))

        fig.update_layout(
            title='Receita, Despesa e Saldo Mensal',
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Valor',
                titlefont_size=16,
                tickfont_size=14,
            ),
            barmode='stack',
            bargap=0.15,
            bargroupgap=0.1
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Sem dados para exibir")
        fig = go.Figure()

        months = [f"{i:02}" for i in range(1, 13)]
        empty_data = pd.DataFrame({
            'month': months,
            'receita': [0] * 12,
            'despesa': [0] * 12,
            'saldo': [0] * 12
        })

        fig.add_trace(go.Bar(
            x=empty_data['month'],
            y=empty_data['receita'],
            name='Receita',
            marker_color='rgb(55, 83, 109)'
        ))

        fig.add_trace(go.Bar(
            x=empty_data['month'],
            y=empty_data['despesa'],
            name='Despesa',
            marker_color='rgb(26, 118, 255)'
        ))

        fig.add_trace(go.Bar(
            x=empty_data['month'],
            y=empty_data['saldo'],
            name='Saldo',
            marker_color='rgb(255, 153, 51)'
        ))

        fig.update_layout(
            title='Receita, Despesa e Saldo Mensal (vazio)',
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Valor',
                titlefont_size=16,
                tickfont_size=14,
            ),
            barmode='stack',
            bargap=0.15,
            bargroupgap=0.1
        )

        st.plotly_chart(fig, use_container_width=True)
