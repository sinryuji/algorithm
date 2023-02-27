def factorial(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))