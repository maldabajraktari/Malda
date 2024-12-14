from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
@app.get("/")

class CountryData(BaseModel):
    country: str
    total_cases: int
    total_deaths: int
    total_recovered: int


def get_covid_data():
    pass


@app.get("/covid-data/")
def get_data():

    df = get_covid_data()
    df = df[['Country,Other', 'Total Cases', 'Total Deaths', 'Total Recovered']]
    df.columns = ['Country', 'Total Cases', 'Total Deaths', 'Total Recovered']
    df = df.dropna()
    data = df.to_dict(orient="records")
    return {"covid_data": data}

