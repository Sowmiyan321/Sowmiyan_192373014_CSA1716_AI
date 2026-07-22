N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

def is_safe(board, row, col):

    for i in range(col):
        if board[row][i]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0

    return False

board = [[0]*N for _ in range(N)]

if solve(board, 0):
    print_board(board)
else:
    print("No Solution")