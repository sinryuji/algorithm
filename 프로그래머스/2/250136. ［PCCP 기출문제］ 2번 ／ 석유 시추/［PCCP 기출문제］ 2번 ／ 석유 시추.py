from collections import deque

dic = {}

def bfs(land, r, c, x, y, n):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])
    land[y][x] = n
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < c and 0 <= ny < r and land[ny][nx] == 1:
                land[ny][nx] = n
                q.append((nx, ny))
                cnt += 1
    dic[n] = cnt

def solution(land):
    answer = 0
    d = {}
    n = 2
    r, c = len(land), len(land[0])
    
    for y in range(r):
        for x in range(c):
            if land[y][x] == 1:
                bfs(land, r, c, x, y, n)
                n += 1
                
    for x in range(c):
        s = set()
        for y in range(r):
            if land[y][x] > 1:
                s.add(land[y][x])
        answer = max(answer, sum(dic[i] for i in s))
    
    
    return answer