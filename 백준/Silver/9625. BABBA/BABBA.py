n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]

if n == 1:
    print(0, 1)
else:
    dp[0][0], dp[0][1] = 0, 0
    dp[1][0], dp[1][1] = 0, 1
    dp[2][0], dp[2][1] = 1, 1

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    print(dp[n][0], dp[n][1])