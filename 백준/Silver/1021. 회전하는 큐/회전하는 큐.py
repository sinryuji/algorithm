from collections import deque

n, m = map(int, input().split())
d = deque(i for i in range(1, n + 1))
cnt = 0
for i in list(map(int, input().split())):
    while d[0] != i:
        if d.index(i) <= len(d) // 2:
            d.append(d.popleft())
        else:
            d.appendleft(d.pop())
        cnt += 1
    d.popleft()
print(cnt)