import plotly.express as px
import numpy as np
import pandas as pd
def plot_category_country_sunburst(df):
    fig = px.sunburst(df, path=['category', 'country', 'youtuber'], values='subscribers',
                    title='Sunburst: Category → Country → YouTuber (by Subscribers)')
    fig.update_layout(height=700)
    return fig