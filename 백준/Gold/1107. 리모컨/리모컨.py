import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
brokens = list(map(int, input().split()))

min_count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)):
        if int(nums[i]) in brokens:
            break
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - N) + len(nums))

print(min_count)