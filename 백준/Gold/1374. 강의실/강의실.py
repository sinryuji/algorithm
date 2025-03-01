import sys, heapq

input = sys.stdin.readline

N = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1]))

heap = []
answer = 0
for a, b, c in lectures:
    if len(heap) != 0 and heap[0] <= b:
        heapq.heappop(heap)
    heapq.heappush(heap, c)
    answer = max(answer, len(heap))

print(answer)
