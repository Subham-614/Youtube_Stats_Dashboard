import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import visualization functions from different folders
from overview.top_10_youtubers import plot_top_10_youtubers
from overview.subscribers_vs_views import plot_subscribers_vs_views
from overview.top_categories import plot_top_categories

from subscriber_insights.subscriber_distribution import plot_subscriber_distribution
from subscriber_insights.outlier_detection import plot_outlier_detection
from subscriber_insights.channel_type_revenue import plot_channel_type_revenue

from revenue_analytics.monthly_earnings_bubble import plot_monthly_earnings_bubble
from revenue_analytics.revenue_distribution import plot_revenue_distribution
from revenue_analytics.yearly_earnings_treemap import plot_yearly_earnings_treemap

from geographic_insights.top_countries import plot_top_countries
from geographic_insights.country_choropleth import plot_country_choropleth
from geographic_insights.urban_population_bubble import plot_urban_population_bubble
from geographic_insights.category_country_sunburst import plot_category_country_sunburst

from growth_trends.youtubers_over_years import plot_youtubers_over_years
from growth_trends.uploads_vs_views import plot_uploads_vs_views
from growth_trends.animated_subscriber_views import plot_animated_subscriber_views
from growth_trends.country_subscribers_race import plot_country_subscribers_race
from growth_trends.animated_choropleth import plot_animated_choropleth
from growth_trends.animated_growth_scatter import plot_animated_growth_scatter
from growth_trends.top_youtubers_growth import plot_top_youtubers_growth

# Page configuration
st.set_page_config(
    page_title="YouTube Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF0000, #FF4444);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .section-header {
        background: linear-gradient(90deg, #4CAF50, #45a049);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 1rem 0;
        text-align: center;
    }
    
    .plot-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        border-radius: 10px 10px 0px 0px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF0000, #FF4444) !important;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load your dataset
@st.cache_data
def load_data():
    # Replace this with your actual data loading
    df = pd.read_csv('Cleaned_Youtube_Stats.csv')  # Update with your file path
    return df

# Load data
df = load_data()

# Header
st.markdown("""
<div class="main-header">
    <h1>🎬 YouTube Analytics Dashboard</h1>
    <p>Comprehensive insights into global YouTube statistics and trends</p>
</div>
""", unsafe_allow_html=True)

# Key metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{len(df):,}</h3>
        <p>Total YouTubers</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    total_subscribers = df['subscribers'].sum() if 'subscribers' in df.columns else 0
    st.markdown(f"""
    <div class="metric-card">
        <h3>{total_subscribers/1e9:.1f}B</h3>
        <p>Total Subscribers</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_views = df['video_views'].sum() if 'video_views' in df.columns else 0
    st.markdown(f"""
    <div class="metric-card">
        <h3>{total_views/1e12:.1f}T</h3>
        <p>Total Views</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if 'lowest_yearly_earnings' in df.columns and 'highest_yearly_earnings' in df.columns:
        df['estimated_yearly_earnings'] = (df['lowest_yearly_earnings'] + df['highest_yearly_earnings']) / 2
        total_revenue = df['estimated_yearly_earnings'].sum()
    else:
        total_revenue = 0

    st.markdown(f"""
    <div class="metric-card">
        <h3>${total_revenue/1e9:.1f}B</h3>
        <p>Total Revenue</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "📈 Subscriber Insights", "💰 Revenue Analytics", "🌍 Geographic Insights", "📽️ Growth & Trends"])

with tab1:
    st.markdown('<div class="section-header"><h2>📊 Overview</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig1 = plot_top_10_youtubers(df)
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig3 = plot_top_categories(df)
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig2 = plot_subscribers_vs_views(df)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-header"><h2>📈 Subscriber Insights</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig4 = plot_subscriber_distribution(df)
            st.plotly_chart(fig4, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig5 = plot_outlier_detection(df)
            st.plotly_chart(fig5, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig6 = plot_channel_type_revenue(df)
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-header"><h2>💰 Revenue Analytics</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig7 = plot_monthly_earnings_bubble(df)
            st.plotly_chart(fig7, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig8 = plot_revenue_distribution(df)
            st.plotly_chart(fig8, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig9 = plot_yearly_earnings_treemap(df)
        st.plotly_chart(fig9, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-header"><h2>🌍 Geographic Insights</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig10 = plot_top_countries(df)
            st.plotly_chart(fig10, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig12 = plot_urban_population_bubble(df)
            st.plotly_chart(fig12, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig11 = plot_country_choropleth(df)
        st.plotly_chart(fig11, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig13 = plot_category_country_sunburst(df)
        st.plotly_chart(fig13, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="section-header"><h2>📽️ Growth & Temporal Trends</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig14 = plot_youtubers_over_years(df)
            st.plotly_chart(fig14, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            fig15 = plot_uploads_vs_views(df)
            st.plotly_chart(fig15, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("🎬 Animated Visualizations")
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig16 = plot_animated_subscriber_views(df)
        st.plotly_chart(fig16, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig17 = plot_country_subscribers_race(df)
        st.plotly_chart(fig17, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig18 = plot_animated_choropleth(df)
        st.plotly_chart(fig18, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig19 = plot_animated_growth_scatter(df)
        st.plotly_chart(fig19, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        fig20 = plot_top_youtubers_growth(df)
        st.plotly_chart(fig20, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(90deg, #667eea, #764ba2); color: white; border-radius: 10px;'>
    <h4>🎬 YouTube Analytics Dashboard</h4>
    <p>Built with Streamlit & Plotly | Data insights for content creators worldwide</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 16px; padding-top: 1rem; color: gray;'>
    Created with ❤️ by <strong>Subham</strong>
</div>
""", unsafe_allow_html=True)
