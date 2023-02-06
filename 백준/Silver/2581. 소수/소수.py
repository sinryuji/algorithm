m = int(input())
n = int(input())

n += 1
a = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        for j in range(i * 2, n, i):
            a[j] = False
sum = 0
for i in range(m, n):
    if i > 1 and a[i]:
        sum += i
if sum == 0:
    print(-1)
else:
    print(sum)
    for i in range(m, n):
        if i > 1 and a[i]:
            print(i)
            break