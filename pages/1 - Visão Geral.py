import streamlit as st
import plotly.express as px
from data_loader import load_data 



df = load_data()
df = df[df["origin_country"] != "Unknown"]

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
st.title("Dashboard de Séries de TV")


st.subheader("Séries por País")
country_count = df_filtered["origin_country"].value_counts().head(10)
country_count = country_count.sort_values(ascending=True)  # Ordem decrescente no gráfico (barra maior no topo)
st.bar_chart(country_count)


st.subheader("Séries por Idioma")
lang_count = df_filtered["original_language"].value_counts().head(10)
lang_count = lang_count.sort_values(ascending=True)
st.bar_chart(lang_count)

st.subheader("Número de Séries por Ano")
series_by_year = df_filtered["year"].value_counts().sort_index()
fig = px.bar(x=series_by_year.index, y=series_by_year.values, labels={"x": "Ano", "y": "Quantidade"})
st.plotly_chart(fig, use_container_width=True)
