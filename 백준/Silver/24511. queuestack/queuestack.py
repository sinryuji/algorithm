import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
qs = list(map(int, input().split()))
q = deque()
for i, v in enumerate(map(int, input().split())):
    if qs[i] == 0:
        q.append(v)
M = int(input())
for i in map(int, input().split()):
    q.appendleft(i)
    print(q.pop(), end=' ')
