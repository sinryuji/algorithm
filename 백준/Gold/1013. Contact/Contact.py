import sys, re

input = sys.stdin.readline

T = int(input())

p = re.compile("(100+1+|01)+")
for _ in range(T):
    if p.fullmatch(input().rstrip()):
        print("YES")
    else:
        print("NO")