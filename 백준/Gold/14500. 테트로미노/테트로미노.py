N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
max_ = max(map(max, graph))
answer = 0

def dfs(x, y, cnt, sum_):
    global answer

    if answer > sum_ + max_ * (4 - cnt):
        return
    if cnt == 4:
        answer = max(answer, sum_)
        return

    for dx, dy in d:
        nx = dx + x
        ny = dy + y
        if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[ny][nx] == 0:
            continue
        t = graph[ny][nx]
        if cnt == 2:
            graph[ny][nx] = 0
            dfs(x, y, cnt + 1, sum_ + t)
            graph[ny][nx] = t
        graph[ny][nx] = 0
        dfs(nx, ny, cnt + 1, sum_ + t)
        graph[ny][nx] = t

for x in range(M):
    for y in range(N):
        t = graph[y][x]
        graph[y][x] = 0
        dfs(x, y, 1, t)
        graph[y][x] = t

print(answer)