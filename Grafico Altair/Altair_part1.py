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
rotulo = graf_barras.mark_text(
    dy = -8,
    size= 14,
).encode(
    text='b',
)

st.subheader('Plot do gráfico de barras:')
st.altair_chart(graf_barras+rotulo, use_container_width=True)