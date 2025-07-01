import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Dashboard de Séries de TV", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data\data_TV.csv")
    df["first_air_date"] = pd.to_datetime(df["first_air_date"])
    df["year"] = df["first_air_date"].dt.year
    df = df[df["origin_country"] != "Unknown"]
    return df

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
st.markdown("Dataframe carregado: `data_TV.csv`")

df = pd.read_csv("data\data_TV.csv")

# Exibe o DataFrame formatado no Streamlit
st.dataframe(df)