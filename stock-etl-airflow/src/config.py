import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "stocks.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")

TICKERS=["AAPL","MSFT","GOOGL"]

YF_INTERVAL = "1d"   # daily; or "1h", "1m" for intraday (note rate limits)
YF_PERIOD = "30d"    # fetch last 30 days
