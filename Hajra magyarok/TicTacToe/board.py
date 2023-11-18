class Board:
    def __init__(self, mask=['•','•','•','•','•','•','•','•','•']):
        self.board = {'a1':mask[0], 'a2':mask[1], 'a3':mask[2], 'b1':mask[3], 'b2':mask[4], 'b3':mask[5], 'c1':mask[6], 'c2':mask[7], 'c3':mask[8]}

    def display_board(self):
        print('\n')
        print('    1   2   3')
        print('a   ' + self.board['a1'] + ' | ' + self.board['a2'] + ' | ' + self.board['a3'])
        print('   ---+---+---')
        print('b   ' + self.board['b1'] + ' | ' + self.board['b2'] + ' | ' + self.board['b3'])
        print('   ---+---+---')
        print('c   ' + self.board['c1'] + ' | ' + self.board['c2'] + ' | ' + self.board['c3'])
        print('\n')
        