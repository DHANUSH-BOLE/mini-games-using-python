def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
print("Welcome to Tic Tac Toe!")
d={
    'X':'',
    'O':''
}
d['X']+=input("player name who plays for X:")
d['O']+=input("player name who plays for O:")

while True:
    print_board(board)
    row = int(input(f"Player {d[current_player]}, enter row (1-3): ")) - 1
    col = int(input(f"Player {d[current_player]}, enter column (1-3): ")) - 1

    if row<0 or row>3 or col<0 or col>3:
        print("Invalid move, Try Again")
        continue
    # Check if the selected cell is empty
    if board[row][col] != " " :
        print("That cell is already taken. Try again.")
        continue
    board[row][col] = current_player

    # Check for a winner or a tie
    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"