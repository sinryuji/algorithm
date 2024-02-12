import sys
input = sys.stdin.readline

N = int(input())
nums = []
ans = dict()
max_num = 0

for i, num in enumerate([*map(int, input().split())]):
    max_num = max(max_num, num)
    nums.append((i, num))
    ans[num] = 0

nums.sort(key=lambda x : x[1])

for i in range(N):
    pos, num = nums[i]
    for target in range(num*2, max_num+1, num):
        if target in ans:
            ans[num] += 1
            ans[target] -= 1

for value in ans.values():
    print(value, end=' ')