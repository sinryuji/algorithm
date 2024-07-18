n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [100001] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(1, k + 1):
        if j - coins[i] >= 0:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])