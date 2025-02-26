import sys, heapq

input = sys.stdin.readline

N = int(input())
classes = sorted([tuple(map(int, input().split())) for _ in range(N)])

heap = []
answer = 0
for s, t in classes:
    if len(heap) > 0 and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)
    answer = max(answer, len(heap))

print(answer)
