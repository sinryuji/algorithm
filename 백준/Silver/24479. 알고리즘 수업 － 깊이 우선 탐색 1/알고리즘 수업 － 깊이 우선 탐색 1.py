import sys
input = sys.stdin.readline

def dfs(start):
    cnt = 1
    stack = [start]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = cnt
            cnt += 1
            for i in sorted(graph[v], reverse = True):
                stack.append(i)

n, m, r = map(int, input().split())
vertices = [i for i in range(1, n + 1)]
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])