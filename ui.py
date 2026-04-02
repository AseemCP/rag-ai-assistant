import streamlit as st
from app import rag_model
st.title("Exam Agent")



uploded_file = st.file_uploader("Upload the Documents")

if uploded_file:
    with open("temp.pdf","wb") as f:
        f.write(uploded_file.read())
    st.write("PDF loaded Successfully")
query = st.chat_input("Enter your question")
if query:
    response = rag_model(query)
    st.chat_message("assistant").write(response.content)