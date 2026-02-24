import streamlit as st
from theme import apply_custom_theme  # 1. Import the function

st.set_page_config(layout="centered")
st.title("Clinical Support & Resources")
st.markdown("---")
# 3. Call the theme IMMEDIATELY after
apply_custom_theme()


st.subheader("Grounding Exercise: Sensory Awareness")
st.write("Use this structured method to reduce acute stress levels:")

# Using columns to create a clean list
s1, s2 = st.columns([1, 4])
s1.write("**5 - Visual**")
s2.write("Identify five distinct objects in your immediate environment.")
s1.write("**4 - Tactile**")
s2.write("Focus on four different textures you can touch right now.")
s1.write("**3 - Auditory**")
s2.write("Listen for three separate sounds in the distance.")
s1.write("**2 - Olfactory**")
s2.write("Identify two distinct scents in the air.")
s1.write("**1 - Gustatory**")
s2.write("Focus on one specific taste.")

st.markdown("---")

st.subheader("Recommended Reading")
st.info("""
**Emotional Resilience**
Focus on what you can control. Data tracking is the first step in identifying 
variables that you have the power to change, such as sleep hygiene and stress management.
""")

st.subheader("Immediate Assistance")
st.write("If you are experiencing a crisis, please contact professional services.")
st.write("- **Crisis Text Line:** Text HOME to 741741")
st.write("- **International Helplines:** [https://www.befrienders.org/](https://www.befrienders.org/)")