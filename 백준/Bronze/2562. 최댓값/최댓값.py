nums = [int(input()) for _ in range(9)]
max = max(nums)
print(f"{max}\n{nums.index(max) + 1}")