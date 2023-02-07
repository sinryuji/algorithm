while True:
    n = int(input())
    if n == 0:
        break
    m = 2 * n + 1
    l = [True] * m
    for i in range(2, int(m ** 0.5) + 1):
        if l[i]:
            for j in range(i * 2, m, i):
                l[j] = False
    cnt = 0
    for i in range(n + 1, m):
        if i > 1 and l[i]:
            cnt += 1
    print(cnt)