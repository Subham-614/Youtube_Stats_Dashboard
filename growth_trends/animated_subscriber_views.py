import plotly.express as px
import numpy as np
import pandas as pd
def plot_animated_subscriber_views(df):
    # Filter out zero or extremely low values to avoid log-scale distortion
    filtered_df = df[(df['subscribers'] > 1000) & (df['video_views'] > 10000)]

    fig = px.scatter(
        filtered_df,
        x='subscribers',
        y='video_views',
        animation_frame='created_year',
        size='uploads',
        color='category',
        hover_name='youtuber',
        title='Subscriber vs Views Over Years (Animated Bubble Chart)',
        log_x=True,
        size_max=60,
        range_x=[1e3, filtered_df['subscribers'].max()*1.2],
        range_y=[filtered_df['video_views'].min()*0.8, filtered_df['video_views'].max()*1.1]
    )

    fig.update_layout(height=650)
    fig.update_traces(marker=dict(opacity=0.6))
    return fig
