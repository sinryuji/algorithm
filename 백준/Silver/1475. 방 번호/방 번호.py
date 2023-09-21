n = list(map(int, list(input())))
nums = [0] * 10
answer = 0

for i in n:
    nums[i] += 1

sn = nums[6] + nums[9]
if sn % 2 != 0:
    sn += 1
sn //= 2
nums[6] = sn
nums[9] = sn
    
print(max(nums))