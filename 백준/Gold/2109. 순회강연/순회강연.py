import sys, heapq

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

heap = []
for p, d in arr:
    heapq.heappush(heap, p)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))