import sys, copy

input = sys.stdin.readline
LOG = 17


def dfs(cur):
    for nxt, dist in graph[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        parents[nxt][0] = (cur, dist)
        dfs(nxt)


def search(idx, cur, left):
    if cur == 0:
        answer[idx] = cur + 1
        return
    for i in range(LOG - 1, -1, -1):
        p_node, p_dist = parents[cur][i]
        if left >= p_dist:
            search(idx, p_node, left - p_dist)
            return
    answer[idx] = cur + 1


N = int(input())
ants = [int(input()) for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

visited = [False] * N
visited[0] = True
parents = [[(0, 0) for _ in range(LOG)] for _ in range(N)]
answer = [0] * N

dfs(0)
for i in range(1, LOG):
    for node in range(N):
        p_node, p_dist = parents[node][i - 1]
        gp_node, gp_dist = parents[p_node][i - 1]
        parents[node][i] = (gp_node, p_dist + gp_dist)

for i in range(N):
    search(i, i, ants[i])
print(*answer, sep='\n')
