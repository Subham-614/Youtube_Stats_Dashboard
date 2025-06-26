import plotly.express as px
import numpy as np
import pandas as pd
def plot_channel_type_revenue(df):
    # 🧮 3. Channel Type vs. Revenue (Bar Chart)
    channel_rev = df.groupby('channel_type')['highest_yearly_earnings'].mean().sort_values(ascending=False).reset_index()

    fig = px.bar(channel_rev, x='channel_type', y='highest_yearly_earnings',
                title='Average Highest Yearly Earnings by Channel Type',
                text='highest_yearly_earnings', color='channel_type')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(height=500, width=950)
    fig.update_yaxes(tickformat=".1s")
    return fig