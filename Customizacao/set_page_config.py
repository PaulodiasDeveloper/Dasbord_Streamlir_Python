import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(
    page_title="Os nomes mais ricos do mundo",
    page_icon="💰",
    layout="centered", # wide, centered, or narrow
    initial_sidebar_state="auto", # auto, expanded, or collapsed
    menu_items={
        'Get Help': 'https://www.extremelly.com',
        'Report a bug': "https://www.extremelly.com",
        'About': "# Olá, sou o Paulo! \n\n Esse Dashboad foi desenvolvido por mim. \n\n Você pode me perguntar qualquer coisa sobre Streamlit, Pandas, Altair e muito mais! \n\n Vamos começar?"
    }
)
# CONECTA NO ARQUIVO EXCEL E CONVERTE EM DATAFRAME
df = pd.read_excel(
    io = "../Datasets/faturamento.xlsx",
    engine="openpyxl",
    sheet_name="ricos",
    usecols="A:B",
    nrows=10,
)

# CRIA UM SIDEBAR PARA FILTRAR OS BILIÁRIOS NO DF E GRÁFICO
st.sidebar.header("Filtre Aqui:")
bilionários = st.sidebar.multiselect(
    "Selecione os Bilionários:",
    options=df["Nome"].unique(),
    default=df["Nome"].unique()
)
# CRIA UMA NOVA VERSÃO DO DF CONFORME FILTROS APLICADOS
df_filtrado = df.query(
    "Nome == @bilionários"
)

# BLOCO GRÁFICO PIZZA (GRÁFICO + RÓTULO + NOMES)
graf1 = alt.Chart(df_filtrado).mark_arc(innerRadius=0, outerRadius=150).encode(
    theta=alt.Theta(field="Fortuna", type="quantitative", stack=True),
    color=alt.Color(field="Nome", type="nominal"),
).properties(width=700, height=450)
rotuloNome = graf1.mark_text(radius=200, size=14).encode(text="Nome")
rotuloValor = graf1.mark_text(radius=160, size=14).encode(text="Fortuna")

# PLOTA O GRÁFICO NA TELA
st.write("# Gráfico de Pizza/Arco")
st.subheader("1- Os mais ricos do mundo")
st.altair_chart(graf1 + rotuloNome + rotuloValor, use_container_width=True)

df