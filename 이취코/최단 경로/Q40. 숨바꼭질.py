import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


INF = int(1e9)
distance = [INF] * (N+1)

q = [(0, 1)]
distance[1] = 0
while q:
    dist, cur = heapq.heappop(q)

    if distance[cur] < dist:
        continue

    for nxt in graph[cur]:
        cost = dist + 1
        if cost < distance[nxt]:
            distance[nxt] = cost
            heapq.heappush(q, (cost, nxt))

max_dist = 0
for dist in distance:
    if dist != INF:
        max_dist = max(max_dist, dist)

answer = []
for i, dist in enumerate(distance):
    if dist == max_dist:
        answer.append(i)

print(min(answer), max_dist, len(answer))
