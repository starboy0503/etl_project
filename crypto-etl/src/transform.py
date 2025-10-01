import pandas as pd
from datetime import datetime

def transform_prices(raw_data):
    rows = []
    for entry in raw_data:
        rows.append({
            "coin": entry["symbol"],        # e.g., BTCUSDT
            "price": float(entry["price"]), # convert string to float
            "timestamp": datetime.now()
        })
    return pd.DataFrame(rows)
