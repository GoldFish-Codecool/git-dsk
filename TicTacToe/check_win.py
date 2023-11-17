def win (table):

    winner = False
    if  ((table[1][1] == table[1][3] == table[1][5]) or
        (table[3][1] == table[3][3] == table[3][5]) or
        (table[5][1] == table[5][3] == table[5][5]) or
        (table[1][1] == table[3][3] == table[5][5]) or 
        (table[5][1] == table[3][3] == table[1][5])):
        winner = True

    return winner



    


