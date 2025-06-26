import plotly.express as px
import numpy as np
import pandas as pd
def plot_animated_growth_scatter(df):
    fig = px.scatter(df, 
                    x="video_views", 
                    y="subscribers", 
                    animation_frame="created_year",
                    size="highest_monthly_earnings", 
                    color="category", 
                    hover_name="youtuber",
                    title="📽️ Animated Scatter: YouTubers' Growth Over Time",
                    log_x=True, log_y=True)  # Apply log scale

    fig.update_traces(marker=dict(opacity=0.6))
    fig.update_layout(height=650)
    return fig