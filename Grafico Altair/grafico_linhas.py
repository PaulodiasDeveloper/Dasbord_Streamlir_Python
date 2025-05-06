import streamlit as st
import pandas as pd
import altair as alt

vendas = pd.DataFrame({
    'Month': ['01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun', '07-Jul', '08-Aug', '09-Sep', '10-Oct', '11-Nov', '12-Dec'],
    'product_A': [30, 10, 80, 20, 40, 15, 35, 25, 78, 45, 23, 87],
    'product_B': [93, 68, 79, 84, 81, 97, 109, 99, 125, 115, 120, 88]
})

st.subheader('Gráfico de linhas: A & B')

graf_linha_A = alt.Chart(vendas).mark_line(
    point=alt.OverlayMarkDef(color='red', size=100, filled=False, fill='white'),
    color='red'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_A',
    axis=alt.Axis(grid=False),
    scale=alt.Scale(domain=(0, 160))),
    tooltip = ['Month', 'product_A', 'product_B']
    
).properties(
    title={
        'text': 'Vendas mensais dos Produtos A e B por Mês', 
        'anchor': 'middle'
    },
    width=600,
    height=400,
)


    
graf_linha_B = alt.Chart(vendas).mark_line(
    point=alt.OverlayMarkDef(color='blue', size=100, filled=False, fill='white'),
    color='blue'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_B'),
    tooltip = ['Month', 'product_A', 'product_B']
)


rotulo_B = graf_linha_B.mark_text(
    dy=-15,
    size=12,
).encode(
    text='product_B'
)

rotulo_A = graf_linha_A.mark_text(
    dy=-15,
    size=12,
).encode(
    text='product_A'
)
    



st.altair_chart(graf_linha_A+graf_linha_B+rotulo_A+rotulo_B, use_container_width=True)
