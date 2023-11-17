def print_table (table):

    import get_table

    for row in table:
        for element in row:
            print (element, end=" ")
        print ()