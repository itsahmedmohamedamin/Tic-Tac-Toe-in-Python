def print_board(board):
    print("  1   2   3")  # Column numbers
    for i, row in enumerate(board):
        print(f"{i + 1} {' | '.join(row)}")  # Row number and row content
        if i < 2:
            print("  -" * 5)

def check_win(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
            row, col = row - 1, col - 1  # Adjusting for 0-based indexing
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def choose_symbols():
    while True:
        symbol = input("Choose your symbol (X/O): ").upper()
        if symbol in ['X', 'O']:
            return symbol, 'O' if symbol == 'X' else 'X'
        else:
            print("Invalid symbol. Please choose X or O.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player1, player2 = choose_symbols()
    current_player = player1
    
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
