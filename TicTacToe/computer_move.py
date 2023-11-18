import random

# here we define the computer move
def computer_move(board, computer_char):
    def check_potential_win_move(board, player_char):
        for row in range(1, 6, 2):  
            for col in range(1, 6, 2): 
                if board[row][col] == '.': 
                    board[row][col] = player_char 
                    if win(board): 
                        board[row][col] = '.' 
                        return (row, col)  
                    board[row][col] = '.' 
    return None

#define potential blocking moves

    def check_potential_block_move(board, opponent_char):
        for row in range(1, 6, 2):  
            for col in range(1, 6, 2):  
                if board[row][col] == '.': 
                    board[row][col] = opponent_char 
                    if win(board):  
                        board[row][col] = '.' 
                        return (row, col)  
                    board[row][col] = '.'  
    return None

    available_moves = [(r, c) for r in range(1, 6, 2) for c in range(1, 6, 2) if board[r][c] == '.']

#define the winning moves
    winning_move = check_potential_win_move(board, computer_char)
    if winning_move:
        return winning_move

    blocking_move = check_potential_block_move(board, 'O' if computer_char == 'X' else 'X')
    if blocking_move:
        return blocking_move

    return random.choice(available_moves) if available_moves else None
