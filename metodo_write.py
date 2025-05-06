import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.write("Este é um texto")

st.write(pd.DataFrame({
    'Coluna A': [1, 2, 3, 4, 5],
    'Coluna B': ["Cachorro", "Gato", "Pato", "Cavalo", "Peixe"],
}))

array = [1, 2, "abc", "Paulo", True]
st.write('Aqui temos um array', array)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a',
    y='b',
    color='c',
    size='c',
    tooltip=['a', 'b', 'c'])

st.write(df)
st.write(c)