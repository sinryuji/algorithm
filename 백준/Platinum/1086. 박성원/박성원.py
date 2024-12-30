import sys, math

input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
K = int(input())

remain = [[(j * 10 ** len(str(S[i])) + S[i]) % K for j in range(K)] for i in range(N)]

dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for mask in range(1 << N):
    for i in range(N):
        if mask & (1 << i):
            continue
        for j in range(K):
            dp[mask | (1 << i)][remain[i][j]] += dp[mask][j]

correct = dp[(1 << N) - 1][0]
total = sum(dp[(1 << N) - 1])
g = math.gcd(total, correct)
print(f'{correct // g}/{total // g}')
