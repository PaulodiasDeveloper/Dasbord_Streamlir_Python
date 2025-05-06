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

# =============================

graf_barras_novo = alt.Chart(fonte).mark_bar(
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
    size=40,
).encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a', 'b']   
).encode(
    x=alt.X('a', sort='y'),
    y = 'b',
    color = alt.condition(
        alt.datum.b > 43,
        alt.value('orange'),  # color for values greater than 50
        alt.value('steelblue')  # color for values less than or equal to 50
    ),
)
rotulo = graf_barras_novo.mark_text(
    align='center',
    baseline='middle',
    size= 14,
    dy = -8,
).encode(text='b')

linha_media = alt.Chart(fonte).mark_rule(color='red').encode(
    y='mean(b)',
)

st.altair_chart(graf_barras_novo+rotulo+linha_media, use_container_width=True)