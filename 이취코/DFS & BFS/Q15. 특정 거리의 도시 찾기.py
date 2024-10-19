import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [False] * (N + 1)
visited[X] = True

answer = []
q = deque([(X, 0)])
while q:
    cur, dist = q.popleft()
    if dist == K:
        answer.append(cur)
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dist + 1))

if len(answer) == 0:
    print(-1)
else:
    print(*sorted(answer), sep='\n')
