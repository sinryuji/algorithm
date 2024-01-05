import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_sum = arr
min_sum = arr

for _ in range(N - 1):
    arr = list(map(int, input().split()))
    max_sum = [arr[0] + max(max_sum[0], max_sum[1]), arr[1] + max(max_sum), arr[2] + max(max_sum[1], max_sum[2])]
    min_sum = [arr[0] + min(min_sum[0], min_sum[1]), arr[1] + min(min_sum), arr[2] + min(min_sum[1], min_sum[2])]

print(max(max_sum), min(min_sum))