def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)


def check_winner(board, player):
  for row in board:
    if all(cell == player for cell in row):
      return True
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  if all(board[row][row] == player for row in range(3)):
    return True

  if all(board[row][2 - row] == player for row in range(3)):
    return True

  return False


def is_board_full(board):
  for row in board:
    for cell in row:
      if cell == " ":
        return False
  return True


def play_tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    print_board(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == " ":
      board[row][col] = current_player
    else:
      print("That cell is already occupied. Try again.")
      continue

    if check_winner(board, current_player):
      print_board(board)
      print(f"{current_player} wins!")
      break

    if is_board_full(board):
      print_board(board)
      print("It's a tie!")
      break


play_tic_tac_toe ()

