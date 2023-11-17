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
    interrupt_game = False
    print_table(board)
    row, col, interrupt_game = get_player_moves(board)

    if interrupt_game == True:
        print("Sorry to see you go in the middle of a game")
        exit()

    make_move(board, row, col, current_player)

    if win(board):
        print_table(board)
        print(f"Player {current_player} wins!")
        break
    
    if is_board_full(board):
        print_table(board)
        print("It's a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'