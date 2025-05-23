import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title = "Menu Principal",
        options = ["Início", "Vendas", "Relatórios", "Dashboards", "Suporte" ],
        icons = ["house", "basket", "bandaid", "bar-chart", "bell"],
        menu_icon = "cast",	
        default_index = 0,
)
    
selected_horizontal = option_menu(
    menu_title = "Menu Principal",
    options = ["Início", "Vendas", "Relatórios", "D.boards", "Suporte" ],
    icons = ["house", "basket", "bandaid", "bar-chart", "bell"],
    menu_icon = "cast",	
    default_index = 0,
    orientation = "horizontal",
    styles = {
        "container": {"padding": "0!important", "background-color": "#fafafa", "width": "100%"},
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {
            "font-size": "15px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#02ab21"},
    },
)