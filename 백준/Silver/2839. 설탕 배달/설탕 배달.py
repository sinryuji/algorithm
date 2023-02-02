n = int(input())

a = 0
while n % 5 != 0 and n > 0:
    n -= 3
    a += 1
if n % 5 != 0:
    print(-1)
else:
    print(n // 5 + a)