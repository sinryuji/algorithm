for _ in range(int(input())):
    input()
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    answer = 0
    for y in range(r):
        for x in range(c):
            if board[y][x] == '>':
                if x + 2 < c:
                    if ''.join(board[y][x:x + 3]) == '>o<':
                        answer += 1
            if board[y][x] == 'v':
                if y + 2 < r:
                    if board[y][x] + board[y+1][x] + board[y+2][x] == 'vo^':
                        answer += 1

    print(answer)
