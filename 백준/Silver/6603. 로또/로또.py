import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 0:
        break
    k = nums[0]
    nums = nums[1:]
    for c in combinations(nums, 6):
        print(*c)
    print()