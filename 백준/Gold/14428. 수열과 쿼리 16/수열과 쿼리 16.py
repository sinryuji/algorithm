import sys

input = sys.stdin.readline


def init(start, end, idx):
    if start == end:
        tree[idx] = [arr[start], start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))
    return tree[idx]


def find(start, end, idx, left, right):
    if left > end or right < start:
        return [float('inf'), 0]
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return min(find(start, mid, idx * 2, left, right), find(mid + 1, end, idx * 2 + 1, left, right))


def update(start, end, idx, target, value):
    if target < start or target > end:
        return
    if start == end:
        arr[target] = value
        tree[idx][0] = value
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, target, value)
    update(mid + 1, end, idx * 2 + 1, target, value)
    tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])


N = int(input())
arr = list(map(int, input().split()))
tree = [[0, 0] for _ in range(N * 4)]
init(0, N - 1, 1)
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    else:
        print(find(0, N - 1, 1, b - 1, c - 1)[1] + 1)
