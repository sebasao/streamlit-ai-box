
import streamlit as st
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title='Home',
    page_icon=':house:',
    initial_sidebar_state='expanded'
)

st.title('Welcome')

st.markdown('''
            This App contains a series of demos and prototypes around AI. 
            
            Open the sidebar to browse them. 
            
            Have fun!
            ''')

