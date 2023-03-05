import sys
    
def dfs(n):
    global flag
    if n == len(blank):
        flag = False
        for line in sudoku:
            print(*line)
        return
    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]
        if check_row(x, i) and check_col(y, i) and check_square(x, y, i) and flag:
            sudoku[x][y] = i
            dfs(n + 1)
            sudoku[x][y] = 0

def check_row(x, n):
    if n in sudoku[x]:
        return False
    return True

def check_col(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

def check_square(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if sudoku[i][j] == n:
                return False
    return True

sudoku = [list(map(int, i.split())) for i in sys.stdin.readlines()]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])
flag = True
dfs(0)