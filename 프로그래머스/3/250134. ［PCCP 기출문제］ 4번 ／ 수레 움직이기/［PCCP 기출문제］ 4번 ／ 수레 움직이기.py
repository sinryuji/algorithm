import copy
from collections import deque


def check(r, c, visited, maze, n, m):
    if 0 <= r < n and 0 <= c < m and maze[r][c] != 5 and visited[r][c] == False:
        return True
    return False


def solution(maze):
    n, m = len(maze), len(maze[0])

    red, blue = [], []
    for r in range(n):
        for c in range(m):
            if maze[r][c] == 1:
                red = [r, c]
            if maze[r][c] == 2:
                blue = [r, c]

    di = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q = deque()
    q.append(red + blue + [[[False] * m for _ in range(n)]] + [[[False] * m for _ in range(n)]] + [0])

    while q:
        rr, rc, br, bc, rv_tmp, bv_tmp, cnt = q.popleft()

        rv = copy.deepcopy(rv_tmp)
        bv = copy.deepcopy(bv_tmp)
        rv[rr][rc] = True
        bv[br][bc] = True

        if maze[rr][rc] == 3 and maze[br][bc] == 4:
            return cnt

        for dr, dc in di:
            if maze[rr][rc] == 3:
                nbr, nbc = br + dr, bc + dc
                if check(nbr, nbc, bv, maze, n, m):
                    if not (nbr == rr and nbc == rc):
                        q.append([rr, rc, nbr, nbc, rv, bv, cnt + 1])
            elif maze[br][bc] == 4:
                nrr, nrc = rr + dr, rc + dc
                if check(nrr, nrc, rv, maze, n, m):
                    if not (nrr == br and nrc == bc):
                        q.append([nrr, nrc, br, bc, rv, bv, cnt + 1])
            else:
                nbr, nbc = br + dr, bc + dc
                if check(nbr, nbc, bv, maze, n, m):
                    for dr2, dc2 in di:
                        nrr, nrc = rr + dr2, rc + dc2
                        if check(nrr, nrc, rv, maze, n, m):
                            if not (nbr == nrr and nbc == nrc) and not (nrr == br and nrc == bc and nbr == rr and nbc == rc):
                                q.append([nrr, nrc, nbr, nbc, rv, bv, cnt + 1])

    return 0
