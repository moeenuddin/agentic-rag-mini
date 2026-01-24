import streamlit as st
from agent import agent
import asyncio

st.set_page_config(page_title="Agentic RAG Mini", layout="centered")

st.title("📄 Agentic Document Assistant")
st.caption("Answers only when confident — otherwise asks for clarification")

query = st.text_input("Ask a question about the document")

if query:
    with st.spinner("Thinking..."):
        response = asyncio.run(agent.run(query)) #agent.run(query)
        st.markdown("### 🤖 Agent Response")
        st.write(response)
