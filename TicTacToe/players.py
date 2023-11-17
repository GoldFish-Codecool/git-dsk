def players ():
    
    player_A_name = input("First Player, Please enter your name: ")
    player_A_char = input("Please select character: (X/O)")

    while player_A_char not in ["X", "O"]:
            player_A_char = input("Select a valid character!  (X/O)")

    player_B_name = input("Second player, Please enter your name: ")
    if player_A_char == "X":
        player_B_char = "O"
    else:
        player_B_char = "X"

    return (player_A_name, player_A_char, player_B_name, player_B_char)





