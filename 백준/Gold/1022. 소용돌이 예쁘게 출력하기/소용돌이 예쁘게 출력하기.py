r1, c1, r2, c2 = map(int, input().split())

board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
x, y = 0, 0
n = 1
l = 1

di = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0

while total > 0:
    for _ in range(2):
        for _ in range(l):
            if c1 <= x <= c2 and r1 <= y <= r2:
                board[y - r1][x - c1] = n
                total -= 1
                m = n
            x += di[d][0]
            y += di[d][1]
            n += 1
        d = (d + 1) % 4
    l += 1

max_len = len(str(m))
for y in range(r2 - r1 + 1):
    for x in range(c2 - c1 + 1):
        print(str(board[y][x]).rjust(max_len), end = ' ')
    print()