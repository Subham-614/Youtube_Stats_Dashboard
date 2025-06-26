import plotly.express as px
import numpy as np
import pandas as pd
def plot_top_categories(df):
    top_categories = df['category'].value_counts().nlargest(6)
    fig = px.pie(names=top_categories.index, values=top_categories.values,
                hole=0.4, title='Top 6 Categories by YouTuber Count')
    fig.update_traces(textinfo='percent+label')
    return fig