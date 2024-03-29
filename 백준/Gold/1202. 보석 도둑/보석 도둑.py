import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = dict()

for _ in range(N):
    m, v = map(int, input().split())
    if m in jewels:
        jewels[m].append(v)
    else:
        jewels[m] = [v]

jewel_weights = sorted(jewels.keys(), reverse=True)
bags = sorted([int(input()) for _ in range(K)])

heap = []
answer = 0
for bag in bags:
    while jewel_weights and jewel_weights[-1] <= bag:
        weight = jewel_weights.pop()
        for values in jewels[weight]:
            heapq.heappush(heap, -values)
    if heap:
        answer -= heapq.heappop(heap)

print(answer)