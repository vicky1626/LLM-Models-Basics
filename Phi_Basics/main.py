import streamlit as st
from langchain.llms import Ollama

# Set page title
st.set_page_config(page_title="🧠 Phi 3 Chatbot")

# Load Phi model using Ollama on port 8000
# Ensure you have pulled the model using: `ollama pull phi3`
llm = Ollama(
    model="phi3",  # You can also try "phi3:mini" or "phi3:medium"
    base_url="http://localhost:8000"
)

st.title("🧠 Local Phi 3 Chatbot with Ollama")
st.markdown("Ask me anything!")

# Input from user
user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = llm(user_input)
    st.success(response)
