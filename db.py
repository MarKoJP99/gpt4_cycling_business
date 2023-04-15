# Functions for interacting with the SQLite database


import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "bicycles.db")

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    conn = get_db()
    with open(os.path.join(BASE_DIR, "schema.sql"), "r") as f:
        conn.executescript(f.read())
    conn.commit()


def search_products(query):
    conn = get_db()
    cur = conn.cursor()
    query = f"%{query}%"
    cur.execute("SELECT DISTINCT * FROM products WHERE product_name LIKE ? OR description LIKE ?", (query, query))
    results = cur.fetchall()
    return results