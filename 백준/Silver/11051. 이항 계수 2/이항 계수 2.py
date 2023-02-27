def factorial(n):
    ret = 1
    while n > 1:
        ret *= n
        n -= 1
    return ret

n, k = map(int, input().split())
print((factorial(n) // (factorial(k) * factorial(n - k))) % 10007)