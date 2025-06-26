# 📈 2. Subscribers vs. Video Views
import plotly.express as px
import numpy as np
import pandas as pd
def plot_subscribers_vs_views(df):
    # Filter low-end and outliers
    filtered_df = df[(df['subscribers'] > 1e6) & (df['video_views'] > 1e7)]

    fig = px.scatter(filtered_df,
                    x='subscribers',
                    y='video_views',
                    color='category',
                    hover_name='youtuber',
                    title='Subscribers vs Video Views (Filtered, Log Scale)')

    fig.update_layout(
        height=600,
        width=1000,
        xaxis_type='log',
        yaxis_type='log',
        xaxis_title='Subscribers (log scale)',
        yaxis_title='Video Views (log scale)'
    )
    return fig