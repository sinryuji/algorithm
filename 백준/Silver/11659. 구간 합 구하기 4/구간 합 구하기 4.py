import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
sum = 0
for i in range(n):
    sum += nums[i]
    prefix_sum[i + 1] = sum

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])