import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(queue):
    d = 0
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append([nx, ny, d + 1])
    return d

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            queue.append([x, y, 0])

answer = bfs(queue)
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            print(-1)
            exit()
print(answer)