import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText
from database import get_condos

def invite_residents():
    st.query_params.clear()
    st.title("Convidar Moradores")
    
    condos = get_condos()
    condo_names = [condo[1] for condo in condos]
    condo_dict = {condo[1]: condo[0] for condo in condos}

    with st.form("invite_residents_form"):
        email = st.text_input("E-mail do Morador")
        selected_condo = st.selectbox("Selecione o Condomínio", condo_names)
        condo_id = condo_dict[selected_condo]
        submitted = st.form_submit_button("Enviar Convite")
        
        if submitted:
            send_invitation_email(email, condo_id)
            st.success("Convite enviado com sucesso")

def send_invitation_email(email, condo_id):
    msg = MIMEText(f"Clique no link para completar seu cadastro: http://seuapp.com/complete_registration?condo_id={condo_id}")
    msg['Subject'] = 'Convite para completar cadastro'
    msg['From'] = 'seu_email@example.com'
    msg['To'] = email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('seu_email@example.com', 'sua_senha')
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
        st.success(f"Convite enviado para {email}")
    except Exception as e:
        st.error(f"Erro ao enviar o email: {e}")
