import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    cnt = 1
    visited[start] = cnt
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt

n, m, r = map(int, input().split())
verticies = [i for i in range(1, n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)

bfs(r)

for i in range(1, n + 1):
    print(visited[i])