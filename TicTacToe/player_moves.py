def get_player_moves():
    while True:
        move = input("Write your move (e.g. A1, A3, B3)"\n).upper()
        if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
            print("Invalid input. Please enter a row (A-C) and a column (1-3).")
            continue
        row, col = ord(move[0]) - 65, int(move[1]) - 1
        if board[row][col] != '.':
                print("That space is already taken. Try again.")
                continue
        return row, col