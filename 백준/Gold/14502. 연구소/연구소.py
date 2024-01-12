from collections import deque
import copy

def bfs():
    global result
    queue = deque()
    tmp = copy.deepcopy(graph)

    for y in range(N):
        for x in range(M):
            if tmp[y][x] == 2:
                queue.append([x, y])           

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= M or ny >= N or nx < 0 or ny < 0:
                continue
            if tmp[ny][nx] == 1 or tmp[ny][nx] == 2:
                continue
            tmp[ny][nx] = 2
            queue.append([nx, ny])

    count = 0
    for y in range(N):
        for x in range(M):
            if tmp[y][x] == 0:
                count += 1
    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                graph[y][x] = 1
                make_wall(count+1)
                graph[y][x] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

make_wall(0)

print(result)