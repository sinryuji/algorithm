from collections import deque

def solution(maps):
    
    def bfs(x, y):
        nonlocal n, m
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        s = int(maps[y][x])
        maps[y][x] = 'X'
        
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx].isdigit():
                    s += int(maps[ny][nx])
                    maps[ny][nx] = 'X'
                    q.append((nx, ny))
                    
        return s
        
    answer = []
    
    n, m = len(maps), len(maps[0])
    maps = [list(maps[i]) for i in range(n)]

    for y in range(n):
        for x in range(m):
            if maps[y][x].isdigit():
                answer.append(bfs(x, y))
    
    answer.sort()
    return answer if len(answer) > 0 else [-1]