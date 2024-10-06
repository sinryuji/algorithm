import heapq
import sys
input = sys.stdin.readline
INf = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            cost += dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INf:
        print('INFINITY')
    else:
        print(distance[i])