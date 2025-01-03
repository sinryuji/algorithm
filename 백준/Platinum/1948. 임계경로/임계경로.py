import sys
from collections import deque

input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
path = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[b] += 1

start, end = map(int, input().split())
q = deque([start])

while q:
    cur = q.popleft()
    for nxt, nxt_dist in graph[cur]:
        indegree[nxt] -= 1
        cost = distance[cur] + nxt_dist
        if distance[nxt] < cost:
            distance[nxt] = cost
            path[nxt] = [cur]
        if distance[nxt] == cost:
            path[nxt].append(cur)

        if indegree[nxt] == 0:
            q.append(nxt)

q = deque([end])
route = set()
while q:
    cur = q.popleft()
    for x in path[cur]:
        if (cur, x) not in route:
            route.add((cur, x))
            q.append(x)

print(distance[end])
print(len(route))
