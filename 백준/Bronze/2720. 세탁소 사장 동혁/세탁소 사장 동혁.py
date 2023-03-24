import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = int(input())
    ret = []
    ret.append(c // 25)
    c %= 25
    ret.append(c // 10)
    c %= 10
    ret.append(c // 5)
    c %= 5
    ret.append(c // 1)
    print(*ret)