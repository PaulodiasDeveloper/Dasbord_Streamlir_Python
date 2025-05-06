import streamlit as st
import pandas as pd
import numpy as np


st.header("Aula de DataFrame")
df = pd.DataFrame(
     np.random.randn(5,5),
     columns=('col %d' %i for i in range(5))
)
st.dataframe(df)
st.write(df)
st.write(df.describe())

st.subheader("Exemplo 2 - alterando dimensões")
st.dataframe(df, 500,250)

st.subheader("Exemplo 3 - Dando um destaque nos maiores valores")
st.dataframe(df.style.highlight_max(axis=0))

st.header("TABLE - Exemoplo similar ao DataFrame")
st.table(df)

# ==== Metrics ====
st.subheader("Exemplo 5 - Temperatura")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "20 °C", "1 °C")
col2.metric("Vento", "10 km/h", "-8%")
col3.metric("Humidade", "86%", "4%", delta_color="inverse")