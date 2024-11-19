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


def lis(data):
    arr = [data[0]]
    for i in data[1:]:
        if arr[-1] < i:
            arr.append(i)
        else:
            arr[binary_search(arr, i)] = i

    return len(arr)


n = int(input())
nums = list(map(int, input().split()))

print(lis(nums))
