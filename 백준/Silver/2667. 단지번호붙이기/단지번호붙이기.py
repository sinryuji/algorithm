def bfs(a, b):
    cnt = 1
    queue = [[a, b]]
    map_[b][a] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if map_[ny][nx] == 1:
                map_[ny][nx] = 0
                queue.append([nx, ny])
                cnt += 1
    return cnt
                

n = int(input())
map_ = [list(map(int, list(input()))) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = []

for y in range(n):
    for x in range(n):
        if map_[y][x] == 1:
            answer.append(bfs(x, y))

answer.sort()
print(len(answer))
print(*answer, sep = '\n')