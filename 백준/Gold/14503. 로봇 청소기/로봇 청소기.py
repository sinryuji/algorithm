import sys

input = sys.stdin.readline


def find(r, c, d):
    global board
    for i in range(4):
        d -= 1
        dr, dc = di[d]
        nr, nc = dr + r, dc + c
        if board[nr][nc] == 0:
            return (nr, nc, d + 4 if d < 0 else d)
    return (-1, -1, -1)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1
    nr, nc, dd = find(r, c, d)
    if not (nr == -1 and nc == -1):
        r, c, d = nr, nc, dd
    else:
        dr, dc = di[d - 2]
        r += dr
        c += dc
        if board[r][c] == 1:
            break

print(answer)