import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 0
q = []
for a, b in arr:
    heappush(q, b)
    while q and q[0] <= a:
        heappop(q)
    ans = max(ans, len(q))

print(ans)