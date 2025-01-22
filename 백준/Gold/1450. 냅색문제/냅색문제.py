import sys
from itertools import combinations
from bisect import bisect_right

input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

arr_left = arr[:N // 2]
arr_right = arr[N // 2:]

sum_left = []
sum_right = []

for i in range(len(arr_left) + 1):
    for comb in combinations(arr_left, i):
        sum_left.append(sum(comb))

for i in range(len(arr_right) + 1):
    for comb in combinations(arr_right, i):
        sum_right.append(sum(comb))

sum_left.sort()
answer = 0
for s in sum_right:
    if s > C:
        continue
    answer += bisect_right(sum_left, C - s)

print(answer)
