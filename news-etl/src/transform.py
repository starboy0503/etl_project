from textblob import TextBlob

def transform_articles(articles):
    transformed = []
    for a in articles:
        headline = a.get("title")
        source = a.get("source", {}).get("name")
        published = a.get("publishedAt")
        sentiment = TextBlob(headline).sentiment.polarity if headline else 0
        transformed.append({
            "headline": headline,
            "source": source,
            "published_at": published,
            "sentiment": sentiment
        })
    return transformed
