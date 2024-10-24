import sys, copy
from itertools import combinations

input = sys.stdin.readline


def bfs():
    for x, y in teachers:
        for dx, dy in di:
            nx, ny = x, y
            while 0 <= nx + dx < N and 0 <= ny + dy < N:
                nx += dx
                ny += dy
                if board[ny][nx] == 'O':
                    break
                if board[ny][nx] == 'S':
                    return False
    return True


N = int(input())
board = []
space = []
teachers = []

for y in range(N):
    row = list(input().rstrip().split())
    for x in range(N):
        if row[x] == 'X':
            space.append((x, y))
        if row[x] == 'T':
            teachers.append((x, y))
    board.append(row)

combi = combinations(space, 3)
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for c in combi:
    for x, y in c:
        board[y][x] = 'O'

    if bfs():
        print("YES")
        exit()

    for x, y in c:
        board[y][x] = 'X'

print("NO")
