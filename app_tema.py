import streamlit as st
import datetime

st.header("Painel de Dados")

with st.sidebar:
    st.header("SELEÇÃO FILTRO")
    st.slider('Valor: ', 0, 100, 60)
    st.multiselect(
        'Cliente: ',
        ['N4', 'N5', 'N6', 'N7']
)
    
col1, col2 = st.columns(2)

with col1:
    d = st.date_input(
        "Quando é seu aniverário?",
        datetime.date(2000,7, 6))
with col2:
    st.slider('Valor: ', 0, 100, 50)
    