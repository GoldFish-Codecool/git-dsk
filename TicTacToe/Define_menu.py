from leaderboardpeter import get_winners
from Leaderboard_summary import get_leaderboard

def menu():
    while True:
        print("1. Player A vs Player B")
        print("2. Player vs Computer")
        print("3. Computer vs Computer")
        print("4. List Game results - Winner|Opponent|Winner character")
        print("5. Show me the leaderboard!")
        print("You can leave the game anytime by typing quit in any form")

        choice = input("\n Enter your choice: ")
        if choice =="1":
            print("You chose Multiplayer option.")
            break    
        elif choice == "2":
            print ("You chose Human against Computer.")
            break
        elif choice == "3":
            print ("Robot fight! Watch!")
            break

        elif choice == "4": 
            get_winners()

        elif choice == "5":
            get_leaderboard()

        elif choice == "quit":
            print ("Sorry to see you go so soon. \n")
            exit() 
        else:
            print("Invalid choice, please enter a valid option.")

    return choice