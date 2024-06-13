import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
S = int(input())

for i in range(N):
    max_num = max(nums[i: min(N, i + S + 1)])
    idx = nums.index(max_num)

    for j in range(idx, i, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]

    S -= idx - i
    if S <= 0:
        break

print(*nums)