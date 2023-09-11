import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    heapq.heappush(heap, (start, 0))
    dist[start] = 0
    
    while heap:
        now, cost = heapq.heappop(heap)
        
        if dist[now] < cost:
            continue
                    
        for next_, next_cost in graph[now]:
            total_cost = cost + next_cost
            if total_cost < dist[next_]:
                dist[next_] = total_cost
                heapq.heappush(heap, (next_, total_cost))
                
    return dist[end]

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
heap = []
    
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

print(-1 if path1 >= INF or path2 >= INF else min(path1, path2))