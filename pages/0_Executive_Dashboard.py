import streamlit as st
import plotly.express as px
from database import get_data
from theme import apply_custom_theme, COLOR_PALETTE

st.set_page_config(layout="wide", page_title="Executive Dashboard")
apply_custom_theme()

st.title("Executive Health Dashboard")
st.markdown("Global system overview and key performance indicators.")
st.markdown("---")

df = get_data()

if df.empty:
    st.info("No system data available. Please initialize logs in the Diary section.")
else:
    # Top Row: High-Density Metrics
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    with col_m1:
        st.metric("Mean Mood Score", f"{round(df['mood'].mean(), 1)}", delta_color="normal")
    with col_m2:
        st.metric("Average Sleep Duration", f"{round(df['sleep'].mean(), 1)}h")
    with col_m3:
        st.metric("Stress Index", f"{round(df['stress'].mean(), 1)}", delta="-0.5", delta_color="inverse")
    with col_m4:
        st.metric("Data Points Collected", len(df))

    st.markdown("---")

    # Middle Row: Main Trends
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Mood Stability Trend")
        fig1 = px.line(df, x='date', y='mood', 
                      template="plotly_white",
                      color_discrete_sequence=[COLOR_PALETTE[0]])
        fig1.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.subheader("Sleep vs. Energy Analysis")
        fig2 = px.scatter(df, x='sleep', y='energy', 
                         trendline="ols",
                         template="plotly_white",
                         color_discrete_sequence=[COLOR_PALETTE[1]])
        st.plotly_chart(fig2, use_container_width=True)

    # Bottom Row: Distribution and Comparisons
    c3, c4 = st.columns(2)
    
    with c3:
        st.subheader("Stress Level Distribution")
        fig3 = px.bar(df, x='date', y='stress', 
                     template="plotly_white",
                     color_discrete_sequence=[COLOR_PALETTE[3]])
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        st.subheader("Metric Correlation Heatmap")
        corr = df[['mood', 'sleep', 'stress', 'energy']].corr()
        fig4 = px.imshow(corr, text_auto=True, 
                        color_continuous_scale='Blues',
                        template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)