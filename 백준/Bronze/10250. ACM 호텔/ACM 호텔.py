t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h
    if a == 0:
        a = h
        b -= 1
    print((a * 100) + (b + 1))