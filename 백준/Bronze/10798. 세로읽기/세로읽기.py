import sys

board = [i.rstrip() for i in sys.stdin.readlines()]
for i in range(max(map(len, board))):
    for j in range(len(board)):
        if i >= len(board[j]):
            continue
        sys.stdout.write(board[j][i])