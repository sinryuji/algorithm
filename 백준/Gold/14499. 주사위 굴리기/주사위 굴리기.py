import sys

input = sys.stdin.readline

def turn(di):
    if di == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif di == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif di == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]

N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

dice = [0] * 6
d = [(), (1, 0), (-1, 0), (0, -1), (0, 1)]
for cmd in cmds:
    nx, ny = x + d[cmd][0], y + d[cmd][1]
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

    x, y = nx, ny
    turn(cmd)

    if board[y][x] == 0:
        board[y][x] = dice[-1]
    else:
        dice[-1] = board[y][x]
        board[y][x] = 0

    print(dice[0])
