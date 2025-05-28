import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
INF = int(1e9)
distance = [INF] * (N + 1)
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))
while q:
    dist, cur = heapq.heappop(q)
    
    if distance[cur] < dist:
        continue
        
    for nxt in graph[cur]:
        cost = dist + nxt[1]
        if distance[nxt[0]] > cost:
            distance[nxt[0]] = cost
            heapq.heappush(q, (cost, nxt[0]))
            
print(distance[N])        