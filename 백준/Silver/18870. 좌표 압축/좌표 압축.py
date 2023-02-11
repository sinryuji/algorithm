import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sortedArr = sorted(list(set(arr)))
dict = {sortedArr[i] : i for i in range(len(sortedArr))}
for i in arr:
    print(dict[i], end = ' ')