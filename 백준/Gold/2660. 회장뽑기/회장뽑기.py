import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque([(start, 0)])

    visited = [False] * (N + 1)
    visited[start] = True

    max_depth = 0
    while q:
        cur, depth = q.popleft()
        max_depth = max(max_depth, depth)

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, depth + 1))

    return max_depth

N = int(input())
graph = [[] for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

min_score = sys.maxsize
candidates = []
for i in range(1, N + 1):
    score = bfs(i)
    if score == min_score:
        candidates.append(i)
    elif score < min_score:
        min_score = score
        candidates = [i]

print(min_score, len(candidates))
print(*sorted(candidates))