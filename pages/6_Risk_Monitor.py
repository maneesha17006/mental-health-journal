import streamlit as st
from theme import apply_custom_theme  # 1. Import the function

# 2. Set the config FIRST
st.set_page_config(layout="wide", page_title="System Risk Monitor")

# 3. Call the theme IMMEDIATELY after
apply_custom_theme()

import plotly.express as px
from database import get_data


st.title("System Risk Monitor")
st.markdown("Automated detection of physiological and emotional anomalies.")
st.markdown("---")

df = get_data()

if len(df) < 3:
    st.info("Risk monitoring requires a minimum of 3 consecutive data entries.")
else:
    # Logic for detection
    avg_mood = df['mood'].tail(3).mean()
    high_stress_count = len(df[df['stress'] > 7].tail(5))

    col_a, col_b = st.columns([1, 2])

    with col_a:
        st.subheader("Status Report")
        if avg_mood < 4:
            st.error("Status: Low Mood Trend Detected")
            st.write("Observation: The 3-day mood average has fallen below the safety threshold.")
        elif high_stress_count >= 2:
            st.warning("Status: Elevated Stress Pattern")
            st.write("Observation: Multiple high-stress entries detected within the last 5 logs.")
        else:
            st.success("Status: Nominal")
            st.write("Observation: No critical patterns or threshold breaches detected.")

    with col_b:
        st.subheader("Threshold Visualization")
        # Visualizing the 4 graphs as small small multiples
        sub1, sub2 = st.columns(2)
        
        fig_m = px.line(df, x='date', y='mood', title="Mood Threshold")
        fig_m.add_hline(y=3, line_dash="dot", line_color="red")
        sub1.plotly_chart(fig_m, use_container_width=True)
        
        fig_s = px.line(df, x='date', y='stress', title="Stress Threshold")
        fig_s.add_hline(y=8, line_dash="dot", line_color="orange")
        sub2.plotly_chart(fig_s, use_container_width=True)