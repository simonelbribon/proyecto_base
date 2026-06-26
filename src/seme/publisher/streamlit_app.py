import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/v1"

st.title("SEME Control Tower 🏯")

# 🧪 INPUT
text = st.text_input("Enviar evento SEME", "Fast API SEME")

if st.button("Disparar pipeline"):
    response = requests.post(
        f"{API_URL}/pipeline",
        json={"text": text}
    )

    st.subheader("Respuesta API")
    st.json(response.json())
