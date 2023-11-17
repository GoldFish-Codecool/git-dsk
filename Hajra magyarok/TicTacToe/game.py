import os
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
        self.player1 = Player(input('Player 1 name: '), 'X')
        self.player2 = Player(input('Player 2 name: '), 'O')
        self.active_player = self.player1
        self.message = f'{self.active_player.name} turn ({self.active_player.symbol}).'

    def play_game(self):
        while self.status:
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the board
            self.board.display_board()
            print(self.message)
            move = self.get_player_move()

            # Check if move is valid
            if move in ['quit', 'q']:
                print('Thanks for playing!\n')
                self.status = False 
            elif move in ['help', 'h']:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Valid moves are: A1, A2, A3, B1, B2, B3, C1, C2, C3\n')
                input('Press Enter to continue...')
            elif move in self.board.board.keys():
                self.make_move(move)
            else:
                self.message = f'{move} is not a valid move. Please try again. \n\n{self.active_player.name} turn.'

    def get_player_move(self):
        move = input('What is your move (A1...C3): ').lower()

        return move
    
    def make_move(self, move):
        # Check if move is valid
        if self.board.board[move] == '•':
            # Make the move
            self.board.board[move] = self.active_player.symbol

            # Check for a winner
            if self.check_for_winners():
                self.message = f'{self.active_player.name} wins!\n'
                self.status = False
                return
            # If no winner check for draw
            elif self.check_for_draw():
                self.message = 'It\'s a tie!\n'
                self.status = False
                return
            else:
                # Switch players
                if self.active_player == self.player1:
                    self.active_player = self.player2
                else:
                    self.active_player = self.player1
                self.message = f'{self.active_player.name} turn ({self.active_player.symbol}).'

        # If move is not valid
        else:
            self.message = f'{move} is not empty. Please try again. \n\n{self.active_player.name} turn ({self.active_player.symbol}).'

    def check_for_draw(self):
        if '•' not in self.board.board.values():
            return True

    def check_for_winners(self):
        winning_combinations = [
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1']
        ]

        for combination in winning_combinations:
            if self.board.board[combination[0]] == self.board.board[combination[1]] == self.board.board[combination[2]] != '•':
                return True
    

