import os 
import sqlite3
import pandas as pd
import streamlit as st
from config import DB_PATH

st.set_page_config(page_title="💻 System Metrics Dashboard",layout="wide")
st.title("💻 System Metrics Monitor")

@st.cache_data(ttl=5)

def load_data():
    if not os.path.exists(DB_PATH):
        st.error("No metrics database found. Run the ETL script first.")
        return pd.DataFrame()
    conn=sqlite3.connect(DB_PATH)
    df=pd.read_sql_query(" SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 100",conn)
    conn.close()
    df["timestamp"]=pd.to_datetime(df["timestamp"])
    return df.sort_values("timestamp")

df=load_data()
if df.empty:
    st.warning("⚠️ No metrics yet. Run the ETL script.")
    st.stop()

col1,col2,col3=st.columns(3)
col1.metric("🧠 CPU Usage (%)",f"{df['cpu_usage'].iloc[-1]:.2f}")
col2.metric("💾 Disk Usage (%)", f"{df['disk_usage'].iloc[-1]:.2f}")
col3.metric("🔋 Memory Usage (%)", f"{df['memory_usage'].iloc[-1]:.2f}")

st.subheader("📈 CPU & Memory Trend")
st.line_chart(df.set_index("timestamp")[["cpu_usage", "memory_usage"]])

st.subheader("📡 Network Usage (MB)")
st.area_chart(df.set_index("timestamp")[["net_sent", "net_recv"]])