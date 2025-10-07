import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH=os.path.join(BASE_DIR,"db/news.db")
SCHEMA_PATH=os.path.join(BASE_DIR,"db/schema.sql")

NEWS_URL="https://news.ycombinator.com/"

MAX_ARTICLES = 30