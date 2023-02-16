import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline())
strs = []
for _ in range(m):
    strs.append(sys.stdin.readline())
cnt = 0
for i in strs:
    if i in s:
        cnt += 1
print(cnt)