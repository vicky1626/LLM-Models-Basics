import streamlit as st
from langchain.llms import Ollama

# Set page title
st.set_page_config(page_title="⚡ Mistral Chatbot")

# Load Mistral model using Ollama on port 8000
llm = Ollama(
    model="mistral", 
    base_url="http://localhost:8000"  # Your Ollama custom port
)

st.title("⚡ Local Mistral Chatbot with Ollama")
st.markdown("Ask me anything!")

# Input from user
user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = llm(user_input)
    st.success(response)
