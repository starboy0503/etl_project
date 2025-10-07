from extract import extract_articles
from transform import transform_articles
from load import load_to_db

def run_webscape_etl():
    print("🔍 Extracting articles...")
    articles=extract_articles()
    print(f"✅ Found {len(articles)} articles")

    print("🧹 Transforming data...")
    df=transform_articles(articles)

    print("💾 Loading to database...")
    load_to_db(df)

    print("🎉 Web Scraping ETL complete!")

if __name__=="__main__":
    run_webscape_etl()
