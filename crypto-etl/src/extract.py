import requests
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # add project root

from config import PAIRS, BINANCE_URL

def fetch_prices():
    prices = []
    for pair in PAIRS:
        resp = requests.get(BINANCE_URL, params={"symbol": pair})
        resp.raise_for_status()
        data = resp.json()   # {"symbol": "BTCUSDT", "price": "42123.45"}
        prices.append(data)
    return prices
