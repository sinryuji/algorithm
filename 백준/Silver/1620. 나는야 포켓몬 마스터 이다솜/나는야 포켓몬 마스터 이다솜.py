import sys

n, m = map(int, sys.stdin.readline().split())
d = dict()
for i in range(1, n + 1):
    input = sys.stdin.readline().rstrip()
    d[str(i)] = input
    d[input] = str(i)
for _ in range(m):
    print(d[sys.stdin.readline().rstrip()])