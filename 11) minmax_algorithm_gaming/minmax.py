import math

def minimax(board, depth, is_maximizing):
    if check_winner(board) == 'X':
        return -1
    elif check_winner(board) == 'O':
        return 1
    elif check_winner(board) == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def check_winner(board):
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 'X'
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return 'O'

    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O'

    if any(' ' in row for row in board):
        return 'Continue'
    else:
        return 'Tie'

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def get_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    x, y = map(int, input("Enter your move (row column): ").split())
    if board[x][y] != ' ':
        print("Invalid move. Try again.")
        continue
    board[x][y] = 'X'

    if check_winner(board) == 'X':
        print("You win!")
        break
    elif check_winner(board) == 'Tie':
        print("It's a tie!")
        break

    print("Computer's move:")
    best_move = get_best_move(board)
    board[best_move[0]][best_move[1]] = 'O'

    if check_winner(board) == 'O':
        print("Computer wins!")
        break
    elif check_winner(board) == 'Tie':
        print("It's a tie!")
        break
