import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    res = [start]
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        for n in graph[cur]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                res.append(n)

    return res


def floyd_warshall(commit, size):
    INF = 1e9
    dist = [[INF] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i == j:
                dist[i][j] = 0

    for i in range(size):
        for n in graph[commit[i]]:
            dist[i][commit.index(n)] = 1

    for k in range(size):
        for i in range(size):
            for j in range(size):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_ = INF
    res = 0
    for i in range(size):
        max_ = max(dist[i])
        if max_ < min_:
            min_ = max_
            res = commit[i]

    return res


N, M = int(input()), int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

committee = []

l = deque(list(range(1, N + 1)))
while l:
    res = bfs(l[0])
    for n in res:
        l.remove(n)
    committee.append(res)

leaders = []
for commit in committee:
    leaders.append(floyd_warshall(commit, len(commit)))

print(len(committee))
print(*sorted(leaders), sep="\n")