import os
from game import Game

def get_menu_choice():
  # Choose game mode
  print(1, 'Player vs Player')
  print(2, 'Player vs AI')
  print(3, 'AI vs AI\n')
  choice = 0

  while choice not in [1, 2, 3]:
    choice = int(input('Enter your choice (1, 2, 3): '))
  
  return choice


if __name__ == '__main__':

  # Clear the screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Welcome to Tic-Tac-Toe!\n')

  # Create a new game
  game = Game(get_menu_choice())

  print(f'\n{game.player1.name} ({game.player1.symbol}) vs {game.player2.name} ({game.player2.symbol})\n')
  input('Press Enter to continue...')

  # Start the game
  game.play_game()

    
