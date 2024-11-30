import sys


def init(start, end, index):
    global mod
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1) % mod
    return tree[index]


def find(start, end, index, left, right):
    global mod
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return find(start, mid, index * 2, left, right) * find(mid + 1, end, index * 2 + 1, left, right) % mod


def update(start, end, index, target, value):
    global mod
    if target < start or target > end:
        return

    if start == end:
        arr[target] = value
        tree[index] = value
        return

    mid = (start + end) // 2
    update(start, mid, index * 2, target, value)
    update(mid + 1, end, index * 2 + 1, target, value)

    tree[index] = tree[index * 2] * tree[index * 2 + 1] % mod


input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)
mod = 1000000007
init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))
