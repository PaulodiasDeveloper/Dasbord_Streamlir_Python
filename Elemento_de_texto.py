import streamlit as st


st.title("Elemento de Texto")
st.header("Header do ST")
st.subheader("Subheader do ST")

st.markdown("## Markdown do ST")
st.markdown("### Markdown do ST")
st.markdown("#### Markdown do ST")
st.markdown("##### Markdown do ST")
st.markdown("###### Markdown do ST")
st.markdown("**Negrito**")
st.markdown("*Itálico*")
st.markdown("~~Riscado~~")
st.markdown("`Código`")
st.markdown("```python\nprint('Hello World')\n```")
st.markdown("```python\nprint('Hello World')\n```", unsafe_allow_html=True)
st.markdown("```python\nprint('Hello World')\n```", unsafe_allow_html=False)

st.caption("Caption do ST")

# Code
code = '''
if(fome > 0 ):
    return "Ir para a cozinha"
else:
    return "Ficar na sala"
'''
st.code(code, language='python')

st.text("Texto do ST")

# Latex https://www.latex-project.org/docs/supportted.html
st.latex(r'''a^2 + b^2 = c^2''')