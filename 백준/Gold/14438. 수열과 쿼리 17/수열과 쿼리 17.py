import sys

input = sys.stdin.readline


def init(s, e, i):
    if s == e:
        tree[i] = arr[s]
        return tree[i]
    m = (s + e) // 2
    tree[i] = min(init(s, m, i * 2), init(m + 1, e, i * 2 + 1))
    return tree[i]


def find(s, e, i, l, r):
    if l > e or r < s:
        return float('inf')
    if l <= s and r >= e:
        return tree[i]
    m = (s + e) // 2
    return min(find(s, m, i * 2, l, r), find(m + 1, e, i * 2 + 1, l, r))


def update(s, e, i, t, v):
    if t < s or t > e:
        return
    if s == e:
        arr[t] = v
        tree[i] = v
        return
    m = (s + e) // 2
    update(s, m, i * 2, t, v)
    update(m + 1, e, i * 2 + 1, t, v)
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])


N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (N * 4)
init(0, N - 1, 1)
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))
