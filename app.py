import gradio as gr
from sentence_transformers import SentenceTransformer

# Load the sentence transformer
sentence_transformer = 'all-MiniLM-L6-v2'
embedding_model = SentenceTransformer(sentence_transformer)

def foo(message, history):
    embedding = embedding_model.encode(message)
    return "I don't know what to do!"

demo = gr.ChatInterface(
    fn=foo,
    type="messages"
)

if __name__ == "__main__":
    demo.launch(share=True)