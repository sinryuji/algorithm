import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    indegree[q] += 1

dp = [0] * (N + 1)
prev = [0] * (N + 1)
q = deque([1])

while q:
    now = q.popleft()
    for n, c in graph[now]:
        indegree[n] -= 1
        s = dp[now] + c
        if s > dp[n]:
            dp[n] = s
            prev[n] = now
        if indegree[n] == 0 and n != 1:
            q.append(n)

now, answer = prev[1], [1]
while now != 1:
    answer.append(now)
    now = prev[now]
answer.append(1)

print(dp[1])
print(*answer[::-1])