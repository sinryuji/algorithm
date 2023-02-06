m, n = map(int, input().split())

n += 1
a = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        for j in range(i * 2, n, i):
            a[j] = False
for i in range(m, n):
    if i > 1 and a[i]:
        print(i)