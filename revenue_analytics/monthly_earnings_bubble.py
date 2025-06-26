import plotly.express as px
import numpy as np
import pandas as pd
# 💵 4. Monthly Earnings vs Subscribers
def plot_monthly_earnings_bubble(df):
    fig = px.scatter(df,
                    x='subscribers',
                    y='highest_monthly_earnings',
                    size='video_views',
                    color='category',
                    hover_name='youtuber',
                    title='Monthly Earnings vs Subscribers (Bubble Chart)',
                    size_max=60)  # Controls the max bubble size

    # Layout adjustments
    fig.update_layout(
        height=650,
        width=1100,
        xaxis_title='Subscribers',
        yaxis_title='Highest Monthly Earnings'
    )

    # Optional: log scale for better spread if values are skewed
    fig.update_layout(
        xaxis_type='log',
        yaxis_type='log'
    )

    # Optional: Format axis ticks for better readability
    fig.update_xaxes(tickformat=".1s")
    fig.update_yaxes(tickformat=".1s")

    return fig
