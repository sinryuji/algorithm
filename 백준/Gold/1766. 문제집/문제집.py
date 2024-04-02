import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

heap = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

answer = []

while heap:
    cur = heapq.heappop(heap)
    answer.append(cur)
    for n in graph[cur]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heapq.heappush(heap, n)

print(*answer)