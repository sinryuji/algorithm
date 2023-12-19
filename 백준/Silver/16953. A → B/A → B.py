from collections import deque

A, B = map(int, input().split())
cnt = 1
queue = deque([[A, cnt]])
flag = False

while queue:
    n, cnt = queue.popleft()
    if n == B:
        flag = True
        print(cnt)
        break
    mul = n * 2
    one = n * 10 + 1
    if mul <= B:
        queue.append([mul, cnt + 1])
    if one <= B:
        queue.append([one, cnt + 1])

if not flag:
    print(-1)