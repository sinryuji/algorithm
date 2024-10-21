# https://www.acmicpc.net/problem/18405

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
board = []
q = []
for y in range(N):
    board.append(list(map(int, input().split())))
    for x in range(N):
        if board[y][x] > 0:
            q.append((board[y][x], x, y, 0))
S, X, Y = map(int, input().split())

q = deque(sorted(q, key=lambda x: x[0]))
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    i, x, y, sec = q.popleft()
    if sec == S:
        break
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
            board[ny][nx] = i
            q.append((i, nx, ny, sec + 1))

print(board[X-1][Y-1])
