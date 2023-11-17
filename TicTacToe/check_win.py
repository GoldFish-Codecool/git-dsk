def win (table):
    # Check rows, columns, and diagonals for a winner
    for i in [1, 3, 5]:  # Rows
        if table[i][1] == table[i][3] == table[i][5] != '.':
            return True
    for i in [1, 3, 5]:  # Columns
        if table[1][i] == table[3][i] == table[5][i] != '.':
            return True
    # Diagonals
    if table[1][1] == table[3][3] == table[5][5] != '.' or \
       table[1][5] == table[3][3] == table[5][1] != '.':
        return True
    return False




    


