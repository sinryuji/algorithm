import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


def init_min(start, end, index):
    if start == end:
        min_tree[index] = arr[start]
        return min_tree[index]

    mid = (start + end) // 2
    min_tree[index] = min(init_min(start, mid, index * 2), init_min(mid + 1, end, index * 2 + 1))
    return min_tree[index]


def init_max(start, end, index):
    if start == end:
        max_tree[index] = arr[start]
        return max_tree[index]
    mid = (start + end) // 2
    max_tree[index] = max(init_max(start, mid, index * 2), init_max(mid + 1, end, index * 2 + 1))
    return max_tree[index]


def find_min(start, end, index, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return min_tree[index]
    mid = (start + end) // 2
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))


def find_max(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[index]
    mid = (start + end) // 2
    return max(find_max(start, mid, index * 2, left, right), find_max(mid + 1, end, index * 2 + 1, left, right))


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
min_tree = [0] * (N * 4)
max_tree = [0] * (N * 4)
init_min(0, N - 1, 1)
init_max(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(find_min(0, N - 1, 1, a - 1, b - 1), find_max(0, N - 1, 1, a - 1, b - 1))
