def add_log_entry():
    pass

def print_log_entries():
    pass

def menu():
    print("1. Enter log entry")
    print("2. Show all entries")
    print("3. Quit")
    choice = int(input("What is your choice"))
    return choice

if __name__=="__main__":
    choice = menu()
    while choice != 3:
        if choice == 1:
            add_log_entry()
        elif choice == 2:
            print_log_entries()
        choice = menu()
    
    