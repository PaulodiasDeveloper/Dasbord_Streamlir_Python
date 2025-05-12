# 💹 Dashboard de Vendas

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit** para visualização e análise de dados de vendas, permitindo a filtragem por vendedor, produto e cliente. Os gráficos são gerados com **Altair**, proporcionando uma interface clara, informativa e moderna.

---

## 📊 Funcionalidades

- **Filtros interativos** na barra lateral:
  - Vendedor
  - Produto
  - Cliente
- **Indicadores principais**:
  - Total de Vendas
  - Margem Total
  - Porcentagem de Margem
- **Gráficos e visualizações**:
  - Quantidade e valor vendido por produto
  - Vendas por vendedor (gráfico de rosca)
  - Vendas por cliente
  - Evolução mensal das vendas

---

## 🧰 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) – Framework para criação de apps em Python.
- [Pandas](https://pandas.pydata.org/) – Manipulação e análise de dados.
- [Altair](https://altair-viz.github.io/) – Biblioteca declarativa para visualização de dados.
- [Pillow (PIL)](https://python-pillow.org/) – Processamento de imagem (logo na sidebar).

---

## 📁 Estrutura do Projeto

```text
├── dashboard_vendas.py
├── Datasets/
│   └── system_extraction.xlsx
├── Mídia/
│   └── logo vizion.png
└── README.md
```

## ▶️ Como Executar

1. Clone este repositório:

```
git clone https://github.com/seu-usuario/dashboard-vendas.git
cd dashboard-vendas
```

2. Crie um ambiente virtual (opcional mas recomendado):
   
```python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Instale as dependências:
   
```
pip install -r requirements.txt
```
4. Execute o aplicativo:
```
streamlit run dashboard_vendas.py
```
---
✅ Pré-requisitos

- Python 3.7+

- Arquivo Excel com os dados de vendas (system_extraction.xlsx)

  - Planilha: salesreport

  - Colunas esperadas: Vendedor, Produto vendido, Cliente, Valor Pedido, Margem Lucro, Quantidade, Data, etc.

---

📌 Observações
- O dashboard está otimizado para rodar localmente, mas pode ser facilmente implantado no Streamlit Cloud ou similar.

- Certifique-se de que o caminho do arquivo e das imagens esteja correto.
---
👤 Autor

Paulo Roberto

Desenvolvedor do projeto e responsável pelas análises.

---

https://github.com/user-attachments/assets/7ac3680e-93db-43b0-a105-e11cd373d3c7