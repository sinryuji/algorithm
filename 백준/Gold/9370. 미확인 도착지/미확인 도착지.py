import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    heap = []
    dist = [INF] * (n + 1)
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
                
    return dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    goals = [int(input()) for i in range(t)]
    save = []
    s_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    for i in goals:
        if (s_dist[g] + g_dist[h] + h_dist[i] == s_dist[i]) or (s_dist[h] + h_dist[g] + g_dist[i] == s_dist[i]):
            save.append(i)
    print(*sorted(save))
        
    