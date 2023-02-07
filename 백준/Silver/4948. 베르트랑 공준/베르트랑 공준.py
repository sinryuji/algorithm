def getPrimeList(n):
    n += 1
    l = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if l[i]:
            for j in range(i * 2, n, i):
                l[j] = False
    return l

primeList = getPrimeList(123456 * 2)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        if i > 1 and primeList[i]:
            cnt += 1
    print(cnt)