import sys
from bisect import bisect_left

input = sys.stdin.readline

def lis(data):
    arr = [data[0]]
    for i in data[1:]:
        if arr[-1] < i:
            arr.append(i)
        else:
            arr[bisect_left(arr, i)] = i

    return len(arr)


n = int(input())
nums = list(map(int, input().split()))

print(lis(nums))
