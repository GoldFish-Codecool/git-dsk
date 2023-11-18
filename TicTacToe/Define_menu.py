from leaderboardpeter import get_winners
from Leaderboard_summary import get_leaderboard

def menu():
    while True:
        print("1. Player A vs Player B")
        print("2. Player vs Computer")
        print("3. Computer vs Computer")
        print("4. List winners - Winner|Opponent|Winner character")
        print("5. Show me the leaderboard!")

        choice = input("Enter your choice: ")
        if choice =="1":
            print("You chose option 1.")
            break    
        elif choice == "2":
            print ("Option 2 is not ready yet, please select Option 1")
        elif choice == "3":
            print ("Option 3 is not ready yet, please select Option 1.")

        elif choice == "4": 
            get_winners()

        elif choice == "5":
            get_leaderboard()

        elif choice == "quit":
            break 
        else:
            print("Invalid choice, please enter a valid option.")

