import sys

input = sys.stdin.readline


def dfs(cur, seen):
    if len(seen) == 5:
        return True

    for nxt in graph[cur]:
        if nxt not in seen:
            seen.append(nxt)
            if dfs(nxt, seen):
                return True
            seen.pop()

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(N):
    if dfs(i, [i]):
        ans = 1
        break

print(ans)