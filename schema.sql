-- removed the DROP TABLE IF EXISTS products as i 
-- dont want to update the table each time i run upload 
-- a new csv file

-- DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    size TEXT NOT NULL
);

INSERT INTO products (product_name, description, price, size)
VALUES
('Bike 1', 'Description for Bike 1', 1000, 'L'),
('Bike 2', 'Description for Bike 2', 1200, 'M'),
('Bike 3', 'Description for Bike 3', 800, 'S'),
('Bike 4', 'Description for Bike 4', 1500, 'XL');
