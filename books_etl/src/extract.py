import requests
from config import GOOGLE_BOOKS_URL

def get_books(query="python", max_results=10):
    """Fetch book data from Google Books API"""
    params = {"q": query, "maxResults": max_results}
    response = requests.get(GOOGLE_BOOKS_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("items", [])
