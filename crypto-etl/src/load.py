from sqlalchemy import create_engine
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config import DB_PATH

def load_to_sqlite(df):
    engine = create_engine(f"sqlite:///{DB_PATH}")
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
