import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = r'C:\Users\paulo\Downloads\Streamlit\Datasets\faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'ricos',
    usecols = 'A:B',
    nrows= 9
)

st.title('GRÁFICO PIZZA - MAIS RICOS DO MUNDO')

graf_pizza = alt.Chart(df).mark_arc(
    innerRadius=0,
    outerRadius=150
).encode(
    theta = alt.Theta(field='Fortuna', type='quantitative', stack=True),
    color = alt.Color(field='Nome', type='nominal', legend=None),
    tooltip = ['Nome', 'Fortuna']
).properties(
    width=900,
    height=550
)

rotuloNome = graf_pizza.mark_text(radius=230, size=14).encode(text='Nome:N')
rotuloValor = graf_pizza.mark_text(radius=170, size=14).encode(text='Fortuna:Q')

st.altair_chart(graf_pizza+rotuloNome+rotuloValor, use_container_width=True)