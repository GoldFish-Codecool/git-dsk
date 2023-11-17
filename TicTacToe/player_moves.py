def get_player_moves(table):
    while True:
        move = input("Write your move (e.g. A1, A3, B3): ").upper()
        if move == "QUIT":
            row, col = (1,1)
            interrupt_game = True
            break
        else:
            interrupt_game = False
            if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":           
                print("Invalid input. Please enter a row (A-C) and a column (1-3).")
                continue
            row, col = 2 * (ord(move[0]) - ord('A')) + 1, 2 * (int(move[1]) - 1) + 1
            if table[row][col] != '.':
                print("That space is already taken. Try again.")
                continue
            break
    return row, col, interrupt_game
