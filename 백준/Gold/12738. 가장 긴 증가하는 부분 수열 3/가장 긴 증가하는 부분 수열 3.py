import sys

input = sys.stdin.readline


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


N = int(input())
nums = list(map(int, input().split()))

s = [nums[0]]
for i in nums[1:]:
    if i > s[-1]:
        s.append(i)
    else:
        s[binary_search(s, i)] = i

print(len(s))
