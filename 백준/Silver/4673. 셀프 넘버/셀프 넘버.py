def solve(num):
    for n in str(num):
        num += int(n)
    return num
    
nums = set(range(1, 10000))
remove = set()
for num in nums:
    remove.add(solve(num))
ret = nums - remove
for i in sorted(ret):
    print(i)