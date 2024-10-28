import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, N - 1
find = False
answer = 0
while left <= right:
    mid = (left + right) // 2
    if nums[mid] > mid:
        right = mid - 1
    elif nums[mid] < mid:
        left = mid + 1
    else:
        find = True
        answer = mid
        break

if find:
    print(answer)
else:
    print(-1)
