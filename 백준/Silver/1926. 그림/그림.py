import sys
from collections import deque

input = sys.stdin.readline

def bfs(r, c):
    graph[r][c] = 2
    q = deque([(r, c)])
    
    area = 1
    while q:
        r, c = q.popleft()
        
        for dr, dc in di:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                graph[nr][nc] = 2
                area += 1
                q.append((nr, nc))
                
    return area
            
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0
max_ = 0
for r in range(n):
    for c in range(m):
        if graph[r][c] == 1:
            cnt += 1
            max_ = max(max_, bfs(r, c))
            
print(cnt)
print(max_)