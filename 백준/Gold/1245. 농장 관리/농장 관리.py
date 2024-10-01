import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    global N, M
    visited[y][x] = True
    d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] > board[y][x]:
                return 0
            if board[ny][nx] == board[y][x]:
                visited[ny][nx] = True
                q.append((nx, ny))
                check_idx.append((nx, ny))

    return 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

check_idx = []

answer = 0
for row in range(N):
    for col in range(M):
        if (col, row) not in check_idx:
            visited = [[False] * M for _ in range(N)]
            answer += bfs(col, row)

print(answer)