CREATE TABLE IF NOT EXISTS headlines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT,
    source TEXT,
    published_at TEXT,
    sentiment REAL
);
