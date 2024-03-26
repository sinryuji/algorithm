import sys

input = sys.stdin.readline


def get_next(x, y):
    if board[y][x] == 'U':
        return (x, y - 1)
    elif board[y][x] == 'D':
        return (x, y + 1)
    elif board[y][x] == 'L':
        return (x - 1, y)
    else:
        return (x + 1, y)


def dfs(x, y):
    visited[y][x] = True
    nx, ny = get_next(x, y)
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
answer = 0

for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            cycle = []
            if dfs(x, y):
                answer += 1

print(answer)