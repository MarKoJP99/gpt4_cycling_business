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
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                cur.execute(
                    "INSERT INTO products (product_name, description, price, size) VALUES (?, ?, ?, ?)",
                    (row[0], row[1], row[2], row[3]),
                )
        conn.commit()
    finally:
        conn.close()

csv_file = "csv_sample.csv"

# Run the script from the command line
if len(sys.argv) > 1:
    # csv_file = sys.argv[1]
    create_products_table()
    update_database(csv_file)
    print("Database updated successfully.")
    
else:
    print("Please provide a CSV file as an argument.")


"""
# using pandas create a csv file with the following data: product_name, description, price, size
csv_sample = pd.DataFrame({'product_name': ['bike1', 'bike2', 'bike3', 'bike4', 'bike5', 'bike6', 'bike7', 'bike8', 'bike9', 'bike10'],
                            'description': ['bike1 description', 'bike2 description', 'bike3 description', 'bike4 description', 'bike5 description', 'bike6 description', 'bike7 description', 'bike8 description', 'bike9 description', 'bike10 description'], 
                            'price': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
                            'size': ['L', 'M', 'S', 'XL', 'L', 'M', 'S', 'XL', 'L', 'M']})
csv_sample.to_csv('csv_sample.csv', index=False)


# function for displaying the products in the database
def display_products():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()

    print("ID | Product Name | Description | Price | Size")
    print("----------------------------------------------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")


# Display products before the update
print("Before updating the database:")
display_products()

# Update the database
update_database('csv_sample.csv')

# Display products after the update
print("\nAfter updating the database:")
display_products()
"""