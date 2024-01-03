import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = int(input()), int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, target = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for next_ in graph[curr]:
            cost = dist + next_[1]
            if distance[next_[0]] > cost:
                distance[next_[0]] = cost
                heapq.heappush(q, [cost, next_[0]])

dijkstra(start)

print(distance[target])