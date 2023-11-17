import os
from game import Game

game = Game()

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
print('Welcome to Tic-Tac-Toe!\n')
print(f'{game.player1.name} vs {game.player2.name}\n')
input('Press Enter to continue...')

while game.status:
  # Clear the screen
  os.system('cls' if os.name == 'nt' else 'clear')

  game.board.display_board()
  print(game.message)
  move = game.get_player_move()

  if move in ['quit', 'q']:
    print('Thanks for playing!\n')
    game.status = False
  elif move in ['help', 'h']:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Valid moves are: A1, A2, A3, B1, B2, B3, C1, C2, C3\n')
    input('Press Enter to continue...')
  elif move in game.board.board.keys():
    game.make_move(move)
  else:
    game.message = f'{move} is not a valid move. Please try again. \n\n{game.active_player.name} turn.'
  

