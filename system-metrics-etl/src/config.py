import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR=os.path.join(BASE_DIR,"db")
DB_PATH=os.path.join(DB_DIR,"metrics.db")
SCHEMA_PATH=os.path.join(DB_DIR,"schema.sql")

POLL_INTERVAL=5