import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    cnt = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if visited[v] == 0:
            visited[v] = cnt
            cnt += 1
            for i in sorted(graph[v], reverse = True):
                queue.append(i)

n, m, r = map(int, input().split())
vertices = [i for i in range(1, n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)

bfs(r)

for i in range(1, n + 1):
    print(visited[i])