import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()

for _ in range(n):
    addr, pwd = input().split()
    d[addr] = pwd
for _ in range(m):
    print(d[input().rstrip()])