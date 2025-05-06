import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_excel(
    io=r'C:\Users\paulo\Downloads\Streamlit\Datasets\faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15,
)

# Gráfico corrigido
graf_area = alt.Chart(df).mark_area(
    color = 'gray',
    line = {'color': 'black'},
    interpolate='monotone',
).encode(
    x=alt.X('Year:T'),  # ou o nome real da sua coluna de data/ano
    y=alt.Y('Value:Q')   # ou o nome real da sua coluna de valores
)

rotulo = graf_area.mark_text(
    size=12,
    color='black',
    align='center',
    dy = -20
    
).encode(text='Value')

st.subheader('KPI DE RESULTADOS ANUAIS')
st.altair_chart(graf_area+rotulo, use_container_width=True)

