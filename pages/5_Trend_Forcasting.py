import streamlit as st
import plotly.express as px
import pandas as pd
from theme import apply_custom_theme
from database import get_data

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Trend Forecasting")
apply_custom_theme()

# 2. Page Header
st.title("Behavioral Reflections & Trends")
st.markdown("Long-term pattern recognition based on historical data logs.")
st.markdown("---")

# 3. Data Retrieval
df = get_data()

# 4. Logic & Visualization
if df.empty:
    st.info("The forecasting engine requires historical data. Please record your daily metrics in the Diary.")
elif len(df) < 2:
    st.warning("Insufficient data density. Please log at least two days of data to generate trend visualizations.")
else:
    # Row 1: Distribution and History
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Mood Frequency Distribution")
        # Ensure x="mood" matches your database column name exactly
        fig_hist = px.histogram(
            df, 
            x="mood", 
            nbins=10, 
            template="plotly_white", 
            color_discrete_sequence=['#1E293B'],
            labels={'mood': 'Mood Rating', 'count': 'Frequency'}
        )
        st.plotly_chart(fig_hist, use_container_width=True)

        st.subheader("Energy Stability Over Time")
        fig_line = px.line(
            df, 
            x='date', 
            y='energy', 
            template="plotly_white",
            color_discrete_sequence=['#3B82F6'],
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        st.subheader("Emotional Baseline Analysis")
        # Shows how often you are in specific mood states
        fig_pie = px.pie(
            df, 
            names='mood', 
            hole=0.6, 
            template="plotly_white",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("Factor Correlation Matrix")
        # This calculates how much sleep/stress impacts your mood
        # We only select the numeric columns to avoid errors
        numeric_df = df[['mood', 'stress', 'sleep', 'energy']]
        corr = numeric_df.corr()
        
        fig_corr = px.imshow(
            corr, 
            text_auto=True, 
            aspect="auto",
            color_continuous_scale='RdBu_r', # Red for negative, Blue for positive
            template="plotly_white"
        )
        st.plotly_chart(fig_corr, use_container_width=True)

    # Row 2: Analytical Insight Block
    st.markdown("---")
    st.subheader("Automated Trend Observation")
    
    # Simple logic to fill the empty space with professional text
    correlation_value = df['sleep'].corr(df['mood'])
    
    inf_col1, inf_col2 = st.columns(2)
    with inf_col1:
        st.write("**Statistical Summary**")
        st.write(f"Standard Deviation of Mood: {round(df['mood'].std(), 2)}")
        st.write(f"Average Stress-to-Energy Ratio: {round(df['stress'].mean() / df['energy'].mean(), 2)}")
        
    with inf_col2:
        st.write("**Predictive Insight**")
        if correlation_value > 0.5:
            st.write("There is a strong positive correlation between your sleep duration and mood score. Prioritizing rest is likely to yield immediate emotional benefits.")
        elif correlation_value < -0.5:
            st.write("Data indicates a significant inverse relationship between these metrics. Further observation is recommended.")
        else:
            st.write("Current data suggests your mood is influenced by variables outside of the tracked sleep/stress parameters.")