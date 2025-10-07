import sqlite3
import os 
from config import DB_PATH,SCHEMA_PATH
import pandas as pd

def ensure_db():
    os.makedirs(os.path.dirname(DB_PATH),exist_ok=True)
    conn=sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH,"r") as f:
        conn.executescript(f.read())
    conn.close()


def upsert_stock_prices(df):
    """
    df: DataFrame matching columns in db/schema.sql
    Performs upsert (INSERT OR REPLACE) using pandas + SQL
    """
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    # Use transaction for speed
    cur = conn.cursor()
    # prepare upsert SQL
    insert_sql = """
    INSERT OR REPLACE INTO stock_prices
    (id, ticker, dt, open, high, low, close, adj_close, volume, sma_5, sma_20, daily_return)
    VALUES
    (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    rows=df.to_records(index=False)
    params=[]

    for r in rows:
         params.append((
            r.ticker, r.dt, r.open, r.high, r.low, r.close, r.adj_close, int(r.volume) if not pd.isna(r.volume) else None,
            float(r.sma_5) if not pd.isna(r.sma_5) else None,
            float(r.sma_20) if not pd.isna(r.sma_20) else None,
            float(r.daily_return) if not pd.isna(r.daily_return) else None
        ))
    cur.executemany("""
    INSERT INTO stock_prices (ticker, dt, open, high, low, close, adj_close, volume, sma_5, sma_20, daily_return)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, params)
    conn.commit()
    conn.close()