import plotly.express as px
import numpy as np
import pandas as pd
# 🎯 6. Outlier Detection: Top 1% Subscribers (Bar Chart)
def plot_outlier_detection(df):
    threshold = df['subscribers'].quantile(0.99)
    top_creators = df[df['subscribers'] >= threshold].sort_values('subscribers', ascending=False)

    fig = px.bar(top_creators.head(10), x='youtuber', y='subscribers',
                title='Top 1% YouTubers by Subscribers',
                text='subscribers', color='category')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(height=550, width=950)
    fig.update_yaxes(tickformat=".1s")
    return fig