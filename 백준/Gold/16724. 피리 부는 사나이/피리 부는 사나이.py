import sys

input = sys.stdin.readline

def dfs(x, y):
    visited[y][x] = True
    dx, dy = nexts[board[y][x]]
    nx, ny = x + dx, y + dy
    cycle.append((x, y))

    if visited[ny][nx]:
        if (nx, ny) in cycle:
            return True
        else:
            return False

    return dfs(nx, ny)


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
nexts = {
    'U': (0, -1),
    'D': (0, 1),
    'R': (1, 0),
    'L': (-1, 0)
}
answer = 0

for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            cycle = []
            if dfs(x, y):
                answer += 1

print(answer)