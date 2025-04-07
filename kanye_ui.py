import streamlit as st
import requests

st.title("🎤 Kanye Quote Generator")

if st.button("Get a Kanye Quote"):
    response = requests.get("https://api.kanye.rest")
    if response.status_code == 200:
        quote = response.json()["quote"]
        st.success(f"Kanye says: \"{quote}\"")
    else:
        st.error("Kanye is silent today.")

