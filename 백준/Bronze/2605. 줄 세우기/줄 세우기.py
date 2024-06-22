import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = []
for i in range(1, n + 1):
    answer.insert(len(answer) - nums[i-1], i)

print(*answer)