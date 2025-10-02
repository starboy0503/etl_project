CREATE TABLE IF NOT EXISTS blocks (
    block_number INTEGER PRIMARY KEY,
    block_hash TEXT,
    parent_hash TEXT,
    timestamp TIMESTAMP,
    tx_count INTEGER,
    gas_used TEXT,   -- casted as text to avoid overflow
    gas_limit TEXT,
    base_fee TEXT
);

CREATE TABLE IF NOT EXISTS transactions (
    tx_hash TEXT PRIMARY KEY,
    block_number INTEGER,
    from_address TEXT,
    to_address TEXT,
    value TEXT,       -- very large integers -> store as text
    gas TEXT,
    gas_price TEXT,
    nonce TEXT,
    tx_index INTEGER
);
