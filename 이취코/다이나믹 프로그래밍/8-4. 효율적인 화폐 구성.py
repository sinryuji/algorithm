n, m = map(int, input().split())
moneys = []
for _ in range(n):
    moneys.append(int(input()))

dp = [10001] * (m + 1)
dp[0] = 0
for i in moneys:
   for j in range(i, m + 1):
       dp[j] = min(dp[j], dp[j - i] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
