import plotly.express as px
import numpy as np
import pandas as pd
def plot_urban_population_bubble(df):
    urban_df = df.groupby('country').agg({
        'urban_population': 'first',
        'subscribers': 'sum'
    }).reset_index()

    fig = px.scatter(urban_df, 
                    x='urban_population', 
                    y='subscribers',
                    size='subscribers',
                    hover_name='country',
                    title='Urban Population vs Total Subscribers (Log Scale)',
                    size_max=50,
                    log_x=True,
                    log_y=True)  # 🔑 log scale

    fig.update_layout(
        height=600,
        width=1000,
        xaxis_title="Urban Population (log scale)",
        yaxis_title="Total Subscribers (log scale)"
    )
    return fig
