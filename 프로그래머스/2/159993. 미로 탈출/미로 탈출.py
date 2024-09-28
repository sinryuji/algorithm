from collections import deque

def solution(maps):
    def bfs(x, y):
        nonlocal n, m
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        visited = [[False] * m for _ in range(n)]
        visited[y][x] = True
        
        q = deque([(x, y, 0)])
        flag = False
        while q:
            x, y, cnt = q.popleft()
            if maps[y][x] == 'E' and flag:
                return cnt
            if maps[y][x] == 'L':
                visited = [[False] * m for _ in range(n)]
                visited[y][x] = True
                q.clear()
                flag = True
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny, cnt + 1))
        
        return -1
        
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                return bfs(j, i)