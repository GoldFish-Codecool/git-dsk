import os
import random
from board import Board
from player import Player
from leadboard import LeadershipBoard


class Game:
    def __init__(self, AI = 2):
        self.leadership_board = LeadershipBoard()
        self.board = Board()
        self.AI = AI  # 1: Player vs Player mode, 2: Player vs AI mode, 3: AI vs AI mode
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.status = True  # True: Game is on, False: Game is over
        self.message = ''

        # Initaite the game. Starts with players. Print board.
        self.initiate_game()
    
    def initiate_game(self):
        if self.AI == 3: # AI vs AI
            self.player1 = Player('Computer 1', 'X', True)
            self.player2 = Player('Computer 2', 'O', True)
        elif self.AI == 2: # Player vs AI
            self.player1 = Player(input('Player 1 name: '), 'X', False)
            self.leadership_board.add_player(self.player1.name)
            self.player2 = Player('Computer', 'O', True)
        else: # Player vs Player
            self.player1 = Player(input('Player 1 name: '), 'X', False)
            self.leadership_board.add_player(self.player1.name)
            self.player2 = Player(input('Player 2 name: '), 'O', False)
            self.leadership_board.add_player(self.player2.name)

        self.active_player = self.player1
        self.message = f'{self.active_player.name} turn ({self.active_player.symbol}).'

    def play_game(self):
    # Play the game
        while self.status:
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the board
            self.board.display_board()
            print(self.message)


            # Get the player's or AI's move
            if self.active_player.AI:
                move = self.get_AI_move()
            else:
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
    # Get the player's move
        move = input('\nWhat is your move (A1...C3): ').lower()

        return move
    
    def get_AI_move(self):
    # Get the AI's move
        possible_moves = [key for key in self.board.board.keys() if self.board.board[key] == '•']
        
        move = random.choice(possible_moves)

        return move


    
    def make_move(self, move):
    # Make the move
        # Check if move is valid
        if self.board.board[move] == '•':
            # Make the move
            self.board.board[move] = self.active_player.symbol

            # Check for a winner
            if self.check_for_winners():
                self.message = f'{self.active_player.name} wins!\n'
                self.leadership_board.save_score(self.active_player.name, 2) if not self.active_player.AI else None
                self.status = False
                return
            # If no winner check for draw
            elif self.check_for_draw():
                self.message = 'It\'s a tie!\n'
                self.leadership_board.save_score(self.player1.name, 1) if not self.player1.AI else None
                self.leadership_board.save_score(self.player2.name, 1) if not self.player2.AI else None
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
    # Check if the board is full, which means a draw
        if '•' not in self.board.board.values():
            return True

    def check_for_winners(self):
    # Check if there is a winner
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
    

