class Board:
    def __init__(self):
        self.board = []
        self.get_empty_board()


    def get_empty_board(self):
        self.board = {'a1':'•', 'a2':'•', 'a3':'•', 'b1':'•', 'b2':'•', 'b3':'•', 'c1':'•', 'c2':'•', 'c3':'•'}

    def display_board(self):
        print('\n')
        print('    1   2   3')
        print('a   ' + self.board['a1'] + ' | ' + self.board['a2'] + ' | ' + self.board['a3'])
        print('   ---+---+---')
        print('b   ' + self.board['b1'] + ' | ' + self.board['b2'] + ' | ' + self.board['b3'])
        print('   ---+---+---')
        print('c   ' + self.board['c1'] + ' | ' + self.board['c2'] + ' | ' + self.board['c3'])
        print('\n')
        