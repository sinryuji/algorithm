# https://www.acmicpc.net/problem/14501

import sys

input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i + schedule[i][0] > N:
        continue
    dp[i] = schedule[i][1]
    for j in range(i):
        if j + schedule[j][0] <= i:
            dp[i] = max(dp[i], dp[j] + schedule[i][1])

print(max(dp))
