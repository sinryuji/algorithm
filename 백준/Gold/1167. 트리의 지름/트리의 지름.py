import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v, s):
    for n, d in graph[v]:
        if dist[n] == -1:
            dist[n] = s + d
            dfs(n, s + d)

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    edge = list(map(int, input().split()))
    for i in range(1, len(edge) - 1, 2):
        graph[edge[0]].append((edge[i], edge[i + 1]))

dist = [-1] * (V + 1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1] * (V + 1)
dist[start] = 0
dfs(start, 0)

print(max(dist))