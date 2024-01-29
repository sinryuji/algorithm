import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    global N
    distance = [INF] * (N + 1)
    distance[start] = 0
    queue = [(start, distance[start])]

    while queue:
        curr, dist = heapq.heappop(queue)
        if distance[curr] < dist:
            continue
        for n, n_dist in graph[curr]:
            cost = dist + n_dist
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(queue, (n, cost))

    return distance

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dists = [[]]

for i in range(1, N + 1):
    dists.append(dijkstra(i))

answer = 0

for i in range(1, N + 1):
    answer = max(answer, dists[i][X] + dists[X][i])

print(answer)