def is_board_full(table):

    for i in [1, 3, 5]:
        if '.' in table[i]:
            return False
    return True
