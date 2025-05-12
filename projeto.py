import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


# --- Configurações da página
st.set_page_config(
    page_title='DASHBOARD DE VENDAS',
    page_icon='💹',
    layout='wide',
    initial_sidebar_state='expanded', 
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/paulo-roberto/',
        'Report a bug': 'https://www.linkedin.com/in/paulo-roberto/',
        'About': 'Dashboard de Vendas.'	
    }
)

# --- Criar o dataset
df = pd.read_excel(
    io = './Datasets/system_extraction.xlsx',
    engine = 'openpyxl',
    sheet_name='salesreport',
    nrows=4400
)

# --- Criar sidebar

with st.sidebar:
    logo_teste = Image.open('./Mídia/data.png')
    st.image(logo_teste, width=300)
    st.subheader('Menu - DASHBOARD DE VENDAS')
    fVendedor = st.selectbox(
        "Selecione o Vendedor",
        options=df['Vendedor'].unique()
    )
    fProduto = st.selectbox(
        "Selecione o Produto",
        options=df['Produto vendido'].unique()
    )
    fCliente = st.selectbox(
        "Selecione o Cliente",
        options=df['Cliente'].unique()
    )
    
# Tabela quantidade vendida por vendedor
tab1_qtd_produto = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Cliente'] == fCliente) 
]
tab1_qtd_produto = tab1_qtd_produto.groupby('Produto vendido').sum(numeric_only=True).reset_index()

# Tabela de Vendas e Margem
tab2_vendas_margem = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente) 
]

# Tabela Vendas por Vendedor
tab3_vendas_vendedor = df.loc[
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente) 
]
tab3_vendas_vendedor = tab3_vendas_vendedor.groupby('Vendedor').sum(numeric_only=True).reset_index()
tab3_vendas_vendedor = tab3_vendas_vendedor.drop(columns=['Nº pedido', 'Preço'])

# Tabela Vendas por Cliente
tab4_vendas_cliente = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto) 
]
tab4_vendas_cliente = tab4_vendas_cliente.groupby('Cliente').sum(numeric_only=True).reset_index()


# Vendas Mensais
tab5_vendas_mensais = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente) 
]
tab5_vendas_mensais['mm'] = tab5_vendas_mensais['Data'].dt.strftime('%m/%y')

# ==== Padrões ====
cor_grafico = '#00B2A9'
altura_grafico = 250

# Gráfico 1 quantidade vendida por produto
graf1_qtd_produto = alt.Chart(tab1_qtd_produto).mark_bar(
    color = cor_grafico,
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
).encode(
    x = 'Produto vendido',
    y = 'Quantidade',
    tooltip = ['Produto vendido', 'Quantidade']
).properties(height=altura_grafico, title='Quantidade Vendida por Produto'
).configure_axis(grid=False).configure_view(strokeWidth=0)


# Gráfico 1 Valor da venda por produto
graf1_valor_produto = alt.Chart(tab1_qtd_produto).mark_bar(
    color = cor_grafico,
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
).encode(
    x = 'Produto vendido',
    y = 'Quantidade',
    tooltip = ['Produto vendido', 'Valor Pedido']
).properties(height=altura_grafico, title='Valor Total por Produto'
).configure_axis(grid=False).configure_view(strokeWidth=0)


# Tabela Vendas por vendedor / Gráfico de rosca
graf2_vendas_vendedor = alt.Chart(tab3_vendas_vendedor).mark_arc(
    innerRadius=100,
    outerRadius=150,
).encode(
    theta=alt.Theta(field="Valor Pedido", type="quantitative", stack=True),
    color=alt.Color(
        field="Vendedor", 
        type="nominal",
        legend=None
    ),
    tooltip=['Vendedor', 'Valor Pedido']
).properties(height=500, width=560, title='Vendas por Vendedor')
rot2Ve = graf2_vendas_vendedor.mark_text(radius=210, size=14).encode(text=alt.Text('Vendedor:N'))
rot2Vp = graf2_vendas_vendedor.mark_text(radius=180, size=12).encode(text=alt.Text('Valor Pedido:Q'))

# Vendas por cliente / Gráfico de barras
graf4_vendas_cliente = alt.Chart(tab4_vendas_cliente).mark_bar(
    color = cor_grafico,
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
).encode(
    x = 'Cliente',
    y = 'Valor Pedido',
    tooltip = ['Cliente', 'Valor Pedido']
).properties(height=altura_grafico, title='Vendas por Cliente'
).configure_axis(grid=False).configure_view(strokeWidth=0)


# Vendas por cliente / Gráfico de linhas
graf5_vendas_mensais = alt.Chart(tab5_vendas_mensais).mark_line(
    color = cor_grafico,
    point = True
).encode(
    alt.X('month(Data):T', title='Data'),
    y = 'Valor Pedido:Q',
    tooltip = ['mm', 'Valor Pedido']
).properties(height=altura_grafico, title='Vendas Mensais').configure_axis(grid=False).configure_view(strokeWidth=0)



# Página principal
total_vendas = round(tab2_vendas_margem['Valor Pedido'].sum(), 2)
total_margem = round(tab2_vendas_margem['Margem Lucro'].sum(), 2)
porc_margem = int(100 * total_margem / total_vendas)


st.header(':bar_chart: Dashboard de Vendas')

# 
dst1, dst2, dst3, dst4 = st.columns([1, 1, 1, 2.5])
with dst1:
    st.write('**VENDAS TOTAIS:**')
    st.info(f'R$ {total_vendas}')
with dst2:
    st.write('**MARGEM TOTAL:**')
    st.info(f'R$ {total_margem}')
with dst3:
    st.write('**MARGEM %:**')
    st.info(f'{porc_margem} %')
st.markdown('---')
    
# Colunas para os gráficos
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.altair_chart(graf4_vendas_cliente, use_container_width=True)
    st.altair_chart(graf5_vendas_mensais, use_container_width=True)

with col2:
    st.altair_chart(graf1_qtd_produto, use_container_width=True)
    st.altair_chart(graf1_valor_produto, use_container_width=True)

with col3:
    st.altair_chart(graf2_vendas_vendedor+rot2Ve+rot2Vp, use_container_width=True)

st.markdown('---')


