import streamlit as st
import sqlite3
import pandas as pd
from config import DB_PATH

@st.cache_data
def load_data():
    conn=sqlite3.connect(DB_PATH)
    df=pd.read_sql("SELECT * FROM articles ORDER by date DESC",conn)
    conn.close()
    return df


st.set_page_config(page_title="📰 Web Scraping ETL Dashboard",layout="wide")
st.title("🕷️ Web Scraping ETL Dashboard")
st.caption("Built with Python • BeautifulSoup • SQLite • Streamlit")


try:
    df=load_data()
    if df.empty:
        st.warning("⚠️ No articles found. Please run the ETL script first.")
    else:
        total_articles=len(df)
        unique_authors = df["author"].nunique()
        latest_date = df["date"].max()

        col1,col2,col3=st.columns(3)
        col1.metric("📰 Total Articles", total_articles)
        col2.metric("✍️ Unique Authors", unique_authors)
        col3.metric("🕒 Latest Update", latest_date)

        st.subheader("🧾 Latest Articles")
        st.dataframe(df[["title", "author", "date", "link"]].head(10), use_container_width=True)

        st.subheader("🏆 Top Authors by Article Count")
        top_authors=df["authors"].value_counts().head(5).reset_index()
        top_authors.columns=["Author", "Article Count"]
        st.bar_chart(top_authors.set_index("Author"))


        st.subheader("📈 Articles Published Over Time")
        df["date"]=pd.to_datetime(df["date"],errors="coerce")
        timeline=df.groupby(df["date"].dt.date).size().reset_index(name="Articles")
        st.line_chart(timeline.set_index("date"))


        st.subheader("🔗 Read the Articles")

        for _,row in df.head(5).iterrows:
            st.markdown(f"- [{row['title']}] ({row['link']}) - * {row["author"]} * ({row['date']})")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")

st.caption("Built with ❤️ by Aditya — Web Scraping ETL Project")

