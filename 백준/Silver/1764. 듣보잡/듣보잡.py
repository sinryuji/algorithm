import sys

n, m = map(int, sys.stdin.readline().split())
notheard = set()
notseen = set()
for _ in range(n):
    notheard.add(sys.stdin.readline().rstrip())
for _ in range(m):
    notseen.add(sys.stdin.readline().rstrip())
ret = sorted(notheard & notseen)
print(len(ret))
print(*ret, sep = '\n')