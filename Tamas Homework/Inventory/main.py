from dbPostGre import *

if __name__ == "__main__":
    
    while True:
        print("\nInvetory Management Menu")
        print("1. List products")
        print("2. Add product")
        print("3. Delete product")
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
        elif choice.upper() == "X" :
            break


