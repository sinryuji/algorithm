import sys
import heapq

input = sys.stdin.readline

n = int(input())
locations = []
for _ in range(n):
    h, o = map(int, input().split())
    locations.append((min(h, o), max(h, o)))
d = int(input())

locations.sort(key=lambda x: (x[1], x[0]))

heap = []
answer = 0
for location in locations:
    start, end = location
    heapq.heappush(heap, start)
    line_start = end - d
    while heap and heap[0] < line_start:
        heapq.heappop(heap)
    answer = max(answer, len(heap))
    
print(answer)