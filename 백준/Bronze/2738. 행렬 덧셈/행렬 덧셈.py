n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    ret = [x + y for x, y in zip(a[i], b[i])]
    print(*ret)