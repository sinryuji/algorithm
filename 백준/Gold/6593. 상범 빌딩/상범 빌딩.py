import sys
from collections import deque

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    graph = []
    for _ in range(L):
        graph.append([list(input().rstrip()) for _ in range(R)])
        input()

    start = []
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if graph[l][r][c] == 'S':
                    start = [l, r, c]
                    visited[l][r][c] = True

    d = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = deque([(*start, 0)])
    ret = 0
    while q:
        l, r, c, m = q.popleft()

        if graph[l][r][c] == 'E':
            ret = m
            break

        for dl, dr, dc in d:
            nl, nr, nc = l + dl, r + dr, c + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and graph[nl][nr][nc] != '#' and not visited[nl][nr][nc]:
                visited[nl][nr][nc] = True
                q.append((nl, nr, nc, m + 1))

    if ret == 0:
        print('Trapped!')
    else:
        print(f'Escaped in {ret} minute(s).')
