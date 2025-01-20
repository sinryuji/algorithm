import sys

input = sys.stdin.readline

n = int(input())
seq = sorted(map(int, input().split()))
x = int(input())

left, right = 0, n - 1
answer = 0
while left < right:
    s = seq[left] + seq[right]
    if s > x:
        right -= 1
    elif s < x:
        left += 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)
