import pandas as pd
def extract_data(csv_path="/Users/adityadhanrajsingh/Desktop/etl_projects/csv-sales-etl/data/sales.csv"):
    df=pd.read_csv(csv_path)
    return df
