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
