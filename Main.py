import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from data_loader import load_data

st.set_page_config(page_title="Dashboard de Séries de TV", layout="wide")

#Chama a função de carregamento de dados
df = load_data()

# Sidebar - filtros
st.sidebar.title("Filtros")
selected_country = st.sidebar.multiselect("País de origem", sorted(df["origin_country"].unique()), default=df["origin_country"].unique())
selected_language = st.sidebar.multiselect("Idioma original", sorted(df["original_language"].unique()), default=df["original_language"].unique())
min_year, max_year = int(df["year"].min()), int(df["year"].max())
selected_year = st.sidebar.slider("Ano de estreia", min_year, max_year, (min_year, max_year))

df_filtered = df[
    df["origin_country"].isin(selected_country) &
    df["original_language"].isin(selected_language) &
    df["year"].between(selected_year[0], selected_year[1])
]

st.sidebar.title("Navegação")

st.title("Dashboard - Séries de TV")
st.markdown("Este é um dashboard interativo para explorar dados de séries de TV.")
st.markdown("Filtre os dados usando a barra lateral para visualizar séries por país de origem, idioma e ano de estreia.")
st.markdown("Use a barra lateral acessar novas páginas.")


st.markdown("Dataframe carregado: `data_TV.csv` de https://www.kaggle.com/datasets/bourdier/all-tv-series-details-dataset")


# Exibe o DataFrame Puro
st.dataframe(df)
