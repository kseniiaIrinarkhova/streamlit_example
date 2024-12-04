# importing libs
import streamlit as st
from groq import Groq

# initializing groq
client = Groq(api_key=st.secrets['GROQ_API_KEY'])

print(st.session_state)

# set default model
if 'default_model' not in st.session_state:
    st.session_state['default_model'] = 'llama3-8b-8192'

# set a message collection

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    print(st.session_state)
    st.session_state.messages.append({'role': 'assistant', 'content': 'Hello! How can I help you today?'})

# Sidebar
st.sidebar.title('Chat')

# Main page
st.title('Chat Page')
st.write('Chatbot Powered by Groq and llama3-8b-8192 default model')
st.divider()

# display list of messages
if st.session_state.messages:
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
else:
    st.write('No messages yet')


st.divider()

#input for new messages
# new_message = st.chat_input('Type your message here')
# st.session_state.messages.append({'role': 'user', 'content': new_message})
