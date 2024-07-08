import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText

def invite_residents():
    st.query_params.clear()
    st.title("Convidar Moradores")
    
    with st.form("invite_residents_form"):
        email = st.text_input("E-mail do Morador")
        condo_id = st.number_input("ID do Condomínio", min_value=1)
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
