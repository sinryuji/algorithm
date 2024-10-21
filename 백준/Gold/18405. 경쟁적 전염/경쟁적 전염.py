import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

q = deque()
for i in range(1, K + 1):
    for y in range(N):
        for x in range(N):
            if board[y][x] == i:
                q.append((x, y, 0))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y, sec = q.popleft()
    if sec == S:
        break
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
            board[ny][nx] = board[y][x]
            q.append((nx, ny, sec + 1))

print(board[X-1][Y-1])
