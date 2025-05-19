import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, M + 1):
            if coin <= i:
                dp[i] += dp[i - coin]

    print(dp[M])
