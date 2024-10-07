import sys, heapq

input = sys.stdin.readline

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

INF = int(1e9)
distances = [INF] * (N + 1)

def dijkstra(start):
    distances[start] = 0
    q = []
    heapq.heappush(q, (distances[start], start))

    while q:
        dist, cur_node = heapq.heappop(q)

        if distances[cur_node] < dist:
            continue

        for next_node, next_dist in graph[cur_node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                q.append((cost, next_node))

dijkstra(C)

cnt, max_dist = 0, 0
for i in range(1, N + 1):
    if distances[i] < INF:
        cnt += 1
        max_dist = max(max_dist, distances[i])

print(cnt - 1, max_dist)