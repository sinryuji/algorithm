import sys

input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

ans = 0
l, r = 1, max(budget)

while l <= r:
    m = (l + r) // 2
    total = 0
    for v in budget:
        if m < v:
            total += m
        else:
            total += v
    if total <= M:
        ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)