CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    authors TEXT,
    publisher TEXT,
    published_date TEXT,
    categories TEXT,
    average_rating REAL,
    ratings_count INTEGER,
    page_count INTEGER,
    language TEXT,
    description TEXT
);
