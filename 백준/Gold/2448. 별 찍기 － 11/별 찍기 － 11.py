N = int(input())

board = [[' '] * N * 2 for _ in range(N)]

def recursion(i, j, size):
    if size == 3:
        board[i][j] = '*'
        board[i+1][j-1] = board[i+1][j+1] = '*'
        for k in range(-2, 3):
            board[i+2][j+k] = '*'
    else:
        new_size = size // 2
        recursion(i, j, new_size)
        recursion(i + new_size, j - new_size, new_size)
        recursion(i + new_size, j + new_size, new_size)

recursion(0, N - 1, N)

for line in board:
    print("".join(line))