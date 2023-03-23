nums = sorted(list(map(int, input().split())))
print(nums[1] + nums[0] + min(nums[2], nums[1] + nums[0] - 1))