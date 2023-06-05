import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
s = [nums[0]]

for i in nums[1:]:
    if s[-1] < i:
        s.append(i)
    else:
        s[bisect_left(s, i)] = i
        
print(len(s))