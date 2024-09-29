import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    global M, N

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])
    board[y][x] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:
                board[ny][nx] = 1
                cnt += 1
                q.append((nx, ny))

    return cnt


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] += 1

answer = 0
count = []

for y in range(M):
    for x in range(N):
        if board[y][x] == 0:
            count.append(bfs(x, y))
            answer += 1


print(answer)
print(*sorted(count), sep = ' ')