import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, f = int(input()), list(map(int, input().split()))
    prefix_sum = [0] * (k + 1)
    for i in range(k):
        prefix_sum[i + 1] = prefix_sum[i] + f[i]
        
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(2, k + 1):
        for j in range(1, k + 2 - i):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + (prefix_sum[j + i - 1] - prefix_sum[j - 1])

    print(dp[1][k])