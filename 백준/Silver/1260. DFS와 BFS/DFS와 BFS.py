import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited_dfs.append(start)
    for i in sorted(lines[start]):
        if i not in visited_dfs:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_bfs.append(start)
    while queue:
        v = queue.popleft()
        for i in sorted(lines[v]):
            if i not in visited_bfs:
                queue.append(i)
                visited_bfs.append(i)
            
n, m, v = map(int, input().split())
vertices = [i for i in range(1, n + 1)]
lines = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
visited_dfs = []
visited_bfs = []

dfs(v)
bfs(v)

print(*visited_dfs)
print(*visited_bfs)