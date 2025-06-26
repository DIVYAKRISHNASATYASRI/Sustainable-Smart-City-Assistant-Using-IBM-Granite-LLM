import streamlit as st
import requests

st.title("🗣️ Smart City Chat Assistant")

query = st.text_input("Ask the City Assistant something:")
if st.button("Send"):
    res = requests.post("http://localhost:8000/chat", json={"query": query})
    st.write("**Response:**")
    st.write(res.json()["response"])