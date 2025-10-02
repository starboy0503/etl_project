import sys, os
sys.path.append(os.path.dirname(__file__))
from extract import extract_data
from transform import transform_data
from load import load_to_sqlite

def run_etl():
    print("Extracting data...")
    df=extract_data()

    print("Transforming data...")
    df=transform_data(df)

    print("Loading data...")
    load_to_sqlite(df)

    print("ETL process completed.")

if __name__=="__main__":
    run_etl()