import sys
input = sys.stdin.readline

def dfs(n):
    dfs_list.append(n)
    visited_dfs[n] = True
    for i in sorted(lines[n]):
        if not visited_dfs[i]:
            dfs(i)

def bfs(n):
    queue = [n]
    visited_bfs[n] = True
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for i in sorted(lines[v]):
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
            
n, m, v = map(int, input().split())
vertices = [i for i in range(1, n + 1)]
lines = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs_list = []
bfs_list = []

dfs(v)
bfs(v)

print(*dfs_list)
print(*bfs_list)