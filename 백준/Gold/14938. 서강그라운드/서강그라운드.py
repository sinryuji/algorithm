import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    global n
    global m

    distance = [INF] * n
    distance[start] = 0
    queue = []
    queue.append((start, distance[start]))

    while queue:
        current, dist = heapq.heappop(queue)
        if distance[current] < dist:
            continue
        for next_, next_dist in graph[current]:
            cost = dist + next_dist
            if distance[next_] > cost:
                distance[next_] = cost
                heapq.heappush(queue, (next_, cost))

    result = 0
    for i in range(n):
        if distance[i] <= m:
            result += items[i]

    return result

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1].append((b-1, l))
    graph[b-1].append((a-1, l))

answer = 0
for i in range(n):
    answer = max(answer, dijkstra(i))

print(answer)