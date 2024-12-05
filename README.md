# Basic LLM Chat App

This is a simple application, combining Steamlit and Groq API to connect with AI models.
You could chose model and temperature for your chat. Models are not fine tuned.

## Project content
- **app.py** - main page
- **pages/chat.py** - chat page
- **requirements.txt** - list of libs
- **.streamlit/secrets.toml.example** - example of sectrets settings

## Installation

1. Copy repository.
2. Create Python Environment (venv) in VS Code. 
3. Register in [Groq.com](https://console.groq.com/) and create an API key
4. Rename **secrets.toml.example** to **secrets.toml**
5. Save your API key in **secrets.toml**
6. Install the packages: `pip install -r requiements.txt`
7. Run the app: `streamlit run app.py`

# Deployed app

[MiniChat](https://minichat.streamlit.app/)