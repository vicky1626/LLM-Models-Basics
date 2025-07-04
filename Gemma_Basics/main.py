import gradio as gr
from langchain.llms import Ollama

# Load Gemma 2 model (make sure it's pulled via `ollama pull gemma2:2b`)
llm = Ollama(
    model="gemma2:2b",  # or "gemma2:9b", "gemma2:27b"
    base_url="http://localhost:8000"
)

# Define response function
def chat_with_gemma(prompt):
    return llm(prompt)

# Launch Gradio interface
iface = gr.Interface(
    fn=chat_with_gemma,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs="text",
    title="💎 Local Gemma 2 Chatbot",
    description="Powered by Ollama + LangChain + Gradio"
)

iface.launch()
