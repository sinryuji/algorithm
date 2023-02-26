import sys

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline())
nums = sorted([int(i) for i in sys.stdin.readlines()])
re_nums = []

for i in range(1, n):
    re_nums.append(nums[i] - nums[i - 1])

gcd = re_nums[0]
for i in range(1, len(re_nums)):
    gcd = get_gcd(gcd, re_nums[i])
    
ret = set()
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        ret.add(i)
        ret.add(gcd // i)
ret.add(gcd)
print(*sorted(list(ret)))