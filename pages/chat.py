# importing libs
import streamlit as st
from groq import Groq

# initializing groq
client = Groq(api_key=st.secrets['GROQ_API_KEY'])
