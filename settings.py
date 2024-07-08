import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText
from auth import get_user_profile

def manage_settings():
    st.query_params.page = "Gerenciar Configurações"
    st.title("Configurações de Usuários e Condomínios")

    option = st.selectbox("Selecione a ação", ["Adicionar Usuário", "Adicionar Condomínio", "Editar Usuário", "Editar Condomínio"])

    if option == "Adicionar Usuário":
        add_user()
    elif option == "Adicionar Condomínio":
        add_condo()
    elif option == "Editar Usuário":
        edit_user()
    elif option == "Editar Condomínio":
        edit_condo()

def add_user():
    with st.form("add_user_form"):
        username = st.text_input("Nome de Usuário")
        email = st.text_input("E-mail")
        profile = st.selectbox("Perfil", ["Síndico", "Subsindico", "Morador"])
        condo_id = st.number_input("ID do Condomínio", min_value=1)
        submitted = st.form_submit_button("Adicionar Usuário")
        
        if submitted:
            conn = sqlite3.connect('condo.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, profile, condo_id) VALUES (?, ?, ?, ?)", 
                           (username, email, profile, condo_id))
            conn.commit()
            conn.close()
            send_invitation_email(email, condo_id)
            st.success("Usuário adicionado com sucesso e convite enviado")

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

def add_condo():
    with st.form("add_condo_form"):
        name = st.text_input("Nome do Condomínio")
        submitted = st.form_submit_button("Adicionar Condomínio")
        
        if submitted:
            conn = sqlite3.connect('condo.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO condos (name) VALUES (?)", (name,))
            conn.commit()
            conn.close()
            st.success("Condomínio adicionado com sucesso")

def edit_user():
    st.write("### Editar Usuário")
    user_id = st.number_input("ID do Usuário", min_value=1)
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    
    if user:
        username = st.text_input("Nome de Usuário", value=user[1])
        email = st.text_input("E-mail", value=user[4])
        
        # Verificar se o usuário logado é um ADM
        logged_in_user_email = st.session_state.get('user')
        logged_in_user_profile = get_user_profile(logged_in_user_email)
        
        if logged_in_user_profile == "ADM":
            profile = st.selectbox("Perfil", ["Síndico", "Subsindico", "Morador", "ADM"], index=["Síndico", "Subsindico", "Morador", "ADM"].index(user[3]))
        else:
            profile = st.selectbox("Perfil", ["Síndico", "Subsindico", "Morador"], index=["Síndico", "Subsindico", "Morador"].index(user[3]))
        
        condo_id = st.number_input("ID do Condomínio", min_value=1, value=user[5])
        
        cursor.execute("SELECT name FROM condos WHERE id=?", (condo_id,))
        condo = cursor.fetchone()
        if condo:
            st.text(f"Nome do Condomínio: {condo[0]}")
        
        if st.button("Atualizar Usuário"):
            cursor.execute("UPDATE users SET username=?, email=?, profile=?, condo_id=? WHERE id=?", 
                           (username, email, profile, condo_id, user_id))
            conn.commit()
            st.success("Usuário atualizado com sucesso")
    else:
        st.error("Usuário não encontrado")

    conn.close()

def edit_condo():
    st.write("### Editar Condomínio")
    condo_id = st.number_input("ID do Condomínio", min_value=1)
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM condos WHERE id=?", (condo_id,))
    condo = cursor.fetchone()
    
    if condo:
        name = st.text_input("Nome do Condomínio", value=condo[1])
        
        if st.button("Atualizar Condomínio"):
            cursor.execute("UPDATE condos SET name=? WHERE id=?", 
                           (name, condo_id))
            conn.commit()
            st.success("Condomínio atualizado com sucesso")
    else:
        st.error("Condomínio não encontrado")

    conn.close()
