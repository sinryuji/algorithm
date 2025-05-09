import sys
from collections import deque

input = sys.stdin.readline


def turn(n, d, left, right):
    if n < 0 or n > 3:
        return
    if left and n > 0 and gears[n][6] != gears[n - 1][2]:
        left = True
    else:
        left = False
    if right and n < 3 and gears[n][2] != gears[n + 1][6]:
        right = True
    else:
        right = False

    gear = gears[n]
    if d == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())
    gears[n] = gear

    if left:
        turn(n - 1, d * -1, True, False)
    if right:
        turn(n + 1, d * -1, False, True)


gears = list(deque(map(int, input().rstrip())) for _ in range(4))
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    turn(n - 1, d, True, True)

ret = 0
for i in range(4):
    ret += gears[i][0] * 2 ** i

print(ret)
