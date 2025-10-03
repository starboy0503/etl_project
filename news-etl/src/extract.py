import requests
from config import NEWS_URL

def fetch_news():
    response = requests.get(NEWS_URL)
    data = response.json()
    return data.get("articles", [])
