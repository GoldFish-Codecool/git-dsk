def add_log_entry():
    log_file = open("log.txt", "a+")
    log_entry = input("Log entry: ")
    log_file.write(log_entry + "\n")
    log_file.close()


def print_log_entries():
    log_file = open("log.txt", "r")
    for line in log_file:
        print(line)
    log_file.close()


def menu():
    print("1. Enter log entry")
    print("2. Show all entries")
    print("3. Quit")
    choice = int(input("What is your choice\n"))
    return choice


if __name__=="__main__":

    choice = menu()
    while choice != 3:
        if choice == 1:
            add_log_entry()
        elif choice == 2:
            print_log_entries()
        choice = menu()
    
    