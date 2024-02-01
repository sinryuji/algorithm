import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        wei, now = heapq.heappop(heap)
        if visited[now]:
            continue
        visited[now] = True
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
heap = []
distance = [INF] * (v + 1)
visited = [False] * (v + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dijkstra(k)

for i in range(1, v + 1):
    print("INF" if distance[i] == INF else distance[i])