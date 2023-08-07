import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[y][x] == 0:
        return False
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
    return True

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if dfs(x, y) == True:
                cnt += 1
    print(cnt)