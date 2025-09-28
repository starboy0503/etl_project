import sqlite3
import os
from transform import transform_data

def load_to_sqlite():
    # Make sure db/ folder exists
    os.makedirs("db", exist_ok=True)

    # Connect (creates movies.db if it doesn’t exist)
    conn = sqlite3.connect("db/movies.db")

    # Get transformed data
    df = transform_data()

    # Save to SQLite
    df.to_sql("top_movies", conn, if_exists="replace", index=False)

    conn.close()
    print("✅ Data loaded to SQLite database at db/movies.db")

if __name__ == "__main__":
    load_to_sqlite()
