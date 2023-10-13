n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    min_val = 1e9
    for j in range(1, int(i ** 0.5) + 1):
        min_val = min(min_val, dp[i - j ** 2])
    dp.append(min_val + 1)

print(dp[n])