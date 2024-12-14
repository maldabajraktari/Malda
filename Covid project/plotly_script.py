import plotly.express as px
import pandas as pd

def plot_top_10_countries(df=None):

    df['Total Cases'] = pd.to_numeric(df['Total Cases'].str.replace(",", ""), errors='coerce')
    df_sorted = df.sort_values(by='Total Cases', ascending=False).head(10)

    if df_sorted.empty:
        raise
    ValueError("DataFrame has no data after sorting and filtering")

    fig = px.bar(df_sorted, x='Country,Other', y='Total Cases',
                 labels={'Country,Other': 'Country', 'Total Cases': 'Total Cases'},
                 title="Top 10 Countries by COVID-19 Cases")
    return fig

data={
    'Country,Other': ['USA', 'India', 'Brazil', 'Russia', 'UK', 'France', 'Germany', 'Turkey', 'Italy', 'Spain'],
    'Total Cases': ['10000000', '9000000', '8500000','7500000', '7000000', '6500000', '6000000', '5500000', '5000000', '4500000']
    }
df = pd.DataFrame(data)
print(df)

fig = plot_top_10_countries(df)
fig.show()
