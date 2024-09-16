import sys

input = sys.stdin.readline


def dfs(x, cnt):
    global ans
    if ans >= cnt + L - x:
        return
    if x == L:
        ans = max(ans, cnt)
        return

    for i, j in bishop[x]:
        if not visited[i - j]:
            visited[i - j] = True
            dfs(x + 1, cnt + 1)
            visited[i - j] = False

    dfs(x + 1, cnt)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

L = 2 * n - 1
bishop = [[] for _ in range(L)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bishop[i + j].append((i, j))

visited = [False] * L
ans = 0
dfs(0, 0)

print(ans)