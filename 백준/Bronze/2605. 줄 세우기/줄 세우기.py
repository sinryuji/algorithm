import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = []
for i in range(n):
    answer.insert(i - nums[i], i+1)

print(*answer)