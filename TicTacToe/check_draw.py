def drawn(table):
    drawn = True
    for raw in table:
        for element in row:
            if element == " ":
                drawn = False
                break

            if not drawn:
                break

            if drawn:
                print("Drawn! Do you want to play again? Y/N")
                