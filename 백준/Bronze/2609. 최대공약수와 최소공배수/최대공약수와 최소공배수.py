def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
md = gcd(a, b)
print(md)
print(a * b // md)