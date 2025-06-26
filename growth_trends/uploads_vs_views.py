import plotly.express as px
import numpy as np
import pandas as pd
def plot_uploads_vs_views(df):
    # 🔁 1. Uploads vs Views
    fig = px.scatter(df, x='uploads', y='video_views',
                    size='subscribers', color='category',
                    hover_name='youtuber',
                    title='Uploads vs. Video Views',
                    size_max=60)
    fig.update_layout(height=600, width=1000)
    fig.update_xaxes(tickformat=".1s")
    fig.update_yaxes(tickformat=".1s")
    return fig