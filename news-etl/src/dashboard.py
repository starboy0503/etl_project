import streamlit as st
import pandas as pd
import sqlite3
from config import DB_PATH

def load_data(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df

st.set_page_config(page_title="News Dashboard", layout="wide")
st.title("📰 Live News Headlines ETL Dashboard")

# --- Latest Headlines ---
st.header("🗞 Latest Headlines")
try:
    news = load_data("""
        SELECT headline, source, published_at 
        FROM headlines 
        ORDER BY published_at DESC 
        LIMIT 20
    """)
    if news.empty:
        st.warning("⚠️ No headlines found. Run ETL first.")
    else:
        st.table(news)
except Exception as e:
    st.error(f"❌ Error loading headlines: {e}")

# --- Sentiment Trend ---
st.header("📊 Sentiment Analysis")
try:
    sentiment = load_data("""
        SELECT published_at, sentiment 
        FROM headlines 
        ORDER BY published_at DESC 
        LIMIT 100
    """)
    if sentiment.empty:
        st.warning("⚠️ No sentiment data found. Run ETL first.")
    else:
        sentiment["published_at"] = pd.to_datetime(sentiment["published_at"])
        st.line_chart(sentiment.set_index("published_at")["sentiment"])
except Exception as e:
    st.error(f"❌ Error loading sentiment data: {e}")
