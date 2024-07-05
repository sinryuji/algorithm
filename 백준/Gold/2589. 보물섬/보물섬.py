import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    m = 0
    while q:
        x, y, h = q.popleft()
        # visited[y][x] = True
        m = max(m, h)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 'L' and not visited[ny][nx]:
                q.append((nx, ny, h + 1))
                visited[ny][nx] = True
    return m

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
processed = [[False] * M for _ in range(N)]

ans = 0
stop = False
for y in range(N):
    # if stop:
    #     break
    for x in range(M):
        if not processed[y][x] and board[y][x] == 'L':
            ans = max(ans, bfs(x, y))
            processed[y][x] = True
            # if ans == N + M - 2:
            #     stop = True
            #     break

print(ans)