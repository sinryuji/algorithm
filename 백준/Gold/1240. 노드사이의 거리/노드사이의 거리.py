import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        cur, dist = q.popleft()
        if cur == end:
            return dist
        for n, n_dist in graph[cur]:
            if not visited[n]:
                visited[n] = True
                q.append((n, dist + n_dist))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

for _ in range(M):
    start, end = map(int, input().split())
    print(bfs(start, end))