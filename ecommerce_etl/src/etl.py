import json
import pandas as pd
import sqlite3
import os
from config import DATA_SOURCE, DB_PATH, SCHEMA_PATH

# ------------------ EXTRACT ------------------
def extract_data():
    """Extract e-commerce data from mock JSON"""
    with open(DATA_SOURCE, 'r') as f:
        data = json.load(f)
    return data["customers"], data["products"], data["orders"]

# ------------------ TRANSFORM ------------------
def transform_data(customers, products, orders):
    """Clean and combine e-commerce data"""
    df_customers = pd.DataFrame(customers)
    df_products = pd.DataFrame(products)
    df_orders = pd.DataFrame(orders)

    # Merge customers and products into orders
    df_merged = df_orders.merge(df_customers, on="customer_id", how="left")
    df_merged = df_merged.merge(df_products, on="product_id", how="left")

    # ✅ FIX: use 'price', not 'order_value' for multiplication
    df_merged["order_value"] = df_merged["quantity"] * df_merged["price"]

    # Convert date strings to datetime objects
    df_merged["order_date"] = pd.to_datetime(df_merged["order_date"], errors="coerce")

    # Remove duplicates
    df_merged.drop_duplicates(subset=["order_id"], inplace=True)

    return df_customers, df_products, df_merged

# ------------------ LOAD ------------------
def ensure_db():
    """Ensure DB and schema exist"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.close()

def load_to_db(customers, products, orders):
    """Load cleaned data into SQLite"""
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    products.to_sql("products", conn, if_exists="replace", index=False)
    orders.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()

# ------------------ RUN ETL ------------------
def run_ecommerce_etl():
    print("🔍 Extracting data...")
    customers, products, orders = extract_data()

    print("🧹 Transforming data...")
    df_customers, df_products, df_orders = transform_data(customers, products, orders)

    print("💾 Loading data into database...")
    load_to_db(df_customers, df_products, df_orders)

    print("✅ E-commerce ETL completed successfully!")

# ------------------ MAIN ------------------
if __name__ == "__main__":
    run_ecommerce_etl()
