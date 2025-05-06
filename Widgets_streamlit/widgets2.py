import pandas as pd
import streamlit as st

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='Interação',
    usecols='B:C',
    nrows=40,
)

st.subheader('Radio Button')
tipoRelatorio = st.radio(
    'Selecione o tipo de relatório',
    ('Mensal', 'Semestral', 'Anual'))
st.write('Você seleciou o tipo: ',tipoRelatorio)



st.subheader('Caixa de Seleção')
opcoes = st.selectbox(
    'Selecione a materia-prima para análise',
    ('Ferro', 'Aço', 'Alumínio', 'Cobre', 'Plástico'))
st.write('Você selecionou a matéria-prima: ',opcoes)


st.subheader('Caixa de Seleção Múltipla')
multi = st.multiselect(
    'Selecione o banco para consulta',
    ['Banco do Brasil', 'Itaú', 'Bradesco', 'Santander'])
st.write('Você selecionou os bancos: ', multi)