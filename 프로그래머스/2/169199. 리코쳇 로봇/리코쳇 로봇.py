from collections import deque

def solution(board):
    def bfs(x, y):
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(x, y, 0)])
        visited = [[False] * col for _ in range(row)]
        visited[y][x] = True

        while q:
            x, y, cnt = q.popleft()
            if board[y][x] == 'G':
                return cnt
            for dx, dy in d:
                nx = x
                ny = y
                while 0 <= nx < col and 0 <= ny < row and board[ny][nx] != 'D':
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if (nx != x or ny != y) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny, cnt + 1))

        return -1

    row = len(board)
    col = len(board[0])
    for y in range(row):
        for x in range(col):
            if board[y][x] == 'R':
                return bfs(x, y)