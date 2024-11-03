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
dp = [(0, nums[0])]

for i in nums[1:]:
    if i > s[-1]:
        s.append(i)
        dp.append((len(s) - 1, i))
    else:
        idx = binary_search(s, i)
        s[idx] = i
        dp.append((idx, i))

last = len(s) - 1
answer = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last:
        answer.append(dp[i][1])
        last -= 1

print(len(answer))
print(*answer[::-1])
