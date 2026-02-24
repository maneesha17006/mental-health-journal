import streamlit as st
from theme import apply_custom_theme  # 1. Import the function
import plotly.express as px
from database import get_data

st.set_page_config(layout="wide")
st.title("Weekly Progress Analysis")
st.markdown("---")

# 3. Call the theme IMMEDIATELY after
apply_custom_theme()

df = get_data()

if df.empty or len(df) < 7:
    st.info("Weekly analysis requires at least 7 days of consecutive data to generate meaningful averages.")
else:
    # Prepare Weekly Data
    df['week'] = df['date'].dt.isocalendar().week
    weekly_df = df.groupby('week').agg({
        'mood': 'mean',
        'stress': 'mean',
        'sleep': 'mean',
        'energy': 'mean'
    }).reset_index()

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Current Weekly Mood", f"{round(weekly_df['mood'].iloc[-1], 1)}")
    m2.metric("Stress Variation", f"{round(weekly_df['stress'].diff().iloc[-1], 1)}")
    m3.metric("Avg Sleep Cycle", f"{round(weekly_df['sleep'].mean(), 1)}h")
    m4.metric("Stability Score", f"{round(10 - weekly_df['mood'].std(), 1)}")

    st.markdown("---")
    
    # 4 Graphs
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Weekly Mood Averages")
        st.plotly_chart(px.bar(weekly_df, x='week', y='mood', color='mood', template="plotly_white"), use_container_width=True)
        
        st.subheader("Sleep Consistency")
        st.plotly_chart(px.line(weekly_df, x='week', y='sleep', markers=True, template="plotly_white"), use_container_width=True)

    with c2:
        st.subheader("Stress Trend by Week")
        st.plotly_chart(px.line(weekly_df, x='week', y='stress', color_discrete_sequence=['#E63946'], template="plotly_white"), use_container_width=True)
        
        st.subheader("Energy Recovery Rate")
        st.plotly_chart(px.scatter(weekly_df, x='energy', y='mood', size='sleep', template="plotly_white"), use_container_width=True)