import streamlit as st
import streamlit_authenticator as stauth
from src.helpers import parse_credentials
import page.Accuracies as ac


def getPage():
    config_dict = parse_credentials()

    authenticator = stauth.Authenticate(
        config_dict['credentials'],
        config_dict['cookie']['name'],
        config_dict['cookie']['key'],
        config_dict['cookie']['expiry_days'],
        config_dict['preauthorized']
    )

    if "name" not in st.session_state:
        st.session_state["name"]=""
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"]=""
    if "username" not in st.session_state:
        st.session_state["username"]=""


    name, authentication_status, username = authenticator.login('Login', 'main')

    st.session_state["name"]=name
    st.session_state["authentication_status"]=authentication_status
    st.session_state["username"]=username

    if authentication_status:
        #with st.sidebar:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
    elif authentication_status == False:
        #with st.sidebar:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        #with st.sidebar:
        st.warning('Please enter your username and password')

    if authentication_status:
        if "start_date" in st.session_state.keys():
            del st.session_state["start_date"]
        if "end_date" in st.session_state.keys():
            del st.session_state["end_date"]
        # ac.getPage()