import psycopg2

DB_NAME = "jwnldpso"
USER = "jwnldpso"
PASSWORD = "LthGD2n61WXRyqEj0n-1Li7-oWcrgNIM"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)

cur = conn.cursor()

def get_products():
    cur.execute("SELECT * FROM products ORDERED BY id;")
    products = cur.fetchall()
    for product in products:
        print(product)


def add_product(name, quantity, price):
    cur.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s) RETURNING id;",
                (name, quantity, price))
    product_id=cur.fetchone()[0]
    conn.commit()
    print(f"Product added with id:  {product_id}")

def delete_product(product_id):
    cur.execute ("DELETE FROM product WHERE id=%s", (product_id))
    conn.commit()
    print("Product with id {product_id} deleted successfully.") 

def update_product(product_id, name, quantity, price=0):
    cur.execute("UPDATE products SET name=%s, quantity=%s, price=%s WHERE id=%s;",
                (name, quantity, price, product_id))
    conn.commit()
    print(f"Product id with {product_id} updated successfully")