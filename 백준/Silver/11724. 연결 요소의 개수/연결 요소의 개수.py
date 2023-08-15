import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        for i in lines[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
            

n, m = map(int, input().split())
lines = [set() for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].add(b)
    lines[b].add(a)

cnt = 0
for i in range(1, n + 1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
            
print(cnt)