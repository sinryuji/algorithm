import sys

k, n = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readlines()))

start, end = 1, max(l)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in l:
        cnt += i // mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)