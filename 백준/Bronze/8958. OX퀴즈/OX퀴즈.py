import sys

n = int(input())
for _ in range(n):
    l = sys.stdin.readline().rstrip().split('X')
    s = 0
    for i in range(len(l)):
        s += sum(range(len(l[i]) + 1))
    print(s)