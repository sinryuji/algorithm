import sys

input = sys.stdin.readline


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


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
        idx = binary_search(arr, i)
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
