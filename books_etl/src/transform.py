def transform_books(raw_books):
    """Transform raw API data into clean structured rows"""
    books = []
    for book in raw_books:
        info = book.get("volumeInfo", {})
        books.append({
            "title": info.get("title"),
            "authors": ", ".join(info.get("authors", [])),
            "publisher": info.get("publisher"),
            "published_date": info.get("publishedDate"),
            "categories": ", ".join(info.get("categories", [])) if info.get("categories") else None,
            "average_rating": info.get("averageRating"),
            "ratings_count": info.get("ratingsCount"),
            "page_count": info.get("pageCount"),
            "language": info.get("language"),
            "description": info.get("description", None),
        })
    return books
