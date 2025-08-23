import sys
from heapq import heappop, heapify, heappush

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    heap = list(map(int, input().split()))
    heapify(heap)
    
    ans = 0
    while len(heap) > 1:
        a, b = heappop(heap), heappop(heap)
        ans += a + b
        heappush(heap, a + b)
        
    print(ans)