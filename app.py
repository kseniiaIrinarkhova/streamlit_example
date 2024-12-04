import streamlit as st

# Set the title of the app
st.title('My First Chat App')

# Add a header
st.header('Welcome to my chat app!')

# Add some text
st.write('This is a simple Streamlit app to get started.')

# Add a slider
slider_value = st.slider('Select a value', 0, 100, 50)
st.write('Selected value:', slider_value)

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Add a text input
user_input = st.text_input('Enter some text')
st.write('You entered:', user_input)