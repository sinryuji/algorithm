n, k = map(int, input().split())
l = [[0, 0]]
for _ in range(n):
    l.append(list(map(int, input().split())))
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = l[i][0]
        v = l[i][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])