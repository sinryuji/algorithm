def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
rings = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(rings[0], rings[i])
    print(rings[0] // g, rings[i] // g, sep = "/")