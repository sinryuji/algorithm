import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))[::-1]

stack = []
cur = 1
while nums:
    if nums[-1] == cur:
        nums.pop()
        cur += 1
    elif stack and stack[-1] == cur:
        stack.pop()
        cur += 1
    else:
        stack.append(nums.pop())

while stack:
    if stack[-1] == cur:
        stack.pop()
        cur += 1
    else:
        break

if stack:
    print('Sad')
else:
    print('Nice')
