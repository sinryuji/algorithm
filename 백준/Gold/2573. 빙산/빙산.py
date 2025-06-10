import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[y][x] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if board[ny][nx] == 0:
                    visited[y][x] += 1
                if visited[ny][nx] == 0 and board[ny][nx] > 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny))

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
while True:
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0 and board[y][x] > 0:
                bfs(x, y)
                cnt += 1

    for y in range(N):
        for x in range(M):
            if visited[y][x] > 0:
                board[y][x] -= (visited[y][x] - 1)
                if board[y][x] < 0:
                    board[y][x] = 0

    if cnt >= 2:
        print(answer)
        break

    if cnt == 0:
        print(0)
        break

    answer += 1
