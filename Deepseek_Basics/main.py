import gradio as gr
from langchain.llms import Ollama

# List of models you want to support
AVAILABLE_MODELS = [
    "deepseek-llm:7b-chat",
    "deepseek-r1:7b",
    "deepseek-r1:14b",
    "deepseek-v2.5:236b",
    "deepseek-coder-v2",
    "deepseek-v3:671b"
]

# Define the interaction function
def chat_with_model(prompt, model_name):
    llm = Ollama(
        model=model_name,
        base_url="http://localhost:8000"  # Change if needed
    )
    return llm(prompt)

# Gradio UI
gr.Interface(
    fn=chat_with_model,
    inputs=[
        gr.Textbox(lines=2, placeholder="Ask me anything..."),
        gr.Dropdown(choices=AVAILABLE_MODELS, label="Select Model", value="deepseek-llm:7b-chat")
    ],
    outputs="text",
    title="🧠 DeepSeek Multi-Model Chatbot",
    description="Choose a model and chat! Powered by Ollama + LangChain + Gradio"
).launch()
