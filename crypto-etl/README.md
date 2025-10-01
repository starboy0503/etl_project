README Notes – Crypto Price ETL
🚀 Project Overview

Crypto Price ETL pipeline that:

Extracts live crypto prices from the Binance API (no API key needed).

Transforms data with Pandas into a structured format.

Loads into a SQLite database for persistence.

Visualizes price trends using Plotly.

This project demonstrates ETL, API integration, database handling, and data visualization — core skills in Data Engineering & ML workflows.

🛠️ Tech Stack

Python 3.10+

Pandas – Data transformation

Requests – API calls

SQLite – Local database

SQLAlchemy – DB interface

Plotly – Interactive visualization

📂 Project Structure
crypto-etl/
│── config.py              # Config (coins, DB path, API endpoint)
│── requirements.txt
│── README.md
│
├── db/
│   └── schema.sql         # SQLite schema
│
├── src/
│   ├── extract.py         # Fetch data from Binance API
│   ├── transform.py       # Clean/format data
│   ├── load.py            # Load data into SQLite
│   ├── etl.py             # Orchestrator (runs ETL)
│   └── dashboard.py       # Visualization with Plotly

⚙️ Setup

Clone repo:

git clone https://github.com/<your-username>/crypto-etl.git
cd crypto-etl


Create virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Initialize database:

sqlite3 db/crypto.db < db/schema.sql

▶️ Run ETL

Fetch latest prices and store in SQLite:

python src/etl.py

📊 Run Dashboard

Visualize stored prices:

python src/dashboard.py


Interactive line chart opens in browser.

🔄 Automate with Cron

Run ETL every 5 minutes:

*/5 * * * * /usr/bin/python3 /path/to/crypto-etl/src/etl.py >> logs/etl.log 2>&1

📋 Example Output
Inserted crypto prices:
      coin      price                  timestamp
0