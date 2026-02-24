import streamlit as st

def apply_custom_theme():
    st.markdown("""
        <style>
        /* Main background and text colors */
        .stApp {
            background-color: #F8FAFC;
            color: #1E293B;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #0F172A;
        }
        [data-testid="stSidebar"] * {
            color: #FFFFFF;
        }
        
        /* Card-like containers for charts */
        div[data-testid="stVerticalBlock"] > div:has(div.stPlotlyChart) {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            margin-bottom: 20px;
        }

        /* Titles and headers */
        h1, h2, h3 {
            color: #334155;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

# professional color palette for Plotly charts
COLOR_PALETTE = ["#3B82F6", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6"]