def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 1:
                queue.append([nx, ny])
                graph[ny][nx] = graph[y][x] + 1


n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

bfs(0, 0)
print(graph[n - 1][m - 1])