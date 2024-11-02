import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

s = [nums[0]]
for i in nums[1:]:
    if i > s[-1]:
        s.append(i)
    else:
        s[bisect_left(s, i)] = i

print(len(s))
