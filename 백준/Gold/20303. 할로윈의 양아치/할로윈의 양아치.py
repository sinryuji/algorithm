import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    visited[x] = True
    cnt = 1
    s = candies[x]
    while q:
        cur = q.popleft()
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                cnt += 1
                s += candies[n]
    return (cnt, s)


N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

group = []
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        group.append(bfs(i))

dp = [0] * (K + 1)
for cnt, s in group:
    for i in range(K - 1, 0, -1):
        if i >= cnt:
            dp[i] = max(dp[i], dp[i - cnt] + s)

print(max(dp))