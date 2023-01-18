import sys

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline()))
max = max(nums)
print(max)
print(nums.index(max) + 1)