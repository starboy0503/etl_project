import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to SQLite database
DB_PATH = os.path.join(BASE_DIR, "../db/eth.db")

# Path to schema.sql
SCHEMA_PATH = os.path.join(BASE_DIR, "../db/schema.sql")

# Ethereum RPC provider (Alchemy/Infura etc.)
WEB3_PROVIDER = "https://eth-mainnet.g.alchemy.com/v2/tRWKKK9behI7oi8RFy3qj"

# Polling interval for realtime ETL
POLL_INTERVAL_SECONDS = 6
