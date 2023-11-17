def get_table ():

    table = [
    [' ','1','|','2','|','3'],
    ['A','.','|','.','|','.'],
    ['-','-','+','-','+','-'],
    ['B','.','|','.','|','.'],
    ['-','-','+','-','+','-'],
    ['C','.','|','.','|','.'],
    ]

    table [1][1] = 'O'
    table [5][3] = 'X'
    table [5][3] = 'O'

    for row in table:
        for element in row:
            print (element, end=" ")
        print ()
 

get_table ()
