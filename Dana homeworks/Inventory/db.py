import psycopg2

DB_name = "xokifxcx"
USER = "xokifxcx"
PASSWORD = "7Rrpd7lF5MeFtiz6CLRG3PObvC9KSodl"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_name, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_products():
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    for product in products:
        print(product)
