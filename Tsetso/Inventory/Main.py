from db import * 

if __name__ == "__main__":
    while True:
        print("\Inventory Management menu")
        print("1. List Products")
        print("2. Add products")
        print("X. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            get_products()
        elif choice == "2":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            add_product(name, quantity, price)
        elif choice.upper() == "X":
            break