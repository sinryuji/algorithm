import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


def get_pos():
    rx, ry, bx, by = 0, 0, 0, 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                rx, ry = x, y
            if board[y][x] == 'B':
                bx, by = x, y
    return rx, ry, bx, by


def move(x, y, dx, dy):
    cnt = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs():
    rx, ry, bx, by = get_pos()

    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, res = q.popleft()

        if res > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if board[nby][nbx] == 'O':
                continue

            if board[nry][nrx] == 'O':
                print(res)
                return

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, res + 1))

    print(-1)

    
bfs()