import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = "/Users/adityadhanrajsingh/Desktop/etl_projects/csv-sales-etl/db/sales.db"

def load_data_from_db(db_path=DB_PATH):
    conn=sqlite3.connect(db_path)
    df=pd.read_sql("SELECT * FROM sales",conn)
    conn.close()
    return df

st.title("📊 Sales Dashboard (CSV ETL Project)")
df=load_data_from_db()
st.write("Raw Data from SQLite Database:")

#sales by product 
sales_by_product=df.groupby('product')['total'].sum().reset_index()
st.bar_chart(sales_by_product.set_index("product"))


#sales by date

sales_by_date=df.groupby('date')['total'].sum().reset_index()
st.line_chart(sales_by_date.set_index("date"))


#KPI summary 

st.write("### Key Performance Indicators (KPIs)")
st.metric("Total Sales",f"${df['total'].sum():,.2f}")
st.metric("Total Orders",len(df))
st.metric("Unique Products",df['product'].nunique())



