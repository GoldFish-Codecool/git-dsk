def menu()
    while True
        print("1. Player A vs Player B")
        print("2. Player vs Computer")
        print("3. Computer vs Computer")

        choice = input("Enter your choice: ")
        if choice =="1":
            print("You chose option 1.")    
        elif choice == "2":
            print ("Option 2 is not ready yet, please select Option 1")
        elif choice == "3":
            print ("Option 3 is not ready yet, please select Option 1.")
        elif choice == "quit":
            break 
        else:
            print("Invalid choice, please enter a valid option.")

