import pandas as pd

def transform_metrics(data):
    "Convert to Dataframe and clean data"
    df=pd.DataFrame([data])
    df["timestamp"]=pd.to_datetime(df["timestamp"])
    return df