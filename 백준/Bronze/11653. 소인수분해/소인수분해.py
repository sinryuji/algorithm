n = int(input())

while n > 1:
    x = 2
    while n % x != 0:
        x += 1
        if x == n:
            break
    print(x)
    n = n / x