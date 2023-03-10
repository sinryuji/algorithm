a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
gcd, x = a1 * b2 + b1 * a2, a2 * b2
while x > 0:
    gcd, x = x, gcd % x
print((a1 * b2 + b1 * a2) // gcd, a2 * b2 // gcd)