import streamlit as st
import time as time
import datetime as datetime

def mostrarResultados():
    st.subheader("Resultados")
    st.write("Cliente:", varCliente)
    st.write("Banco:", varBanco)
    st.write("Parcelas:", varParcelas)
    st.write("Data de Vencimento:", varData)
    st.write("Filial: ", varCheckbox)


with st.form('Formulário de seleçao de parâmetros.'):

    st.subheader("Formulário no Streamlit")
    varCliente = st.radio(
        "1-Selecione o cliente:",
        ("Space X", "Microsoft", "Apple", "Google", "Amazon")
    )
        
    varBanco = st.multiselect(
        "2-Selecione o banco:",
        ("Banco do Brasil", "Itaú", "Bradesco", "Santander", "Caixa")
    )
        
    varParcelas = st.slider(
        "3-Quantas parcelas deseja financiar? ", 0, 60, 20
    )
        
    varData = st.date_input(
        "4-Selecione a data do vencimento:",
        datetime.date(2022,1,1))
    varCheckbox = st.checkbox('Filial Campinas')
    
    with st.spinner("Carregando..."):
        time.sleep(1.5)
        st.success("Carregamento concluído!")

    
    botao_form = st.form_submit_button("Filtrar")
    '----------------------------------'
    
    if botao_form:
        st.success("Dados filtrados com sucesso!")
        mostrarResultados()