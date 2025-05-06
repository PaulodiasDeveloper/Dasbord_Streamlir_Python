import streamlit as st
import time as time
import datetime as datetime


varModal = st.sidebar.selectbox(
    "Selecione o modal de transporte:",
    ("Aéreo", "Marítimo", "Rodoviário", "Ferroviário", "Outro")
)
st.write(f"Modal de transporte: {varModal}")


with st.sidebar:
    varCliente = st.radio(
        "Selecione o cliente:",
        ("Space X", "Microsoft", "Apple", "Google", "Amazon")
    )
    
    varBanco = st.multiselect(
        "Selecione o banco:",
        ("Banco do Brasil", "Itaú", "Bradesco", "Santander", "Caixa")
    )
    
    varParcelas = st.slider(
        "Selecione parcelas deseja financiar? ", 0, 60, 20
    )
    
    varData = st.date_input(
        "Selecione a data do vencimento:",
        datetime.date(2022,1,1)
    )
    with st.spinner("Carregando..."):
        time.sleep(1.5)
        st.success("Carregamento concluído!")
    
st.write(f"Cliente: {varCliente}")
st.write(f"Banco: {varBanco}")
st.write(f"Parcelas: {varParcelas}")
st.write(f"Data de vencimento: {varData}")
    