import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted([int(input()) for _ in range(N)])

answer = sys.maxsize
left, right = 0, 0
while right < N:
    diff = nums[right] - nums[left]
    if diff < M:
        right += 1
    elif diff > M:
        answer = min(answer, diff)
        left += 1
    else:
        answer = diff
        break

print(answer)