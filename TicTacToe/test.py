from create_table import get_table
from print_board import print_table
from Define_menu import

#initialize table
table = get_table()
#print empty board
print_table (table)
#call the menu

#player moves asking for moves as long as check_draw or check_win is false

#announce the winner


while True:
    print_table(board)
    row, col = get_player_moves(board)
    make_move(board, row, col, current_player)

    if check_winner(board):
        print_table(board)
        print(f"Player {current_player} wins!")
        break
    if is_board_full(board):
        print_table(board)
        print("It's a draw!")
        break
