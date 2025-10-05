import streamlit as st
import pandas as pd
import sqlite3
from config import DB_PATH


def load_data():
    conn = sqlite3.connect(DB_PATH)
    orders = pd.read_sql("SELECT * FROM orders", conn)
    conn.close()
    return orders


st.set_page_config(page_title="E-commerce Dashboard", layout="wide")
st.title("📊 E-commerce Dashboard")

df=load_data()

st.header("🧾 Recent Orders")
st.dataframe(df)

st.header("💰 Order Value Distribution")
st.bar_chart(df["order_value"])

st.header("🌍 Orders by Country")
st.bar_chart(df.groupby("customer_id")["order_value"].sum())