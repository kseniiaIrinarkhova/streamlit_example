import streamlit as st

#Sidebar

# Add the sidebar
st.sidebar.title('Chat')

# Add a checkbox to the sidebar
st.sidebar.checkbox('Display all')

#Main page

# Navbar
with st.container(border=True):
    # st.subheader("Navbar")
    st.page_link('./pages/chat.py', label='Chat')

# Set the title of the app
st.title('Chat App')
st.write('Chatbot Powered by Groq')
st.divider()