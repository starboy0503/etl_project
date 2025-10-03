from extract import fetch_news
from transform import transform_articles
from load import load_articles

def run_news_etl():
    articles = fetch_news()
    clean_data = transform_articles(articles)
    load_articles(clean_data)
    print(f"✅ Loaded {len(clean_data)} articles")

if __name__ == "__main__":
    run_news_etl()
