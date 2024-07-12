import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(now):
    global visited
    visited[now] = 1
    for nxt in graph[now]:
        if visited[nxt] == -1:
            visited[now] += dfs(nxt)
    return visited[now]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [-1] * (N+1)

dfs(R)

for _ in range(Q):
    print(visited[int(input())])