import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: dist[i][j] = 0

for a in range(n):
    for b, c in graph[a]:
        dist[a][b] = min(dist[a][b], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF: dist[i][j] = 0

for i in dist:
    print(*i)