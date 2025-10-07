import streamlit as st
import pandas as pd
import sqlite3
from config import DB_PATH

# ------------------ Utility ------------------
def load_data(query):
    """Helper to run SQL queries and return DataFrame"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ------------------ Page Setup ------------------
st.set_page_config(page_title="E-commerce Dashboard", layout="wide")
st.title("🛍 E-Commerce Sales Dashboard")

# ------------------ Data Loading ------------------
try:
    orders = load_data("SELECT * FROM orders")
    customers = load_data("SELECT * FROM customers")
    products = load_data("SELECT * FROM products")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ------------------ KPIs ------------------
total_orders = len(orders)
total_revenue = orders["order_value"].sum()
unique_customers = orders["customer_id"].nunique()
top_country = (
    customers["country"].mode()[0] if not customers.empty else "N/A"
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Orders", f"{total_orders}")
col2.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
col3.metric("👥 Unique Customers", f"{unique_customers}")
col4.metric("🌍 Top Country", top_country)

st.divider()

# ------------------ Recent Orders ------------------
st.header("🧾 Recent Orders")
st.dataframe(
    orders.sort_values("order_date", ascending=False)
           .head(10)
           .loc[:, ["order_id", "order_date", "customer_id", "product_id", "order_value"]],
    use_container_width=True
)

st.divider()

# ------------------ Revenue Trends ------------------
st.header("📈 Revenue Trend Over Time")
orders_by_date = (
    orders.groupby("order_date")["order_value"].sum().reset_index()
)
st.line_chart(orders_by_date, x="order_date", y="order_value")

# ------------------ Top Products ------------------
st.header("🏆 Top Selling Products")
top_products = (
    orders.groupby("product_id")["order_value"].sum()
    .reset_index()
    .sort_values(by="order_value", ascending=False)
    .head(5)
)
top_products = top_products.merge(products, on="product_id", how="left")
st.bar_chart(top_products.set_index("name")["order_value"])

# ------------------ Orders by Country ------------------
st.header("🌍 Orders by Country")
orders_country = (
    orders.merge(customers, on="customer_id", how="left")
    .groupby("country")["order_value"]
    .sum()
    .reset_index()
)
st.bar_chart(orders_country.set_index("country")["order_value"])

st.caption("⚙️ Data source: SQLite DB (`ecommerce.db`) | Built with Streamlit")
