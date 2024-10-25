import sys
from collections import deque

input = sys.stdin.readline


def move(countries):
    total = sum(board[y][x] for x, y in countries)
    val = total // len(countries)

    for x, y in countries:
        board[y][x] = val


def bfs(x, y):
    global N, L, R
    q = deque([(x, y)])
    visited[y][x] = True
    result = [(x, y)]

    while q:
        x, y = q.popleft()

        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and L <= abs(board[ny][nx] - board[y][x]) <= R:
                visited[ny][nx] = True
                q.append((nx, ny))
                result.append((nx, ny))

    return result


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                result = bfs(x, y)
                if len(result) > 1:
                    flag = True
                    move(result)

    if not flag:
        break

    answer += 1

print(answer)
