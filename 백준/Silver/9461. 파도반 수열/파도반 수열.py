import sys
input = sys.stdin.readline

dp = [0] * (101)
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n - 1])