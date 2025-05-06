import streamlit as st

st.header("Expander")
st.line_chart({"data": [1, 5, 2, 2, 1]})

with st.expander("Ver detalhes"):
    st.write("""
        Esse é um exemplo de Expamder.
        Você vai ver como usá-lo.""")
    st.image("../Mídia/dice.jpg")

