import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(map(int, input().split()))

ret = 0
zero_cnt = 0
robots = deque([False] * 2 * N)
while zero_cnt < K:
    ret += 1

    arr.rotate(1)
    robots.rotate(1)

    robots[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and arr[i + 1] > 0:
            robots[i], robots[i + 1] = False, True
            arr[i + 1] -= 1
            if arr[i + 1] == 0:
                zero_cnt += 1

    robots[N - 1] = False

    if arr[0] > 0 and not robots[0]:
        arr[0] -= 1
        robots[0] = True
        if arr[0] == 0:
            zero_cnt += 1

print(ret)