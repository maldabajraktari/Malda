import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find('table', {'id': 'main_table_countries_today'})

    headers = [header.text.strip() for header in table.find_all('th')]

    rows = table.find_all('tr')[1:]  # Skip the header row

    data = []
    for row in rows:
        cols = row.find_all('td')
        country_data = [col.text.strip() for col in cols]
        data.append(country_data)


    df = pd.DataFrame(data, columns=headers)
    return df

covid_df = get_covid_data()
covid_df.head()
