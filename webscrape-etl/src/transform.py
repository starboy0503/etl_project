import pandas as pd

def transform_articles(articles):
    """Clean and format scraped article data"""
    df=pd.DataFrame(articles)
    if df.empty:
        return df
    
    df.drop_duplicates(subset=["link"],inplace=True)

    df["date"]=pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d %H:%M")

    df["author"].fillna("Unknow",inplace=True)

    return df