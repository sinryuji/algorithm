def getPrimeList(n):
    n += 1
    l = [True] * n
    l[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if l[i]:
            for j in range(i * 2, n, i):
                l[j] = False
    return l

primeList = getPrimeList(10000)

for _ in range(int(input())):
    n = int(input())
    a, b = n // 2, n // 2
    while a > 0:
        if primeList[a] and primeList[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1