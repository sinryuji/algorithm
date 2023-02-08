n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    ret = [x + y for x, y in zip(a[i], b[i])]
    for j in ret:
        print(j, end = ' ')
    print()