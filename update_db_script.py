import sys
import csv
import sqlite3

from db import create_products_table, create_products_table

def get_db():
    db = sqlite3.connect("bicycles.db")
    return db

def update_database(filename):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                size TEXT NOT NULL,
                weight REAL NOT NULL
            )
        """)
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                cur.execute(
                    "INSERT OR IGNORE INTO products (product_name, description, price, size, weight) "
                    "SELECT ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM products WHERE product_name = ? AND description = ?)",
                    (row[0], row[1], row[2], row[3], row[4], row[0], row[1])
                )

        conn.commit()
    finally:
        conn.close()


# Run the script from the command line
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
    create_products_table()
    update_database(csv_file)
    print("Database updated successfully.")
    
else:
    print("Please provide a CSV file as an argument.")

