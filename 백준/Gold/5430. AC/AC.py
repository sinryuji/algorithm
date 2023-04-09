import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    flag = True
    rev = False
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip().strip('[]').split(','))
    if arr[0] == '':
        arr.pop()
    for i in p:
        if i == 'R':
            rev = not rev
        else:
            if len(arr) == 0:
                print('error')
                flag = False
                break
            if not rev:
                arr.popleft()
            else:
                arr.pop()
    if flag:
        if rev:
            arr.reverse()
        print('[', ','.join(arr), ']', sep = '')