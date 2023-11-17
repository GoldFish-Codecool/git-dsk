import table from create_table:

for row in table:
    for element in row:
        if element == X or element == 0:
            print("Drawn! Do you want to restart? (Y/N)")