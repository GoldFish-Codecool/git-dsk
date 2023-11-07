import psycopg2

DB_NAME = "nvstxtyi"
USER = "nvstxtyi"
PASSWORD = "dSUv-8aMx4nGV230q9pDsDz4HxCeXH7m"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()


def get_products():
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    for product in products:
        print(product)


