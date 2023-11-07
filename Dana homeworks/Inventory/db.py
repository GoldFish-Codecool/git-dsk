import psycopg2

DB_name = "xokifxcx"
USER = "xokifxcx"
PASSWORD = "7Rrpd7lF5MeFtiz6CLRG3PObvC9KSodl"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_name, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_products():
    cur.execute("SELECT * FROM products ORDER BY id;")
    products = cur.fetchall()
    for product in products:
        print(product)

def add_product(name, quantity, price):
    cur.execute("INSERT INTO products(name, quantity, price) VALUES (%s, %s, %s) RETURNING id;",
                (name, quantity, price))
    product_id = cur.fetchone()[0]
    conn.commit()
    print(f"Product added with id: {id}")

def delete_product (product_id):
    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    print(f"Product with id {product_id} deleted successfully")

def update_product(product_id, name, quantity, price):
    cur.execute("UPDATE products SET name = %s, quantity = %s, price = %s WHERE id = %s;",(name, quantity, price, product_id))
    conn.commit()
    print(f"Product with id {product_id} updated successfully")