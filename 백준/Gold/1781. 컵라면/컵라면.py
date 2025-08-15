import sys, heapq

input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

heap = []
for a, b in arr:
    heapq.heappush(heap, b)
    if len(heap) > a:
        heapq.heappop(heap)
        
print(sum(heap))