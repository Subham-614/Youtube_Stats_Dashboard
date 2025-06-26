import plotly.express as px
import numpy as np
import pandas as pd
def plot_animated_choropleth(df):
    fig = px.choropleth(df, 
                        locations="country", 
                        locationmode="country names",
                        color="subscribers",
                        animation_frame="created_year",
                        title="🌎 Animated Choropleth: Subscribers Growth by Country",
                        color_continuous_scale="Viridis")

    fig.update_layout(height=600)
    return fig
