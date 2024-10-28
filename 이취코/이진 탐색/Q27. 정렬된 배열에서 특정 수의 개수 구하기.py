import sys

input = sys.stdin.readline


def binary_left(arr, target):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_right(arr, target):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


N, x = map(int, input().split())
nums = list(map(int, input().split()))

left = binary_left(nums, x)
if 0 <= left < N and nums[left] == x:
    print(binary_right(nums, x) - left + 1)
else:
    print(-1)
