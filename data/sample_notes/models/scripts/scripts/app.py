import streamlit as st
from scripts.query_engine import ask_question

st.set_page_config(page_title="Custom Knowledge Assistant", page_icon="🧠")
st.title("🧠 Custom Knowledge Assistant")
st.markdown("Ask questions based on your personal notes (Markdown, PDF, Notion).")

query = st.text_input("What would you like to know?")
if query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
        st.success(answer)
