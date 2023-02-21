n, m = map(int, input().split())
basket = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    while i < j:
        tmp = basket[i]
        basket[i] = basket[j]
        basket[j] = tmp
        i += 1
        j -= 1
print(*basket[1:])