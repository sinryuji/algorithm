import sys

input = sys.stdin.readline


def dfs(cur, depth):
    if depth == 5:
        return True
    visited[cur] = True

    for nxt in graph[cur]:
        if not visited[nxt]:
            if dfs(nxt, depth + 1):
                return True
            visited[nxt] = False

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(N):
    visited = [False] * N
    if dfs(i, 1):
        ans = 1
        break

print(ans)