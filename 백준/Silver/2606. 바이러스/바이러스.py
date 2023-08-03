import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = True
    for i in lines[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)

n, m = int(input()), int(input())
lines = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
visited = [False] * (n + 1)
cnt = 0

dfs(1)

print(cnt)