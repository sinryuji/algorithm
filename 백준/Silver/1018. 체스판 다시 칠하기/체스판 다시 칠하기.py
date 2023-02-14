import sys

n, m = map(int, sys.stdin.readline().split())
chess = [i.rstrip() for i in sys.stdin.readlines()]
ret = []

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if chess[x][y] == 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if chess[x][y] == 'W':
                        b += 1
                    else:
                        w += 1
        ret.append(min(w, b))
print(min(ret))