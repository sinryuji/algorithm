import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[y][x] < board[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)

    return dp[y][x]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[0] * n for _ in range(n)]

answer = 0
for y in range(n):
    for x in range(n):
        answer = max(answer, dfs(x, y))

print(answer)
