-- schema.sql
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    seats INTEGER NOT NULL,
    fuel TEXT NOT NULL,
    type TEXT NOT NULL,
    image_filename TEXT NOT NULL
);