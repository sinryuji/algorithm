import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))
    dp = [[] for _ in range(m)]
    for i in range(len(gold)):
        dp[i % m].append(gold[i])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if j == n - 1:
                left_down = 0
            else:
                left_down = dp[i - 1][j + 1]
            left = dp[i - 1][j]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)


    print(max(dp[-1]))
