-- removed the DROP TABLE IF EXISTS products as i 
-- dont want to update the table each time i run upload 
-- a new csv file

-- DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    size TEXT NOT NULL,
    weight REAL NOT NULL
);


