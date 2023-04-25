import sys
input = sys.stdin.readline

def lis(data):
    n = len(data)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

d = dict()
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    d[x] = y
d = dict(sorted(d.items()))

print(len(d) - lis(list(d.values())))