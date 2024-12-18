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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tree = [0] * (N + 1)

d = dict()
for i, v in enumerate(A):
    d[v] = i + 1

answer = 0
for i in B[::-1]:
    idx = d[i]
    answer += prefix_sum(idx)
    update(idx)

print(answer)
