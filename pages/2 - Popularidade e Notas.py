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

st.subheader("Popularidade vs Nota Média")
fig = px.scatter(df_filtered, x="vote_average", y="popularity", hover_data=["name"],
                labels={"vote_average": "Nota Média", "popularity": "Popularidade"},
                title="Popularidade x Nota")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Séries Mais Votadas (Filtrado por idioma)")
idioma = st.selectbox("Filtrar por idioma", df_filtered["original_language"].unique())
top_voted = df_filtered[df_filtered["original_language"] == idioma].sort_values("vote_count", ascending=False).head(10)
fig2 = px.bar(top_voted, x="name", y="vote_count", title=f"Top 10 - Idioma {idioma}")
st.plotly_chart(fig2, use_container_width=True)
