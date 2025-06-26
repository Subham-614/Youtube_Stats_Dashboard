import plotly.express as px
import numpy as np
import pandas as pd
def plot_top_10_youtubers(df):
    """
    Creates a bar chart showing top 10 YouTubers by subscriber count
    
    Args:
        df (pd.DataFrame): YouTube dataset with required columns
        
    Returns:
        plotly.graph_objects.Figure: Bar chart figure
    """
    
    # Get top 10 YouTubers by subscribers
    top_10_subs = df.sort_values(by='subscribers', ascending=False).head(10)
    
    # Create bar chart
    fig = px.bar(
        top_10_subs, 
        x='youtuber', 
        y='subscribers', 
        title='Top 10 YouTubers by Subscribers', 
        hover_data=['country', 'video_views'], 
        color='country',
        height=600
    )
    
    # Update y-axis formatting and range
    fig.update_yaxes(
        tickformat=".0s", 
        range=[0, top_10_subs['subscribers'].max() * 1.1]
    )
    
    # Additional styling for better appearance
    fig.update_layout(
        xaxis_title="YouTuber",
        yaxis_title="Subscribers",
        showlegend=True,
        xaxis_tickangle=-45
    )
    
    return fig