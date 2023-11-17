def get_table ():

    table = [
    ['','1','|','2','|','3'],
    ['A','.','|','.','|','.'],
    ['-','-','+','-','+','-'],
    ['B','.','|','.','|','.'],
    ['-','-','+','-','+','-'],
    ['C','.','|','.','|','.'],
    ]


    #table [2][2] = 'O'

    for row in table:
        for element in row:
            print (element)
        #print ()
 

get_table ()
