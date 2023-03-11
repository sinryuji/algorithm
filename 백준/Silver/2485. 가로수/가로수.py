import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline())
trees = [int(i) for i in sys.stdin.readlines()]
gap = [trees[i + 1] - trees[i] for i in range(len(trees) - 1)]
x = gcd(gap[0], gap[1])
for i in range(2, len(gap)):
    x = gcd(x, gap[2])
print((trees[-1] - trees[0]) // x + 1 - len(trees))