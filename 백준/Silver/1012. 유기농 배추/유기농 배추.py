import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    queue = [[a, b]]
    graph[b][a] == 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append([nx, ny])

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)