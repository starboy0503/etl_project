import time
from extract import extract_metrics
from transform import transform_metrics
from load import load_to_db
from config import POLL_INTERVAL

def run_metrics_etl():
    print("📊 Starting System Metrics ETL...")
    while True:
        data=extract_metrics()
        df=transform_metrics(data)
        load_to_db(df)
        print(f"✅ Loaded metrics at {data['timestamp']}")
        time.sleep(POLL_INTERVAL)

if __name__=="__main__":
    run_metrics_etl()