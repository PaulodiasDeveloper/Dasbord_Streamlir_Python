import streamlit as st

st.subheader("Trabalhando com Formato JSON")

meuObjeto = {
    "banana": "Amarela",
    "laranja": "Laranja",
    "uva": "Roxa",
    "maça": "Verde",
}

st.json(meuObjeto)
   