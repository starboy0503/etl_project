for running dashboard streamlit run src/dashboard.py

🚀 Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, Pandas, and SQLite, along with a Streamlit dashboard for visualization.

The pipeline takes raw sales data from a CSV file, processes it to calculate revenue, and loads it into a SQLite database. The dashboard then reads from the database and visualizes sales insights.

🛠️ Tech Stack

Python 3.10+

Pandas → Data extraction & transformation

SQLite → Lightweight database for storage

Streamlit → Interactive dashboard

📂 Project Structure
csv-sales-etl/
│── data/
│    └── sales.csv        # Raw sales data (CSV file)
│
│── db/
│    └── sales.db         # SQLite database
│    └── schema.sql       # Database schema
│
│── src/
│    ├── extract.py       # Extract step
│    ├── transform.py     # Transform step
│    ├── load.py          # Load step
│    ├── etl.py           # ETL orchestrator
│    └── dashboard.py     # Streamlit dashboard
│
│── README.md

⚙️ Setup

Clone the repo

git clone https://github.com/<your-username>/csv-sales-etl.git
cd csv-sales-etl


Create & activate a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Initialize the database schema

sqlite3 db/sales.db < db/schema.sql

▶️ Run ETL

Extract → Transform → Load sales data from CSV to SQLite:

python src/etl.py

📊 Run Dashboard

Launch the interactive sales dashboard:

streamlit run src/dashboard.py


You’ll see:

Raw sales data

Bar chart → Sales by product

Line chart → Sales by date

KPI metrics → Total Sales, Total Orders, Unique Products

📋 Example Output
📥 Extracting data...
🔄 Transforming data...
💾 Loading data into SQLite...
✅ ETL Process Completed!


Dashboard View:

Total Sales = $1,870

Total Orders = 5

Products Sold = 4

✨ Future Improvements

Add filters (by product / date range) in dashboard

Schedule ETL runs with cron/Airflow

Export reports in Excel/PDF

Extend to use PostgreSQL for larger datasets