S = input()
N = len(S)

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for l in range(1, N):
    for i in range(N - l):
        j = i + l
        dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
        if S[i] == S[j]:
            dp[i][j] += dp[i + 1][j - 1] + 1

print(dp[0][N-1])
