import sqlite3
import pandas as pd
import os
from config import DB_PATH, SCHEMA_PATH

def ensure_db():
    """Ensure DB exists and schema is applied"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.close()

def truncate_books():
    """Delete all existing records before reloading"""
    ensure_db()  # ✅ ensures table exists before deleting
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("DELETE FROM books;")
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"⚠️ Skipping truncate (table not found): {e}")
    conn.close()

def load_books(book_rows):
    """Insert cleaned book data into DB"""
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame(book_rows)
    df.to_sql("books", conn, if_exists="append", index=False)
    conn.close()

def check_duplicates():
    """Remove duplicate titles (if any)"""
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        DELETE FROM books
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM books
            GROUP BY title
        );
    """)
    conn.commit()
    conn.close()
