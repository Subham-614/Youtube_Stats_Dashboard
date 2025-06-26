import plotly.express as px
import numpy as np
import pandas as pd
def plot_country_choropleth(df):
    country_group = df.groupby("country").agg({"subscribers": "sum"}).reset_index()

    fig = px.choropleth(country_group, locations="country", locationmode="country names",
                        color="subscribers", hover_name="country",
                        title="Total Subscribers by Country",
                        color_continuous_scale="Reds")
    fig.update_layout(height=600, width=1000)
    return fig