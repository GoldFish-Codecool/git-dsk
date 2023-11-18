from create_table import get_table
from print_board import print_table
from Define_menu import menu
from players import players_name_char
from player_moves import get_player_moves
from move import make_move
from check_win import win
from check_draw import is_board_full
from leaderboardpeter import *

menu()
player_A, player_B = players_name_char()
board = get_table()
player_turn = []
if player_A [1] == "X":
    player_turn = player_A
else:
    player_turn = player_B

#current_player = 'X'

while True:
    interrupt_game = False
    print_table(board)
    print(f"\n\033[1;31m{player_turn[0]}\033[0m")
    row, col, interrupt_game = get_player_moves(board)

    if interrupt_game == True:
        print("Sorry to see you go in the middle of a game")
        exit()

    make_move(board, row, col, player_turn[1])

    if win(board):
        print_table(board)
        print(f"Player {player_turn[0]} wins!")
        winner = player_A[0] if player_turn == player_A else player_B[0]
        opponent = player_B[0] if player_turn == player_A else player_A[0]
        xoro= player_turn[1]
        add_winner(winner, opponent, xoro)
        break
    
    if is_board_full(board):
        print_table(board)
        print("It's a draw!")
        break

    if player_turn == player_A:
        player_turn = player_B
    else:
        player_turn = player_A
    #current_player = 'O' if current_player == 'X' else 'X'