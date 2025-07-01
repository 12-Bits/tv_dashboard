import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

st.subheader("Distribuição das Notas Médias")
fig, ax = plt.subplots()
sns.histplot(df_filtered["vote_average"], bins=20, ax=ax)
st.pyplot(fig)

st.subheader("Distribuição da Popularidade")
fig, ax = plt.subplots()   
sns.histplot(df_filtered["popularity"], bins=30)
plt.xscale('log')