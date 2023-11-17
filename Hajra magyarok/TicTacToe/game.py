from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.status = True
        self.message = ''

        # Initaite the game. Starts with players. Print board.
        self.initiate_game()
    
    def initiate_game(self):
        self.player1 = Player('Player 1', 'X')
        self.player2 = Player('Player 2', 'O')
        self.active_player = self.player1
        self.message = f'{self.active_player.name} turn.'

    def get_player_move(self):
        move = input('What is your move (A1...C3): ').lower()

        return move
    
    def make_move(self, move):
        
        if self.board.board[move] == '•':
            self.board.board[move] = self.active_player.symbol

            if self.active_player == self.player1:
                self.active_player = self.player2
            else:
                self.active_player = self.player1
            self.message = f'{self.active_player.name} turn.'

        else:
            self.message = f'{move} is not empty. Please try again. \n\n{self.active_player.name} turn.'
