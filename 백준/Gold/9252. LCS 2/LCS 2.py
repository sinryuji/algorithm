a = input()
b = input()
a_len = len(a)
b_len = len(b)
dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for r in range(1, a_len + 1):
    for c in range(1, b_len + 1):
        if a[r - 1] == b[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

answer = []
r, c = a_len, b_len

while len(answer) != dp[-1][-1]:
    if dp[r][c] == dp[r - 1][c]:
        r -= 1
        continue
    elif dp[r][c] == dp[r][c - 1]:
        c -= 1
        continue
    else:
        r -= 1
        c -= 1
        answer.append(a[r])

print(dp[-1][-1])
print(''.join(answer[::-1]))