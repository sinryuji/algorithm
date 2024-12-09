import sys

input = sys.stdin.readline


def update(start, end, index, target, diff):
    tree[index] += diff
    if start == end:
        return
    mid = (start + end) // 2
    if target <= mid:
        update(start, mid, index * 2, target, diff)
    else:
        update(mid + 1, end, index * 2 + 1, target, diff)

def find(start, end, index, target):
    tree[index] -= 1
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[index * 2] >= target:
        return find(start, mid, index * 2, target)
    else:
        return find(mid + 1, end, index * 2 + 1, target - tree[index * 2])


n = int(input())
N = 10 ** 6
tree = [0] * (N * 4)
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0] == 1:
        print(find(0, N, 1, data[1]))
    else:
        b, c = data[1], data[2]
        update(0, N, 1, b, c)
