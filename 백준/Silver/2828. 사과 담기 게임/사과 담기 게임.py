import sys

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

s, e = 1, M
ans = 0
for _ in range(J):
    loc = int(input())
    if s <= loc <= e:
        continue
    else:
        if loc < s:
            move = s - loc
            s -= move
            e -= move
            ans += move
        elif e < loc:
            move = loc - e
            s += move
            e += move
            ans += move

print(ans)