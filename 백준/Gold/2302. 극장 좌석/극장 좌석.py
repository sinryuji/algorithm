import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
vips = set(int(input()) for _ in range(M))

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    if i in vips or i - 1 in vips:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])