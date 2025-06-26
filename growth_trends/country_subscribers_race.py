import plotly.express as px
import numpy as np
import pandas as pd
def plot_country_subscribers_race(df):
    fig = px.bar(df, 
                x="country", 
                y="subscribers", 
                color="country",
                animation_frame="created_year", 
                range_y=[0, df['subscribers'].max()],
                title="📈 Country-wise Subscribers Over Years (Animated Bar Race)")

    fig.update_layout(height=600)
    return fig
