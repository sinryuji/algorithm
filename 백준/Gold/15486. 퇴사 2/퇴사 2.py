import sys

input = sys.stdin.readline

N = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i-1])
    date = i + arr[i][0] - 1
    if date <= N:
        dp[date] = max(dp[date], dp[i-1] + arr[i][1])

print(max(dp))
