import sys

input = sys.stdin.readline

N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i + consulting[i][0] <= N:
        dp[i] = consulting[i][1]
        for j in range(i):
            if j + consulting[j][0] <= i:
                dp[i] = max(dp[i], consulting[i][1] + dp[j])

print(max(dp))