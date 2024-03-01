import sys
input = sys.stdin.readline


def check_row(r, c, num):
    for x in range(9):
        if c != x and num == sdoku[r][x]:
            return False
    return True


def check_col(r, c, num):
    for x in range(9):
        if r != x and num == sdoku[x][c]:
            return False
    return True


def check_three(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if r != nr + x and c != nc + y and num == sdoku[nr + x][nc + y]:
                return False
    return True


def dfs(depth, r, c, num):
    if depth > 0:
        if not check_row(r, c, num):
            return
        if not check_col(r, c, num):
            return
        if not check_three(r, c, num):
            return

    if depth >= len(zero_p):
        for i in range(9):
            print(''.join(map(str, sdoku[i])))
        exit()

    nr, nc = zero_p[depth]
    for i in range(1, 10):
        sdoku[nr][nc] = i
        dfs(depth + 1, nr, nc, i)
        sdoku[nr][nc] = 0


sdoku = []
zero_p = []
for i in range(9):
    temp = list(map(int, input().rstrip()))
    for j in range(9):
        if temp[j] == 0:
            zero_p.append((i, j))
    sdoku.append(temp)

dfs(0, 0, 0, 0)