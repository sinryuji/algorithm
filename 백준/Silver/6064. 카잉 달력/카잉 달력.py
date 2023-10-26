import sys
input = sys.stdin.readline

def calculate(m, n, x, y):
    while x <= m * n:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(calculate(M, N, x, y))