N = int(input())
nums = list(map(int, input().split()))
answer = [0] * N

for i, x in enumerate(nums):
    y = x
    while answer[:y].count(0) != x:
        y += 1
    while answer[y] != 0:
        y += 1
    answer[y] = i + 1

print(*answer)