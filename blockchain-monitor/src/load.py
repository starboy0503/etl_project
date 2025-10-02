import sqlite3
import pandas as pd
import os
from config import DB_PATH, SCHEMA_PATH

def ensure_db():
    """Ensure DB exists and schema is applied."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
    conn.executescript(schema)
    conn.close()

def load_block(block_dict):
    """Insert block into DB"""
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame([block_dict])
    df.to_sql("blocks", conn, if_exists="append", index=False)
    conn.close()

def load_transactions(tx_rows):
    """Insert transactions into DB"""
    if not tx_rows:
        return
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame(tx_rows)
    df.to_sql("transactions", conn, if_exists="append", index=False)
    conn.close()
