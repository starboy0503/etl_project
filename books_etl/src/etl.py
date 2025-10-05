from extract import get_books
from transform import transform_books
from load import load_books, truncate_books, check_duplicates

def run_books_etl(query="python", max_results=10, refresh=False):
    print(f"🔍 Extracting books for query: '{query}'")

    raw_books = get_books(query, max_results)
    print(f"✅ Extracted {len(raw_books)} records")

    transformed = transform_books(raw_books)
    print(f"🧹 Transformed {len(transformed)} records")

    if refresh:
        truncate_books()
        print("🧽 Old data cleared before reload.")

    load_books(transformed)
    check_duplicates()
    print(f"💾 Loaded data into SQLite successfully!")

if __name__ == "__main__":
    run_books_etl("data science", 20, refresh=True)
