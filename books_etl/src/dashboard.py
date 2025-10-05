import streamlit as st
import pandas as pd
import sqlite3
from config import DB_PATH

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM books ORDER BY average_rating DESC", conn)
    conn.close()
    return df

st.set_page_config(page_title="📚 Books ETL Dashboard", layout="wide")
st.title("📘 Google Books Dashboard")

# Search
query = st.text_input("🔍 Search books by keyword:", "python")

if st.button("Fetch Books"):
    from src.etl import run_books_etl
    run_books_etl(query=query, max_results=10, refresh=True)
    st.success(f"✅ Books for '{query}' loaded successfully! Please refresh.")

# Show Data
df = load_data()

st.header("Top Rated Books")
st.dataframe(df[["title", "authors", "average_rating", "ratings_count", "categories"]])

st.header("📊 Ratings Distribution")
st.bar_chart(df["average_rating"].value_counts().sort_index())
