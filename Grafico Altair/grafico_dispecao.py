import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv(r'C:\Users\paulo\Downloads\Streamlit\Datasets\vega_car.csv')

disper = alt.Chart(df).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon',
    color=alt.Color('Origin:N')
)

st.subheader('GRÁFICO DE DISPERSÃO: CONSUMO POR CAVALO')
st.altair_chart(disper, use_container_width=True)