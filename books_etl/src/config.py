import os

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "books.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "db", "schema.sql")

# API Config
GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"
