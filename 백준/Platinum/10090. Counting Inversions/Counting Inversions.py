import sys

input = sys.stdin.readline


def prefix_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


def update(i):
    while i <= N:
        tree[i] += 1
        i += i & -i


N = int(input())
nums = list(map(int, input().split()))
arr = sorted([(-v, i+1) for i, v in enumerate(nums)])
tree = [0] * (N + 1)

answer = 0
for v, i in arr:
    answer += prefix_sum(i)
    update(i)

print(answer)
