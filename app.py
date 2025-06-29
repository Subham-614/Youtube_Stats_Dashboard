import streamlit as st
import pandas as pd

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
    page_title="YouTube Analytics Studio",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# YouTube-themed CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Roboto', sans-serif;
    }
    
    .main {
        background-color: #0f0f0f;
        color: #ffffff;
    }
    
    .youtube-header {
        background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%);
        padding: 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(255, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .youtube-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.1; }
    }
    
    .youtube-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        z-index: 1;
        position: relative;
    }
    
    .youtube-header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        z-index: 1;
        position: relative;
    }
    
    .play-button {
        display: inline-block;
        font-size: 2rem;
        margin-right: 1rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border: 2px solid #FF0000;
        padding: 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,0,0,0.2), transparent);
        transition: left 0.5s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 0, 0, 0.4);
        border-color: #ffffff;
    }
    
    .metric-card h3 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        color: #FF0000;
        text-shadow: 0 0 10px rgba(255, 0, 0, 0.5);
    }
    
    .metric-card p {
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.8;
        font-weight: 500;
    }
    
    .section-header {
        background: linear-gradient(135deg, #282828 0%, #3f3f3f 100%);
        border-left: 5px solid #FF0000;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        margin: 2rem 0 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .section-header h2 {
        margin: 0;
        font-weight: 500;
        font-size: 1.8rem;
    }
    
    .plot-container {
        background: linear-gradient(135deg, #181818 0%, #252525 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        margin: 1rem 0;
        border: 1px solid #404040;
        transition: all 0.3s ease;
    }
    
    .plot-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.6);
        border-color: #FF0000;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #0f0f0f;
        padding: 8px;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 24px;
        border-radius: 8px;
        background: linear-gradient(135deg, #282828 0%, #3f3f3f 100%);
        color: #ffffff;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        font-weight: 500;
        font-size: 1rem;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #404040 0%, #555555 100%);
        border-color: #FF0000;
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%) !important;
        color: white !important;
        border-color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
    }
    
    .youtube-footer {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        border: 2px solid #FF0000;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
        color: white;
    }
    
    .youtube-footer h4 {
        color: #FF0000;
        font-size: 1.5rem;
        margin: 0 0 0.5rem 0;
        font-weight: 700;
    }
    
    .creator-badge {
        display: inline-block;
        background: linear-gradient(45deg, #FF0000, #FF4444);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 0.5rem;
        box-shadow: 0 2px 10px rgba(255, 0, 0, 0.3);
    }
    
    .stats-highlight {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid #FF0000;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: white;
    }
    
    /* Dark mode scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0f0f0f;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FF0000;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #CC0000;
    }
    
    /* Plotly chart background fix */
    .js-plotly-plot .plotly .modebar {
        background: rgba(255, 0, 0, 0.1) !important;
    }
    
    .animated-text {
        background: linear-gradient(-45deg, #000000, #333333, #666666, #000000);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
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

# YouTube-themed Header
st.markdown("""
<div class="youtube-header">
    <h1><span class="play-button">▶️</span><span class="animated-text">YouTube Analytics Studio</span></h1>
    <p>🚀 Dive deep into the world's largest video platform • Discover trends, creators & insights</p>
    <div style="margin-top: 1rem;">
        <span class="creator-badge">📊 Creator Intelligence</span>
        <span class="creator-badge">📈 Growth Analytics</span>
        <span class="creator-badge">🌍 Global Reach</span>
    </div>
</div>
""", unsafe_allow_html=True)

# YouTube-style Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_creators = len(df) if not df.empty else 995
    st.markdown(f"""
    <div class="metric-card">
        <h3>{total_creators:,}</h3>
        <p>📺 Total Creators</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    total_subscribers = df['subscribers'].sum() if 'subscribers' in df.columns else 73500000000
    st.markdown(f"""
    <div class="metric-card">
        <h3>{total_subscribers/1e9:.1f}B</h3>
        <p>👥 Total Subscribers</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_views = df['video_views'].sum() if 'video_views' in df.columns else 4800000000000
    st.markdown(f"""
    <div class="metric-card">
        <h3>{total_views/1e12:.1f}T</h3>
        <p>👀 Total Views</p>
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
        <p>💰 Total Revenue</p>
    </div>
    """, unsafe_allow_html=True)

# YouTube-style Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Creator Overview", 
    "📈 Subscriber Analytics", 
    "💰 Revenue Intelligence", 
    "🌍 Global Insights", 
    "📊 Growth Trends"
])

with tab1:
    st.markdown('<div class="section-header"><h2>🏠 Creator Overview Dashboard</h2></div>', unsafe_allow_html=True)
    
    # Stats highlight
    st.markdown("""
    <div class="stats-highlight">
        <strong>🎯 Platform Highlights:</strong> Analyzing the top creators who shape YouTube's ecosystem with billions of views and millions of subscribers worldwide.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("🏆 Top 10 YouTube Creators")
        fig1 = plot_top_10_youtubers(df)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("🎭 Content Categories")
        fig3 = plot_top_categories(df)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("📊 Subscribers vs Views Correlation")
    fig2 = plot_subscribers_vs_views(df)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-header"><h2>📈 Subscriber Analytics Lab</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-highlight">
        <strong>🔍 Deep Dive:</strong> Understanding subscriber patterns, distributions, and identifying standout performers in the creator economy.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("📊 Subscriber Distribution")
        fig4 = plot_subscriber_distribution(df)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("🎯 Outlier Detection")
        fig5 = plot_outlier_detection(df)
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("💼 Channel Type vs Revenue Analysis")
    fig6 = plot_channel_type_revenue(df)
    st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-header"><h2>💰 Revenue Intelligence Center</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-highlight">
        <strong>💎 Monetization Insights:</strong> Exploring the financial landscape of YouTube's top earners and revenue distribution patterns.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("💸 Monthly Earnings Bubble")
        fig7 = plot_monthly_earnings_bubble(df)
        st.plotly_chart(fig7, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("📈 Revenue Distribution")
        fig8 = plot_revenue_distribution(df)
        st.plotly_chart(fig8, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🗺️ Yearly Earnings Treemap")
    fig9 = plot_yearly_earnings_treemap(df)
    st.plotly_chart(fig9, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-header"><h2>🌍 Global YouTube Insights</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-highlight">
        <strong>🌎 Worldwide Reach:</strong> Mapping YouTube's global influence across countries, cultures, and demographics.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("🏴 Top Countries by Creators")
        fig10 = plot_top_countries(df)
        st.plotly_chart(fig10, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("🏙️ Urban Population Analysis")
        fig12 = plot_urban_population_bubble(df)
        st.plotly_chart(fig12, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🗺️ Global Creator Distribution")
    fig11 = plot_country_choropleth(df)
    st.plotly_chart(fig11, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🌅 Category-Country Sunburst")
    fig13 = plot_category_country_sunburst(df)
    st.plotly_chart(fig13, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="section-header"><h2>📊 Growth & Temporal Trends</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-highlight">
        <strong>⏰ Time Machine:</strong> Journey through YouTube's evolution with animated visualizations showing platform growth over time.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("📅 YouTubers Over Years")
        fig14 = plot_youtubers_over_years(df)
        st.plotly_chart(fig14, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.subheader("📼 Uploads vs Views")
        fig15 = plot_uploads_vs_views(df)
        st.plotly_chart(fig15, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header"><h2>🎬 Dynamic Visualizations</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🎭 Animated Subscriber vs Views")
    fig16 = plot_animated_subscriber_views(df)
    st.plotly_chart(fig16, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🏁 Country Subscribers Race")
    fig17 = plot_country_subscribers_race(df)
    st.plotly_chart(fig17, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🌍 Animated World Map")
    fig18 = plot_animated_choropleth(df)
    st.plotly_chart(fig18, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("💫 Growth Scatter Animation")
    fig19 = plot_animated_growth_scatter(df)
    st.plotly_chart(fig19, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.subheader("🚀 Top YouTubers Growth")
    fig20 = plot_top_youtubers_growth(df)
    st.plotly_chart(fig20, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# YouTube-themed Footer
st.markdown("---")
st.markdown("""
<div class="youtube-footer">
    <h4>▶️ YouTube Analytics Studio</h4>
    <p>🎬 Empowering creators with data-driven insights • Built with ❤️ using Streamlit & Plotly</p>
    <p style="font-size: 0.9rem; opacity: 0.7; margin-top: 1rem;">
        📊 Real-time analytics • 🌍 Global coverage • 🚀 Creator success stories
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 16px; padding-top: 1rem; color: gray;'>
    Created with ❤️ by <strong>Subham</strong>
</div>
""", unsafe_allow_html=True)