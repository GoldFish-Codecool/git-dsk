import os
from game import Game

def get_settings():
  game_type = 0
  difficulty = 0

  # Choose game mode
  print('Choose game mode:')
  print(1, 'Player vs Player')
  print(2, 'Player vs AI')
  print(3, 'AI vs AI\n')

  while game_type not in [1, 2, 3]:
    game_type = int(input('Enter your choice (1, 2, 3): '))
  
  # Choose difficulty
  if game_type > 1:
    print('\nChoose difficulty:')
    print(1, 'Easy AI')
    print(2, 'Normal AI')
    print(3, 'Hard AI')
    
    while difficulty not in [1, 2, 3]:
      difficulty = int(input('Choose difficulty for AI (1, 2, 3): '))

  print()

  return [game_type, difficulty]


if __name__ == '__main__':

  # Clear the screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Welcome to Tic-Tac-Toe!\n')

  settings = get_settings()
  
  # Create a new game
  game = Game(settings[0], settings[1])

  # Start the game
  game.play_game()

    
