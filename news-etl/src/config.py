import os 
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH=os.path.join(BASE_DIR,"db","news.db")
SCHEMA_PATH=os.path.join(BASE_DIR,"db","schema.sql")


NEWS_API_KEY="c55da2d3ac74475095811dc9071799f4"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
