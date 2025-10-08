import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="WAF Log Dashboard", layout="wide")
st.title("🛡️ Web App Firewall Log Visualization")

engine = create_engine("sqlite:///logs.db")
df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC", engine)

st.markdown("## 🔎 Recent Requests")
st.dataframe(df, use_container_width=True)

attack_counts = df["result"].value_counts()
st.markdown("## 📊 Attack Type Distribution")
st.bar_chart(attack_counts)