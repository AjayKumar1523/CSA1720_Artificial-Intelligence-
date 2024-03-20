import sys

# Define players
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"

# Define winning combinations
WINNING_COMBOS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def evaluate(board):
    for combo in WINNING_COMBOS:
        symbols = [board[i][j] for i, j in combo]
        if symbols == [PLAYER_X, PLAYER_X, PLAYER_X]:
            return 1
        elif symbols == [PLAYER_O, PLAYER_O, PLAYER_O]:
            return -1
    return 0

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    score = evaluate(board)
    if score != 0 or depth == 0:
        return score

    if maximizing_player:
        max_score = -sys.maxsize
        for move in available_moves(board):
            board[move[0]][move[1]] = PLAYER_X
            max_score = max(max_score, alpha_beta_pruning(board, depth - 1, alpha, beta, False))
            board[move[0]][move[1]] = EMPTY
            alpha = max(alpha, max_score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = sys.maxsize
        for move in available_moves(board):
            board[move[0]][move[1]] = PLAYER_O
            min_score = min(min_score, alpha_beta_pruning(board, depth - 1, alpha, beta, True))
            board[move[0]][move[1]] = EMPTY
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        return min_score

def best_move(board):
    best_score = -sys.maxsize
    move = None
    for possible_move in available_moves(board):
        board[possible_move[0]][possible_move[1]] = PLAYER_X
        score = alpha_beta_pruning(board, 5, -sys.maxsize, sys.maxsize, False)
        board[possible_move[0]][possible_move[1]] = EMPTY
        if score > best_score:
            best_score = score
            move = possible_move
    return move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    print_board(board)

    while True:
        player_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if board[player_move[0]][player_move[1]] == EMPTY:
            board[player_move[0]][player_move[1]] = PLAYER_O
            print_board(board)

            if evaluate(board) != 0:
                print("You win!")
                break

            if not available_moves(board):
                print("Draw!")
                break

            computer_move = best_move(board)
            board[computer_move[0]][computer_move[1]] = PLAYER_X
            print_board(board)

            if evaluate(board) != 0:
                print("Computer wins!")
                break

            if not available_moves(board):
                print("Draw!")
                break
        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()
