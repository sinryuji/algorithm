import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    heap = [(distance[start], start)]
    visited = set()
    while heap:
        dist, curr = heapq.heappop(heap)
        if curr in visited:
            continue
        if curr == end:
            break
        visited.add(curr)
        for n, n_dist in graph[curr]:
            if distance[n] > dist + n_dist:
                distance[n] = dist + n_dist
                prev_node[n] = curr
                heapq.heappush(heap, (distance[n], n))

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [INF] * (n + 1)
distance[start] = 0
prev_node = [0] * (n + 1)
path = [end]

dijkstra(start, end)
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(distance[end])
print(len(path))
print(*path)