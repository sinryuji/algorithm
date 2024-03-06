import sys

input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e6)
ans = INF

for i in range(3):
    dp = [[1000] * 3 for _ in range(N)]
    dp[0][i] = rgb[0][i]
    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    dp[N - 1][i] = INF
    ans = min(ans, min(dp[N - 1]))

print(ans)