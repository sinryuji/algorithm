import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = sorted([list(map(int, input().split())) for _ in range(N)])
bags = sorted([int(input()) for _ in range(K)])

answer = 0
tmp = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        answer -= heapq.heappop(tmp)

print(answer)