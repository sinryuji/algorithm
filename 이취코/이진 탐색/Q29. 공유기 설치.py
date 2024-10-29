# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

left = 1
right = houses[-1] - houses[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    cur = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= cur + mid:
            cur = houses[i]
            cnt += 1

    if cnt >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
