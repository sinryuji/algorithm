import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ret = 0
    imp = deque([int(i) for i in input().split()])
    while imp:
        imp_max = max(imp)
        front = imp.popleft()
        m -= 1
        
        if imp_max == front:
            ret += 1
            if m < 0:
                print(ret)
                break
        else:
            imp.append(front)
            if m < 0:
                m = len(imp) - 1