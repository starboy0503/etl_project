import os
import sqlite3
import pandas as pd
import streamlit as st
from src.config import DB_PATH

# -------------------------------
# Utility: Load Data from SQLite
# -------------------------------
@st.cache_data
def load_data():
    """Load unique articles from SQLite database"""
    if not os.path.exists(DB_PATH):
        st.error("❌ Database not found. Run the ETL script first!")
        return pd.DataFrame()

    try:
        with sqlite3.connect(DB_PATH) as conn:
            query = """
                SELECT DISTINCT title, author, date, link
                FROM articles
                ORDER BY date DESC
            """
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

# -------------------------------
# Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="📰 Web Scraping ETL Dashboard", layout="wide")
st.title("🕷️ Web Scraping ETL Dashboard")
st.caption("Built with Python • BeautifulSoup • SQLite • Streamlit")

# -------------------------------
# Load Data
# -------------------------------
df = load_data()

if df.empty:
    st.warning("⚠️ No articles found. Please run `python -m src.etl` first.")
    st.stop()

# Ensure expected columns exist
expected_cols = {"title", "author", "date", "link"}
missing = expected_cols - set(df.columns)
if missing:
    st.error(f"❌ Missing columns in DB: {missing}")
    st.stop()

# Clean up DataFrame just in case
df = df.drop_duplicates(subset=["link"])
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["date"].fillna(pd.Timestamp.now(), inplace=True)

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("⚙️ Filters")

authors = ["All"] + sorted(df["author"].dropna().unique().tolist())
selected_author = st.sidebar.selectbox("Filter by Author", authors)

if selected_author != "All":
    df = df[df["author"] == selected_author]

# -------------------------------
# Key Metrics
# -------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("📰 Total Articles", len(df))
col2.metric("✍️ Unique Authors", df["author"].nunique())
col3.metric("📅 Latest Date", df["date"].max().strftime("%Y-%m-%d"))

# -------------------------------
# Charts
# -------------------------------
st.subheader("📈 Articles Published Over Time")
timeline = df.groupby(df["date"].dt.date).size().reset_index(name="Articles")
st.line_chart(timeline.set_index("date"))

st.subheader("🏆 Top Authors")
top_authors = df["author"].value_counts().head(10).reset_index()
top_authors.columns = ["Author", "Articles"]
st.bar_chart(top_authors.set_index("Author"))

# -------------------------------
# Latest Articles Table
# -------------------------------
st.subheader("🗞️ Latest Articles")
st.dataframe(df[["title", "author", "date", "link"]].head(20), use_container_width=True)

# -------------------------------
# External Links
# -------------------------------
st.subheader("🔗 Open Articles")
for _, row in df.head(10).iterrows():
    st.markdown(f"- [{row['title']}]({row['link']}) — *{row['author']}* ({row['date'].strftime('%Y-%m-%d')})")

st.caption("Built with ❤️ by Aditya — Web Scraping ETL Project")
