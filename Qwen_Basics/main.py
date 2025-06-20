import streamlit as st
from langchain.llms import Ollama

# Set page title
st.set_page_config(page_title="⚡ Qwen 2.5 Chatbot")

# Load Qwen 2.5 model using Ollama on port 8000
# IMPORTANT: Make sure you have 'qwen2.5' pulled with Ollama
# You can do this by running 'ollama pull qwen2.5' in your terminal
llm = Ollama(
    model="qwen2.5",  # Change the model name to "qwen2.5"
    base_url="http://localhost:8000"  # Your Ollama custom port
)

st.title("⚡ Local Qwen 2.5 Chatbot with Ollama")
st.markdown("Ask me anything!")

# Input from user
user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = llm(user_input)
    st.success(response)
