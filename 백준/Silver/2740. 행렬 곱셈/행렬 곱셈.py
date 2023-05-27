n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ret = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            ret[x][y] += a[x][z] * b[z][y]

for i in range(n):
    print(*ret[i], sep = ' ')