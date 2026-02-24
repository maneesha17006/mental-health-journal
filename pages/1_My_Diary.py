import streamlit as st
from theme import apply_custom_theme  # 1. Import the function
from datetime import date
from database import add_entry, get_data

st.set_page_config(page_title="Daily Journal", layout="centered")
# 3. Call the theme IMMEDIATELY after
apply_custom_theme()


# Header Section
st.title("✍️ Daily Reflection")
st.markdown("---")
st.write("Take a moment to check in with yourself. How are you feeling today?")

# Layout with Columns for a clean UI
col1, col2 = st.columns(2)

with col1:
    entry_date = st.date_input("Date", date.today())
    mood = st.select_slider(
        "Rate your Mood (1 = Low, 10 = Great)",
        options=range(1, 11), value=5
    )
    stress = st.select_slider(
        "Stress Level (1 = Calm, 10 = High)",
        options=range(1, 11), value=3
    )

with col2:
    sleep = st.number_input("Sleep (Hours)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    energy = st.select_slider(
        "Energy Level (1 = Exhausted, 10 = Vibrant)",
        options=range(1, 11), value=6
    )

# Note Section
note = st.text_area("What's on your mind? (Optional)", placeholder="Write a few sentences about your day...")

# Center the button using a container
st.markdown("---")
# inside pages/1_My_Diary.py

if st.button("Save Daily Entry", use_container_width=True):
    try:
        # We convert the date to a string so SQLite stores it reliably
        date_str = entry_date.strftime("%Y-%m-%d")
        add_entry(date_str, mood, stress, sleep, energy, note)
        
        st.success("Entry recorded in the system archive.")
        # This line forces the app to notice the new data
        st.cache_data.clear() 
    except Exception as e:
        st.error(f"System Error: {e}")

# Quick view of today's status
st.sidebar.info("Tip: Try to be as honest as possible. This data is for your eyes only.")