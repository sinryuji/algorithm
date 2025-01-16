import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
deq = deque((i + 1, v) for i, v in enumerate(arr))

answer = []
while True:
    i, v = deq.popleft()
    answer.append(i)
    if not deq:
        break
    if v > 0:
        for _ in range(v-1):
            deq.append(deq.popleft())
    else:
        for _ in range(-v):
            deq.appendleft(deq.pop())

print(*answer)
