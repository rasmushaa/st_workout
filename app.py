import os
from dotenv import load_dotenv
import streamlit as st

env = os.getenv('STREAMLIT_ENV', 'dev') # Load the environment, default is dev
dotenv_file = f".env.{env}"
load_dotenv(dotenv_file)

def main():
    st.switch_page('pages/login.py')


if __name__ == '__main__':
    main()