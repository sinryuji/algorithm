import sys
from collections import Counter

input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

print(sum(nums) // 10)
print(sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[0][0])