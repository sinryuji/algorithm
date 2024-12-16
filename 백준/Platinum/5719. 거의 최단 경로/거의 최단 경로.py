import sys
import heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    distance = [INF] * N
    distance[S] = 0

    q = []
    heapq.heappush(q, (S, 0))

    while q:
        cur, dist = heapq.heappop(q)

        if distance[cur] < dist:
            continue

        for nxt, nxt_dist in graph[cur]:
            if edges[cur][nxt]:
                continue
            cost = dist + nxt_dist
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (nxt, cost))

    return distance


def bfs():
    q = deque()
    q.append(D)

    while q:
        cur = q.popleft()

        if cur == S:
            continue

        for post, post_dist in graph_reverse[cur]:
            if distance[post] + post_dist == distance[cur] and not edges[post][cur]:
                edges[post][cur] = True
                q.append(post)


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    graph_reverse = [[] for _ in range(N)]
    edges = [[False] * N for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((V, P))
        graph_reverse[V].append((U, P))

    distance = dijkstra()
    bfs()
    distance = dijkstra()
    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])
