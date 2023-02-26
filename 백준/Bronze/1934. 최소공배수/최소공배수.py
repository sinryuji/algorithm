def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))