import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(list(map(int, input().split()))) for _ in range(N)]

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv_di = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

cctv = deque()
answer = 0

for y in range(N):
    for x in range(M):
        if board[y][x] != 6 and board[y][x] != 0:
            cctv.append((board[y][x], x, y))
        if board[y][x] == 0:
            answer += 1


def count_zero(board_copy):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if board_copy[y][x] == 0:
                cnt += 1
    return cnt


def move(x, y, direc, board_copy):
    for d in direc:
        nx, ny = x, y
        dx, dy = di[d]
        while True:
            nx += dx
            ny += dy
            if ny < 0 or ny >= N or nx < 0 or nx >= M or board_copy[ny][nx] == 6:
                break
            if board_copy[ny][nx] != 0:
                continue
            board_copy[ny][nx] = '#'


def dfs(n, board):
    global answer
    board_copy = [[j for j in board[i]] for i in range(N)]

    if n == len(cctv):
        answer = min(answer, count_zero(board_copy))
        return

    number, x, y = cctv[n]

    for d in cctv_di[number]:
        move(x, y, d, board_copy)
        dfs(n + 1, board_copy)
        board_copy = [[j for j in board[i]] for i in range(N)]


dfs(0, board)
print(answer)
