import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
dist1 = [INF] * (N + 1)
dist2 = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph1[a].append((b, c))
    graph2[b].append((a, c))

heap = [(X, 0)]
dist1[X] = 0
while heap:
    curr, dist = heapq.heappop(heap)
    if dist1[curr] < dist:
        continue
    for n, n_dist in graph1[curr]:
        if dist1[n] > dist + n_dist:
            dist1[n] = dist + n_dist
            heapq.heappush(heap, (n, dist1[n]))

heap = [(X, 0)]
dist2[X] = 0
while heap:
    curr, dist = heapq.heappop(heap)
    if dist2[curr] < dist:
        continue
    for n, n_dist in graph2[curr]:
        if dist2[n] > dist + n_dist:
            dist2[n] = dist + n_dist
            heapq.heappush(heap, (n, dist2[n]))

print(max(dist1[i] + dist2[i] for i in range(1, N + 1)))