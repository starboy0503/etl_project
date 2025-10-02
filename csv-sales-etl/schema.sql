CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT,
    total REAL
);
