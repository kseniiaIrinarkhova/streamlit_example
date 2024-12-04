import streamlit as st

#Sidebar

# Add the sidebar
st.sidebar.title('Chat')

# Add a checkbox to the sidebar
st.sidebar.checkbox('Display all')

#Main page

# Set the title of the app
st.title('Chat App')

with st.container(border=True):
    st.subheader("Navbar")

