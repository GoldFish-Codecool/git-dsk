from Define_menu import menu

def players_name_char ():

    option = menu()
    
    if option == "1":
        player_A_name = input("First Player, Please enter your name: ")
        player_A_char = input("Please select character: (X/O)").upper()

        while player_A_char not in ["X", "O"]:
            player_A_char = input("Select a valid character!  (X/O)")

        player_B_name = input("Second player, Please enter your name: ")
        
    elif option == "2":
        player_A_name = input("First Player, Please enter your name: ")
        player_A_char = input("Please select character: (X/O)").upper()

        while player_A_char not in ["X", "O"]:
            player_A_char = input("Select a valid character!  (X/O)")

        player_B_name = "Computer"
    
    elif option == "3":
        player_A_name = "Computer 1"
        player_B_name = "Computer 2"
        player_A_char = "X"
        
    print ()
    if player_A_char == "X":
        player_B_char = "O"
        print (f"{player_A_name} starts! \n")
    else:
        player_B_char = "X"
        print (f"{player_B_name} starts! \n")
    
    player_A = [player_A_name, player_A_char]
    player_B = [player_B_name, player_B_char]

    return (player_A, player_B)





