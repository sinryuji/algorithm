import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
d1 = dict()
d2 = dict()
for _ in range(n):
    x, y = map(int, input().split())
    d1[x] = y
    d2[y] = x

data = [i[1] for i in sorted(d1.items())]

arr = [data[0]]
dp = [(0, arr[0])]
for i in data[1:]:
    if arr[-1] < i:
        dp.append((len(arr), i))
        arr.append(i)
    else:
        idx = bisect_left(arr, i)
        arr[idx] = i
        dp.append((idx, i))

l = len(arr)
print(n - l)
l -= 1
lis = []
for i, v in dp[::-1]:
    if i == l:
        lis.append(v)
        l -= 1
lis = lis[::-1]

print(*sorted(d2[i] for i in set(data) - set(lis)), sep='\n')
