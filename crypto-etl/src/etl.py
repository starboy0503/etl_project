import sys, os
sys.path.append(os.path.dirname(__file__))

from extract import fetch_prices
from transform import transform_prices
from load import load_to_sqlite

def run_etl():
    raw = fetch_prices()
    df = transform_prices(raw)
    load_to_sqlite(df)
    print("Inserted crypto prices:\n", df)

if __name__ == "__main__":
    run_etl()
