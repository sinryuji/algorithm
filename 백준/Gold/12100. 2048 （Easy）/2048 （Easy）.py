import sys, copy

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def move_right(board):
    for y in range(N):
        target = N - 1
        for x in range(N - 1, -1, -1):
            if board[y][x] == 0:
                continue
            tmp = board[y][x]
            board[y][x] = 0
            if board[y][target] == 0:
                board[y][target] = tmp
            elif board[y][target] == tmp:
                board[y][target] *= 2
                target -= 1
            else:
                target -= 1
                board[y][target] = tmp
    return board


def move_left(board):
    for y in range(N):
        target = 0
        for x in range(1, N):
            if board[y][x] == 0:
                continue
            tmp = board[y][x]
            board[y][x] = 0
            if board[y][target] == 0:
                board[y][target] = tmp
            elif board[y][target] == tmp:
                board[y][target] *= 2
                target += 1
            else:
                target += 1
                board[y][target] = tmp
    return board


def move_up(board):
    for x in range(N):
        target = 0
        for y in range(N):
            if board[y][x] == 0:
                continue
            tmp = board[y][x]
            board[y][x] = 0
            if board[target][x] == 0:
                board[target][x] = tmp
            elif board[target][x] == tmp:
                board[target][x] *= 2
                target += 1
            else:
                target += 1
                board[target][x] = tmp
    return board


def move_down(board):
    for x in range(N):
        target = N - 1
        for y in range(N - 1, -1, -1):
            if board[y][x] == 0:
                continue
            tmp = board[y][x]
            board[y][x] = 0
            if board[target][x] == 0:
                board[target][x] = tmp
            elif board[target][x] == tmp:
                board[target][x] *= 2
                target -= 1
            else:
                target -= 1
                board[target][x] = tmp
    return board


def dfs(arr, cnt):
    global answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > answer:
                    answer = arr[i][j]
        return

    dfs(move_right(copy.deepcopy(arr)), cnt + 1)
    dfs(move_left(copy.deepcopy(arr)), cnt + 1)
    dfs(move_up(copy.deepcopy(arr)), cnt + 1)
    dfs(move_down(copy.deepcopy(arr)), cnt + 1)


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(pan, 0)

print(answer)