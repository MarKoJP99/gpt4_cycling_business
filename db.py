import os
import sqlite3
import csv

# DATABASE is the path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "bicycles.db")

# get_db() is called in init_db() and search_products()
def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# init_db() is called in app.py
def init_db(app):
    with app.app_context():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        if not cur.fetchone():
            create_products_table()
            with open(os.path.join(BASE_DIR, "schema.sql"), "r") as f:
                conn.executescript(f.read())
            conn.commit()



# search_products() is the function that is called in app.py
def search_products(query):
    conn = get_db()
    cur = conn.cursor()
    query = f"%{query}%"
    cur.execute("SELECT DISTINCT * FROM products WHERE product_name LIKE ? OR description LIKE ?", (query, query))
    results = cur.fetchall()
    return results

# update_database() is called in update_db_script.py
def create_products_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            description TEXT,
            price REAL,
            size TEXT,
            weight REAL
        )
    """)
    conn.commit()
    conn.close()
