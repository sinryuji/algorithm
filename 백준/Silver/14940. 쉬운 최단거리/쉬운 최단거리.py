n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
target_x = 0
target_y = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            target_x = x
            target_y = y
        elif graph[y][x] == 1:
            graph[y][x] = -1
            
graph[target_y][target_x] = 0 
queue = [[target_x, target_y]]
while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[ny][nx] == -1:
            graph[ny][nx] = graph[y][x] + 1
            queue.append([nx, ny])
            
for i in range(n):
    print(*graph[i])