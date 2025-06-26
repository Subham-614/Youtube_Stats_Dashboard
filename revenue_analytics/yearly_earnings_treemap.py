import plotly.express as px
import numpy as np
import pandas as pd
def plot_yearly_earnings_treemap(df):
    fig = px.treemap(df, path=['category', 'youtuber'], values='highest_yearly_earnings',
                    title='Treemap of Yearly Earnings by Category and YouTuber')
    fig.update_layout(height=700)
    return fig