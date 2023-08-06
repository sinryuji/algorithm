def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if map_[y][x] == 0:
        return False
    map_[y][x] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
    return True

n = int(input())
map_ = [list(map(int, list(input()))) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = []

for y in range(n):
    for x in range(n):
        cnt = 0
        if dfs(x, y) == True:
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer, sep = '\n')