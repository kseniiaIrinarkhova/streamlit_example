# importing libs
import streamlit as st
from groq import Groq
import requests

# function to change default LLM
def change_model():
    st.session_state['default_model'] = st.session_state.model
    print(st.session_state)
    return

# initializing groq
client = Groq(api_key=st.secrets['GROQ_API_KEY'])

# get list of models
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
    "Content-Type": "application/json"
}

models = [model['id'] for model in requests.get(url, headers=headers).json()['data'] if model['context_window'] == 8192 and model['active'] == True] 

# print(st.session_state)

# set default model
if 'default_model' not in st.session_state:
    st.session_state['default_model'] = 'llama3-8b-8192'

# set a message collection

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    # print(st.session_state)
    st.session_state.messages.append({'role': 'assistant', 'content': 'Hello! How can I help you today?'})


# Sidebar
st.sidebar.title('Chat')
temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=1.0, value=0.5, step=0.01, key='temperature')
print(st.session_state['default_model'])
st.sidebar.selectbox('Model', models, index=models.index(st.session_state['default_model']), key='model', on_change=change_model)

# Main page
st.title('Chat Page')
st.write(f'Chatbot Powered by Groq and **{st.session_state.default_model}** as LLM')

st.divider()

# display list of messages
if st.session_state.messages:
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
else:
    st.write('No messages yet')


st.divider()

# input for new messages
if prompt := st.chat_input('Type a message...'):
    # display user message in chat message container
    with st.chat_message('user'):
        st.markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    with st.chat_message('assistant'):
        response_text = st.empty()
        # get response from groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": message["role"],
                    "content": message["content"],
                }
                for message in st.session_state['messages']
            ],
            model=st.session_state['default_model'],
            stream=True,
            temperature=temperature,
        )
        # create assistant response from groq response
        full_response=""

        for chunk in chat_completion:   
            full_response += chunk.choices[0].delta.content or ""
            response_text.markdown(full_response)
    
        # add assistant message to chat history
        st.session_state.messages.append({'role': 'assistant', 'content': full_response})
        # print(st.session_state.messages)
