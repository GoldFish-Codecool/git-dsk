import psycopg2

DB_NAME ="hucodjek"
USER = "hucodjek"
PASSWORD = "Eryt_3nZU6fPM3tO1Q11735_FJIvBAys"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_products() :
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    for product in products :
        print(product)

def add_product(name, quantity, price) :
    cur.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s) RETURNING iD;", (name, quantity, price))
    product_id = cur.fetchone()[0]
    conn.commit
    print (f"Product added with id: {product_id}")

def delete_product(product_id) :
    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit
    print(f"Successfully deleted id {product_id}")




