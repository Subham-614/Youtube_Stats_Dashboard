import plotly.express as px
import numpy as np
import pandas as pd
def plot_revenue_distribution(df):
    # 📉 7. Revenue Distribution

    # Optional: cap outliers at 99th percentile
    cap = df['highest_yearly_earnings'].quantile(0.99)
    filtered_df = df[df['highest_yearly_earnings'] <= cap]

    fig = px.histogram(filtered_df, 
                    x='highest_yearly_earnings', 
                    nbins=50,
                    title='Distribution of Highest Yearly Earnings (Capped at 99th Percentile)')

    fig.update_layout(
        height=600,
        width=1000,
        xaxis_title='Highest Yearly Earnings',
        yaxis_title='Number of YouTubers'
    )

    fig.update_xaxes(tickformat=".1s")

    return fig
