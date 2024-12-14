import pandas as pd
import streamlit as st
from fastapi import requests


def plot_top_10_countries(df):
    pass

def streamlit_app():
    st.title("COVID-19 Data Visualization")

    response = requests.get("http://127.0.0.1:8000/covid-data/")
    data = response.json()["covid_data"]

    df = pd.DataFrame(data)

    st.write("COVID-19 Data for Countries")
    st.dataframe(df)

    fig = plot_top_10_countries(df)
    st.plotly_chart(fig)


if __name__ == "__main__":
    streamlit_app