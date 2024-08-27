import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([(a, 0)])
visited = [False] * (N + 1)
visited[a] = True
ans = -1
while q:
    cur, dist = q.popleft()
    if cur == b:
        ans = dist
        break
    for n in graph[cur]:
        if not visited[n]:
            q.append((n, dist + 1))
            visited[n] = True

print(ans)