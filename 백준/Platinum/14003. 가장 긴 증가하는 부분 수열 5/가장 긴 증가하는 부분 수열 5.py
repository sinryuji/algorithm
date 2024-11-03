import sys
from bisect import bisect_left

input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))
s = [nums[0]]
dp = [(0, nums[0])]

for i in nums[1:]:
    if i > s[-1]:
        s.append(i)
        dp.append((len(s) - 1, i))
    else:
        idx = bisect_left(s, i)
        s[idx] = i
        dp.append((idx, i))

last = len(s) - 1
answer = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last:
        answer.append(dp[i][1])
        last -= 1

print(len(answer))
print(*answer[::-1])
