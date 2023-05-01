a = input()
b = input()
a_len = len(a)
b_len = len(b)
dp = [0] * max(a_len, b_len)

for i in range(a_len):
    n = 0
    for j in range(b_len):
        if n < dp[j]:
            n = dp[j]
        elif a[i] == b[j]:
            dp[j] = n + 1

print(max(dp))