import streamlit as st
import hashlib
from backend.credentials_api import CredentialsAPI


@st.cache_data
def st_wrapper_password_check(username, password_hash):
    api = CredentialsAPI()
    return api.username_and_password_match(username, password_hash)

@st.cache_data
def st_wrapper_init_user(username, password_hash):
    api = CredentialsAPI()
    return api.init_user(username, password_hash)


st.title('Amazing User Login App')

st.write('Please login')
username = st.text_input('Username')
password_hash = hashlib.sha256(st.text_input('Password', type='password').encode('utf-8')).hexdigest()

if st.button('Login', icon=":material/login:"):

    if st_wrapper_password_check(username, password_hash):
        st.success('Login successful')
        st.session_state['user'] = st_wrapper_init_user(username, password_hash)
        st.switch_page('pages/exercise.py')
    
    else:
        st.error('Password and Username do not match')