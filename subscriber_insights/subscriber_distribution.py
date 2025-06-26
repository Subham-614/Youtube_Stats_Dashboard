import plotly.express as px
import numpy as np
import pandas as pd
def plot_subscriber_distribution(df):
    # 📦 3. Category-wise Subscriber Averages

    fig = px.box(df, 
                x='category', 
                y='subscribers', 
                title='Subscriber Distribution by Category')

    # Adjust layout size
    fig.update_layout(height=600, width=1100)

    # Optional: Rotate x-axis labels for readability
    fig.update_layout(xaxis_tickangle=-45)
    fig.update_layout(yaxis_type='log')
    fig.update_yaxes(title='Subscribers (log scale)', tickformat=".1s")


    return fig
