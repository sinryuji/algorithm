import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 and m > ny >= 0 and map[y][x] > map[ny][nx]:
            ways += dfs(nx, ny)
    dp[y][x] = ways
    
    return dp[y][x]

m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

print(dfs(0, 0))