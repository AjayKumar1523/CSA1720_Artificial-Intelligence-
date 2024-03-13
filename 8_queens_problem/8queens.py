def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = "Q"

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = "."

    return False

def solve_n_queens():
    board = [["."]*N for _ in range(N)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

def print_solution(board):
    for row in board:
        print(" ".join(row))

N = 8

num_solutions = int(input("Enter the number of possible arrangements you want: "))
for _ in range(num_solutions):
    print(f"\nSolution {_ + 1}:")
    solve_n_queens()
