import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(r):
    global cnt
    visited[r] = cnt
    for i in sorted(lines[r], reverse = True):
        if visited[i] == 0:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split())
vertices = [i for i in range(1, (n + 1))]
lines = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
visited = [0] * (n + 1)
cnt = 1

dfs(r)

for i in range(1, n + 1):
    print(visited[i])