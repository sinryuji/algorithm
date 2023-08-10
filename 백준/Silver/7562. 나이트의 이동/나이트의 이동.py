import sys
input = sys.stdin.readline

def bfs(x1, y1, x2, y2):
    queue = [[x1, y1]]
    while queue:
        x, y = queue.pop(0)
        if x == x2 and y == y2:
            return graph[y][x]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[ny][nx] == 0:
                queue.append([nx, ny])
                graph[ny][nx] = graph[y][x] + 1
    return 0

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(input())):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    print(bfs(x1, y1, x2, y2))