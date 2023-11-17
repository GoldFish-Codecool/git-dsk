from create_table import get_table
from print_board import print_table
from Define_menu import menu
from players import players_name_char
from player_moves import get_player_moves
from move import make_move
from check_win import win
from check_draw import is_board_full

menu()
players_name_char()
board = get_table()
current_player = 'X'

while True:
    print_table(board)
    row, col = get_player_moves(board)
    make_move(board, row, col, current_player)

    if win(winner):
        print_table(board)
        print(f"Player {current_player} wins!")
        break
    
    if is_board_full(board):
        print_table(board)
        print("It's a draw!")
        break

  current_player = 'O' if current_player == 'X' else 'X'