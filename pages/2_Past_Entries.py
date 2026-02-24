import streamlit as st
from database import get_data
from theme import apply_custom_theme

st.set_page_config(layout="wide", page_title="Data Archive")
apply_custom_theme()

st.title("Data Archive")
st.markdown("---")

# 1. Fetch the data
df = get_data()

# 2. Display Status Metrics
c1, c2 = st.columns(2)
with c1:
    st.metric("Total Records Found", len(df))
with c2:
    st.write(f"Source: `/data/journal.db`")

# 3. Display the Table
if not df.empty:
    # Sort by date so the newest is on top
    df = df.sort_values(by='date', ascending=False)
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.warning("The database is currently empty. Please log an entry in the Diary.")