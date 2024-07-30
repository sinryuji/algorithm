N = int(input())
# dp = [0] * (N + 1)

if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    # dp[1] = 3
    # dp[2] = 7
    pprev = 3
    prev = 7
    cur = 0

    for i in range(3, N + 1):
        cur = prev + prev + pprev
        pprev = prev
        prev = cur

    print(cur % 9901)