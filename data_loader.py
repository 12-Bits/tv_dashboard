
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/data_TV.csv") 
    df["first_air_date"] = pd.to_datetime(df["first_air_date"]).dt.date  # <-- remove hora
    df["year"] = pd.to_datetime(df["first_air_date"]).dt.year  #  converte de novo para datetime
    df = df[df["origin_country"] != "Unknown"]
    
    return df
