import os
import sys
import pandas as pd
from datetime import datetime, timedelta
from airflow.decorators import dag, task

# -------------------- PATH FIX --------------------
# Dynamically add project root to PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# -------------------- IMPORTS --------------------
from src.extract import extract_all
from src.transform import compute_indicators
from src.load import upsert_stock_prices

# -------------------- DAG CONFIG --------------------
default_args = {
    "owner": "aditya",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="stock_market_etl",
    description="Daily Stock Market ETL using yfinance",
    default_args=default_args,
    schedule_interval="@daily",  # every day at midnight
    start_date=datetime(2025, 10, 1),
    catchup=False,
    max_active_runs=1,
    tags=["stocks", "etl"],
)
def stock_etl():
    """Airflow DAG: Extract, Transform, Load stock market data"""

    @task()
    def extract_task():
        df = extract_all()
        if df is None or df.empty:
            return None
        return df.to_json(orient="records", date_format="iso")

    @task()
    def transform_task(df_json):
        if not df_json:
            return None
        df = pd.read_json(df_json, orient="records")
        transformed = compute_indicators(df)
        return transformed.to_json(orient="records", date_format="iso")

    @task()
    def load_task(df_json):
        if not df_json:
            return "no-data"
        df = pd.read_json(df_json, orient="records")
        upsert_stock_prices(df)
        return f"✅ Loaded {len(df)} rows."

    raw = extract_task()
    transformed = transform_task(raw)
    result = load_task(transformed)
    return result

# -------------------- DAG OBJECT --------------------
dag = stock_etl()
