import plotly.express as px
import numpy as np
import pandas as pd
def plot_top_youtubers_growth(df):

    # 1. Get Top 10 YouTubers by final subscriber count
    top10_youtubers = df.sort_values("subscribers", ascending=False).head(10)["youtuber"].tolist()

    # 2. Filter dataset to only these youtubers
    df_top10 = df[df["youtuber"].isin(top10_youtubers)]

    # 3. Create the animated bar chart
    fig = px.bar(df_top10.sort_values("created_year"), 
                x="subscribers", 
                y="youtuber", 
                color="youtuber",
                animation_frame="created_year",
                orientation='h',
                hover_name="youtuber",
                title="🏆 Top 10 YouTubers' Subscriber Growth Over the Years",
                range_x=[0, df_top10["subscribers"].max()*1.1],
                height=600)

    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig