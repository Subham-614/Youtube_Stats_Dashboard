import plotly.express as px
import numpy as np
import pandas as pd
def plot_youtubers_over_years(df):
    # 📅 6. YouTubers Created Over Years
    created_years = df['created_year'].value_counts().sort_index()
    fig = px.line(x=created_years.index, y=created_years.values, 
                labels={'x': 'Year', 'y': 'Number of Channels'}, 
                title='Number of YouTubers Created Per Year')
    return fig