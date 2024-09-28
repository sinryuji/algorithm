import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

answer = 0

for y in range(n):
    for x in range(m):
        if x == 0 or y == 0:
            dp[y][x] = arr[y][x]
        elif arr[y][x] == 1:
            dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1
        answer = max(answer, dp[y][x])

print(answer ** 2)