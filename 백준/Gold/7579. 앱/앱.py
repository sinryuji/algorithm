import sys
input = sys.stdin.readline

n, m = map(int, input().split())
apps = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
s = sum(costs)
dp = [[0] * (s + 1) for _ in range(n + 1)]
answer = s

for i in range(1, n + 1):
    byte = apps[i]
    cost = costs[i]
            
    for j in range(1, s + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], byte + dp[i - 1][j - cost])
        if dp[i][j] >= m:
            answer = min(answer, j)

if m != 0:
    print(answer)
else:
    print(answer)