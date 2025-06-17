import streamlit as st
from langchain.llms import Ollama

# Set page title
st.set_page_config(page_title="🦙 LLaMA Chatbot")

# Load LLaMA model using Ollama on port 8000
llm = Ollama(
    model="llama3",
    base_url="http://localhost:8000"  # 👈 Custom port here
)

st.title("🦙 Local LLaMA Chatbot with Ollama")
st.markdown("Ask me anything!")

# Input from user
user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = llm(user_input)
    st.success(response)
