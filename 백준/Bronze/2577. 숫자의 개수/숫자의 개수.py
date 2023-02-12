import sys, math

ret = str(math.prod(list(map(int, sys.stdin.readlines()))))
arr = [0] * 10
for i in ret:
    arr[int(i)] += 1
print(*arr, sep = '\n')