import streamlit as st
from theme import apply_custom_theme  # 1. Import the function

# 2. Set the config FIRST
st.set_page_config(layout="wide")
st.title("Pattern Intelligence")
st.markdown("---")

# 3. Call the theme IMMEDIATELY after
apply_custom_theme()

import plotly.express as px
import plotly.graph_objects as go
from database import get_data



df = get_data()

if df.empty or len(df) < 2:
    st.info("Insufficient data. Please log at least two entries in the Diary to unlock pattern analysis.")
else:
    # 1. TOP ROW: PRIMARY ANALYTICS
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Mood and Sleep Correlation")
        fig1 = px.scatter(df, x="sleep", y="mood", size="energy", color="stress",
                         labels={"sleep": "Sleep Hours", "mood": "Mood Score"},
                         template="plotly_white",
                         color_continuous_scale="RdBu_r")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Stress and Energy Heatmap")
        try:
            z_data = df.pivot_table(index='stress', columns='energy', values='mood', aggfunc='mean')
            fig2 = px.imshow(z_data, 
                            labels=dict(x="Energy Level", y="Stress Level", color="Avg Mood"),
                            color_continuous_scale='Tealrose',
                            template="plotly_white")
            st.plotly_chart(fig2, use_container_width=True)
        except:
            st.write("Heatmap will populate as your data variety increases.")

    # 2. MIDDLE ROW: STABILITY & DISTRIBUTION
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Energy Stability Index")
        fig3 = px.area(df, x="date", y="energy", 
                      line_shape="spline", 
                      color_discrete_sequence=['#2E86C1'],
                      template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("Stress Level Frequency")
        fig4 = px.pie(df, names='stress', hole=0.5,
                     color_discrete_sequence=px.colors.sequential.Greens_r,
                     template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

    # 3. BOTTOM SECTION: AUTO-GENERATED REFLECTION INSIGHTS
    st.markdown("---")
    st.subheader("Automated Behavioral Insights")
    
    # Logic to fill empty space with smart text
    insight_col1, insight_col2 = st.columns(2)
    
    # Calculate Correlation Insight
    correlation = df['sleep'].corr(df['mood'])
    avg_mood_high_sleep = df[df['sleep'] > 7]['mood'].mean()
    avg_mood_low_sleep = df[df['sleep'] <= 7]['mood'].mean()

    with insight_col1:
        st.write("**Sleep Impact Analysis**")
        if avg_mood_high_sleep > avg_mood_low_sleep:
            diff = round(avg_mood_high_sleep - avg_mood_low_sleep, 1)
            st.write(f"Data suggests your mood improves by {diff} points on days you sleep more than 7 hours.")
        else:
            st.write("Current data shows your mood is consistent regardless of sleep duration.")

    with insight_col2:
        st.write("**Stress Factor Analysis**")
        high_stress_days = len(df[df['stress'] > 7])
        if high_stress_days > 0:
            st.write(f"You have recorded high stress levels on {high_stress_days} occasions. Cross-referencing shows these days often align with lower energy scores.")
        else:
            st.write("Stress levels have remained within a manageable range for this tracking period.")