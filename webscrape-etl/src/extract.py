import requests
from bs4 import BeautifulSoup
from config import NEWS_URL, MAX_ARTICLES

def extract_articles():
    """Scrape top articles from Hacker News"""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    response = requests.get(NEWS_URL, headers=headers, timeout=10)

    if response.status_code != 200:
        print(f"⚠️ Failed to fetch page. Status: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    rows = soup.select("tr.athing")  # main rows of articles

    for item in rows[:MAX_ARTICLES]:
        title_tag = item.select_one(".titleline a")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = title_tag["href"]

        # Get the next row to find author info
        subtext = item.find_next_sibling("tr").select_one(".subtext")
        author_tag = subtext.select_one(".hnuser") if subtext else None
        author = author_tag.get_text(strip=True) if author_tag else "Unknown"

        articles.append({
            "title": title,
            "author": author,
            "date": None,  # Hacker News homepage doesn’t provide date
            "link": link
        })

    print(f"✅ Found {len(articles)} articles")
    return articles
