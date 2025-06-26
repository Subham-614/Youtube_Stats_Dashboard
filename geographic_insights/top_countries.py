import plotly.express as px
import numpy as np
import pandas as pd
def plot_top_countries(df):
    # 🏆 2. Top 10 Countries by Total Subscribers
    top_countries = df.groupby('country')['subscribers'].sum().nlargest(10).reset_index()

    fig = px.bar(top_countries, 
                x='country', 
                y='subscribers',
                color='country',  # 🎨 Unique color per country
                title='Top 10 Countries by Total Subscribers',
                text='subscribers',
                color_discrete_sequence=px.colors.qualitative.Set1)  # Optional: clean palette

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(height=500, width=900, showlegend=False)
    fig.update_yaxes(tickformat=".1s")
    return fig
