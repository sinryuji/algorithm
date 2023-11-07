from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
normal_visited = [[False] * N for _ in range(N)]
blindness_visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, flag):
    target = graph[y][x]
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if flag == False:
                if graph[ny][nx] != target:
                    continue
                elif normal_visited[ny][nx] == False:
                    normal_visited[ny][nx] = True
                    queue.append([nx, ny])
            if flag == True:
                if target == 'R' and graph[ny][nx] == 'B':
                    continue
                if target == 'G' and graph[ny][nx] == 'B':
                    continue
                if target == 'B' and graph[ny][nx] != target:
                    continue
                elif blindness_visited[ny][nx] == False:
                    blindness_visited[ny][nx] = True
                    queue.append([nx, ny])

normal = 0
blindness = 0
for y in range(N):
    for x in range(N):
        if normal_visited[y][x] == False:
            bfs(x, y, False)
            normal += 1
for y in range(N):
    for x in range(N):
        if blindness_visited[y][x] == False:
            bfs(x, y, True)
            blindness += 1

print(normal, blindness)