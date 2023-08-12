import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(queue, cnt):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append([nx, ny, nz])
                cnt -= 1
    if cnt > 0:
        return -1
    return graph[z][y][x] - 1               

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
cnt = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append([x, y, z])
            elif graph[z][y][x] == 0:
                cnt += 1

print(bfs(queue, cnt))