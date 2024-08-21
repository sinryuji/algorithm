import sys
from collections import deque

input = sys.stdin.readline

d = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def bfs(board, x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    res = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                bfs(board, x, y)
                # print(board)
                res += 1
    print(res)