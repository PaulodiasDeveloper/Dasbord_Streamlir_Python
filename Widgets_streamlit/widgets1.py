import pandas as pd
import streamlit as st


df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='Interação',
    usecols='B:C',
    nrows=40,
)

st.subheader('Botão')
if st.button('Clique aqui para ver o gráfico'):
    st.write('Você clicou no botão!')
    

def convert_df(df):
    return df.to_csv().encode('utf-8')
st.subheader('Botão de download')
st.download_button(
    label='Baixar dados em CSV',
    data=convert_df(df),
    file_name='df.csv',
    mime='text/csv'
)


st.subheader('Caixa de seleção')
selected = st.checkbox('Marque a caixa')
if selected:
    st.write('Você marcou a caixa!')
    