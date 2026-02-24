import streamlit as st

st.set_page_config(page_title="MindFlow Digital Systems", layout="wide")

def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1499209974431-9dac3adaf471?q=80&w=2070");
            background-size: cover;
        }}
        .reportview-container {{
            background: rgba(255, 255, 255, 0.9);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

st.title("MindFlow: Emotional Pattern Analysis")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("System Purpose")
    st.write("""
    This platform is a professional-grade emotional self-tracking system. 
    By documenting daily metrics including sleep, stress, and mood, the system 
    identifies physiological and psychological correlations to help improve 
    long-term well-being.
    """)
    
    st.subheader("Instructions")
    st.write("1. Access the 'Diary' page to log your daily data.")
    st.write("2. Review 'Executive Dashboard' for high-level summaries.")
    st.write("3. Visit 'Pattern Intelligence' for deep-dive correlation analysis.")

with col2:
    st.info("**Data Privacy Notice**\n\nAll data is stored locally in your system's database. No external servers are used for data processing.")