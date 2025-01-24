def solution(park, routes):
    n, m = len(park), len(park[0])
    r = c = 0
    for row in range(n):
        for col in range(m):
            if park[row][col] == 'S':
                r, c = row, col
    
    d = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    for route in routes:
        di, v = route.split()
        dr, dc = d[di]
        v = int(v)
        nr, nc = r, c
        while v > 0 and 0 <= (nr + dr) < n and 0 <= (nc + dc) < m and park[nr+dr][nc+dc] != 'X':
            v -= 1
            nr += dr
            nc += dc
        if v == 0:
            r, c = nr, nc  
    
    return [r, c]