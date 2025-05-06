import altair as alt
import pandas as pd
import streamlit as st

fonte = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 187, 19, 87, 52],
})

st.title('Esse e o nosso dataset de exemplo')
fonte

graf_barras = alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a', 'b']
)
rotulo_barra = graf_barras.mark_text(
    dy = -8,
    size= 14,
).encode(
    text='b',
)

st.subheader('Plot do gráfico de barras:')
st.altair_chart(graf_barras+rotulo_barra, use_container_width=True)



graf_area = alt.Chart(fonte).mark_area(
    color='#FDC82F',
    interpolate='step-after',
    line=True,
    stroke='black',
    strokeWidth=1,
    opacity=0.5,
).encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)

rotulo_area = graf_area.mark_text(
    dy = -9,
    dx = 30,
    size= 14,
).encode(
    text='b',
)

st.subheader('Plot do gráfico de área:')
st.altair_chart(graf_area+rotulo_area, use_container_width=True)



graf_pizza = alt.Chart(fonte).mark_arc().encode(
    theta=alt.Theta(field='b', type='quantitative'),
    color=alt.Color(field='a', type='nominal'),
    tooltip=['a', 'b']
).properties(
    width=300,
    height=300
)

st.subheader('Plot do gráfico de pizza:')
st.altair_chart(graf_pizza, use_container_width=True)