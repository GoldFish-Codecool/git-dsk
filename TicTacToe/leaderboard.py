import psycopg2

DB_NAME ="hucodjek"
USER = "hucodjek"
PASSWORD = "Eryt_3nZU6fPM3tO1Q11735_FJIvBAys"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_products() :
    cur.execute("SELECT * FROM products ORDER BY id;")
    products = cur.fetchall()
    for product in products :
        print(product)

def add_product(name, quantity, price) :
    cur.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s) RETURNING iD;", (name, quantity, price))
    product_id = cur.fetchone()[0]
    conn.commit()
    print (f"Product added with id: {product_id}")

def delete_product(product_id) :
    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    print(f"Successfully deleted id {product_id}")

def update_product(product_id, name, quantity, price = 0):
    cur.execute("UPDATE products SET name = %s, quantity = %s, price = %s WHERE id = %s;",
                (name, quantity, price, product_id))
    conn.commit()
    print(f"Product with id {product_id} updated successfully")

    from dbPostGre import *

if __name__ == "__main__":
    
    while True:
        print("\nInvetory Management Menu")
        print("1. List products")
        print("2. Add product")
        print("3. Delete product")
        print("4. Update product")
        print("X. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": 
            get_products()
        elif choice == "2" :
            name = input("Product name: ")
            quantity = input("Quantity: ")
            price = input("Price: ")
            add_product(name, quantity, price)
        elif choice == "3":
            product_id = int(input("Product id: "))
            delete_product(product_id)
        elif choice == "4" :
            product_id = int(input("Product_id: "))
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            update_product(product_id, name, quantity, price) 
        elif choice.upper() == "X" :
            break