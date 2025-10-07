import sqlite3
import os
from config import DB_PATH,SCHEMA_PATH

def ensure_db():
    """Ensure DB and schema exist"""
    os.makedirs(os.path.dirname(DB_PATH),exist_ok=True)
    conn=sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH,"r") as f:
        conn.executescript(f.read())
    conn.close()


def load_to_db(df):
    """Load transformed articles into SQLite DB"""
    ensure_db()
    conn=sqlite3.connect(DB_PATH)
    df.to_sql("articles", conn, if_exists="append", index=False)
    conn.close()
