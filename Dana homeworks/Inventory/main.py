from db import *

if __name__ == "__main__":
    while True:
        print("\nInventory Management Menu")
        print("1. List products")
        print("2. Add product")
        print("3. Delete product")
        print("4. Update product")
        print("X. Exit")

        choice = input ("Enter your choice:")

        if choice == "1":
            get_products()

        elif choice == "2":
            name = input ("Product name :")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            add_product(name, quantity, price)

        elif choice == "3":
            product_id = int(input("Product_id: "))
            delete_product(product_id)

        elif choice == "4":
            product_id = int(input("Product:id: "))
            name = input ("Product name :")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            update_product(product_id, name, quantity, price)

        elif choice.upper() == "X":
            break 