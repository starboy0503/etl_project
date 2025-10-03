import sqlite3, os
import pandas as pd
from config import DB_PATH, SCHEMA_PATH

def ensure_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.close()

def load_articles(articles):
    if not articles: return
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    pd.DataFrame(articles).to_sql("headlines", conn, if_exists="append", index=False)
    conn.close()
