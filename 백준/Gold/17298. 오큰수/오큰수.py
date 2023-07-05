import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = [0]
answer = [-1] * n

for i in range(1, n):
    while s and nums[i] > nums[s[-1]]:
        answer[s.pop()] = nums[i]
    s.append(i)

print(*answer)