import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    way = 0
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and board[ny][nx] < board[y][x]:
            way += dfs(nx, ny)
    dp[y][x] = way

    return dp[y][x]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(dfs(0, 0))
