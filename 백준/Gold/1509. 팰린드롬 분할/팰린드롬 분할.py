S = input()
L = len(S)

is_palindrome = [[0] * L for _ in range(L)]
dp = [2500] * (L + 1)
dp[-1] = 0
for e in range(L):
    for s in range(e + 1):
        if S[s] == S[e] and (e - s < 2 or is_palindrome[s + 1][e - 1]):
            is_palindrome[s][e] = 1
            dp[e] = min(dp[e], dp[s - 1] + 1)

print(dp[L - 1])