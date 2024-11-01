import sys

input = sys.stdin.readline


def bs(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return left


N = int(input())
arr = list(map(int, input().split()))
s = [arr[0]]

for i in arr[1:]:
    if i < s[-1]:
        s.append(i)
    else:
        s[bs(s, i)] = i

print(N - len(s))
