import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = r'C:\Users\paulo\Downloads\Streamlit\Datasets\normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87,
)


if st.button("Reiniciar"):
    st.rerun()
if st.button("Parar"):
    st.stop()


Histograma = alt.Chart(df).mark_bar().encode(
    x = alt.X('x', bin=alt.Bin(step=5)),
    y = 'sum(count)'
)

st.subheader('HISTOGRAMA - NOTAS DE 1000 ALUNOS')
st.altair_chart(Histograma, use_container_width=True)

df