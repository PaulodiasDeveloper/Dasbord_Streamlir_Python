import pandas as pd
import streamlit as st
import datetime

st.subheader("Slider")
parcelas = st.slider(
    'Com quantas parcelas deseja simular?', 0, 60,30)
st.write("Você seecionou", parcelas, 'parcelas')

intervalo = st.slider(
    'Qual intervalo desejado?',
    0.0, 100.0, (25.0, 75.0))
st.write('intervalo: ', intervalo)


st.subheader("Slider")
d = st.date_input(
    'Selecione a data',
    datetime.date(2022, 1, 1),
)
st.write('Data selecionada:', d)

