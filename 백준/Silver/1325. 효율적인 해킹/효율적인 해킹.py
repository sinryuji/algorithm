import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited = [False] * N
    visited[start] = True
    result = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                result += 1
    return result


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b - 1].append(a - 1)

cnt = [0] * N
for i in range(N):
    cnt[i] = bfs(i)

max_cnt = max(cnt)
answer = []
for i in range(N):
    if max_cnt == cnt[i]:
        answer.append(i+1)

print(*answer)
