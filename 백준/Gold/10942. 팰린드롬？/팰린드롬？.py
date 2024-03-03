import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
for cnt in range(N - 2):
    for i in range(N - 2 - cnt):
        j = i + 2 + cnt
        if nums[i] == nums[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])