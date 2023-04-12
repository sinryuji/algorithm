import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * n
if n <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[1] + s[2], s[0] + s[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    print(dp[n - 1])