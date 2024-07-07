num = input()
dp = [0] * len(num)
dp[0] = 1

if len(num) >= 2:
    if num[1] != '0' and num[0] + num[1] <= '34':
        dp[1] = 2
    else:
        dp[1] = 1

if len(num) >= 3:
    for i in range(2, len(num)):
        if num[i - 1] != '0' and num[i] != '0' and num[i - 1] + num[i] <= '34':
            dp[i] = dp[i - 1] + dp[i - 2]
        elif num[i] != '0':
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 2]

print(dp[len(num) - 1])