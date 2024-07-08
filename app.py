import streamlit as st
from auth import login, get_user_profile
from dashboard import show_dashboard
from finance import manage_finance
from inventory import manage_inventory
from payments import manage_payments
from providers import manage_providers
from settings import manage_settings
from invite_residents import invite_residents
from complete_registration import complete_registration

st.set_page_config(page_title="Administração de Condomínios", layout="wide")

PAGES = {
    "Dashboard": show_dashboard,
    "Gerenciar Finanças": manage_finance,
    "Gerenciar Estoque": manage_inventory,
    "Gerenciar Pagamentos": manage_payments,
    "Gerenciar Prestadores": manage_providers,
    "Gerenciar Configurações": manage_settings,
    "Convidar Moradores": invite_residents,
}

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if st.session_state.logged_in:
        profile = get_user_profile(st.session_state.user)
        
        st.sidebar.title("Menu")
        query_params = st.query_params.to_dict()
        default_page = "Dashboard"
        selected_page = query_params.get("page", default_page)

        if profile == "Síndico" or profile == "ADM":
            for page, func in PAGES.items():
                if st.sidebar.button(page):
                    st.query_params.page = page
                    st.experimental_rerun()

        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.experimental_rerun()
        
        page_func = PAGES.get(selected_page, show_dashboard)
        page_func()
    else:
        login()

if __name__ == "__main__":
    # Checar se está na tela de completar cadastro
    query_params = st.query_params.to_dict()
    if 'complete_registration' in query_params:
        complete_registration()
    else:
        main()
