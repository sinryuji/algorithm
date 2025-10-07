import sys
from collections import deque

input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(r, c):
    target = board[r][c]
    q = deque([(r, c)])
    pos = []

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and \
                board[nr][nc] == target:
                pos.append((nr, nc))
                q.append((nr, nc))
                visited[nr][nc] = True

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for r, c in pos:
            board[r][c] = '.'
            bomb_list.append((r, c))


def drop(arr):
    for r in rnage(6):
        cnt = 0
        for c in range(11, -1, -1):
            if arr[r][c] == '.':
                cnt += 1
            if arr[r][c] != '.' and cnt > 0:
                arr[r] = ['.'] * cnt + arr[r][:12 - cnt]


board = [list(input().rstrip()) for _ in range(12)]

ans = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    bomb_list = []

    for r in range(12):
        for c in range(6):
            if board[r][c] != '.' and not visited[r][c]:
                bfs(r, c)

    if len(bomb_list) == 0:
        break

    for bomb in bomb_list:
        r, c = bomb
        for i in range(r, 0, -1):
            board[i][c] = board[i - 1][c]
        board[0][c] = '.'

    ans += 1

print(ans)