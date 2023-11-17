import os
from game import Game

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
print('Welcome to Tic-Tac-Toe!\n')

# Create a new game
game = Game()

print(f'\n{game.player1.name} ({game.player1.symbol}) vs {game.player2.name} ({game.player2.symbol})\n')
input('Press Enter to continue...')

# Start the game
game.play_game()

# Clear the screen. Print final board. Print results.
os.system('cls' if os.name == 'nt' else 'clear')
game.board.display_board()
print(game.message)

game.leadership_board.display_leaderboard()
