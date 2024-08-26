import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, h):
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not b[nx][ny] and a[nx][ny] > h:
            b[nx][ny] = True
            dfs(nx, ny, h)


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ans = 0
for k in range(max(map(max, a))):
    b = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] > k and not b[i][j]:
                cnt += 1
                b[i][j] = True
                dfs(i, j, k)
    ans = max(ans, cnt)

print(ans)