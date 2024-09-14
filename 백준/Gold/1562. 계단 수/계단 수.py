N = int(input())
bit_range = 1 << 10
num_range = 10
mod = 1000000000
dp = [[[0] * bit_range for _ in range(num_range)] for _ in range(N + 1)]
for i in range(1, num_range):
    dp[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(num_range):
        for k in range(bit_range):
            if j > 0:
                nxt = k | 1 << (j - 1)
                dp[i + 1][j - 1][nxt] += dp[i][j][k]
                dp[i + 1][j - 1][nxt] %= mod
            if j < 9:
                nxt = k | 1 << (j + 1)
                dp[i + 1][j + 1][nxt] += dp[i][j][k]
                dp[i + 1][j + 1][nxt] %= mod

res = 0
for i in range(num_range):
    res += dp[N][i][bit_range - 1]
    res %= mod

print(res)