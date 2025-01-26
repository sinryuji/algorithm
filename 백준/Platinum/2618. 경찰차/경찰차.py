import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def calc(m, n):
    return abs(li[m][0] - li[n][0]) + abs(li[m][1] - li[n][1])


def solve(m, n):
    nxt = max(m, n) + 1
    if nxt == W + 2:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    calc1 = solve(nxt, n) + calc(m, nxt)
    calc2 = solve(m, nxt) + calc(n, nxt)
    if calc1 < calc2:
        dp_trace[m][n] = 1
        dp[m][n] = calc1
    else:
        dp_trace[m][n] = 2
        dp[m][n] = calc2

    return dp[m][n]


N = int(input())
W = int(input())
li = [[1, 1], [N, N]]
for _ in range(W):
    li.append(list(map(int, input().split())))

dp = [[-1] * 1002 for _ in range(1002)]
dp_trace = [[-1] * 1002 for _ in range(1002)]

print(solve(0, 1))

m, n = 0, 1
for i in range(2, W + 2):
    print(dp_trace[m][n])
    if dp_trace[m][n] == 1:
        m = i
    else:
        n = i
