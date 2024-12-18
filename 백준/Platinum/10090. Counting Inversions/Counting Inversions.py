import sys

input = sys.stdin.readline


def query(l, r):
    s = 0
    while l < r:
        if l % 2:
            s += tree[l]
            l += 1
        if r % 2:
            r -= 1
            s += tree[r]
        l //= 2
        r //= 2
    return s


def update(idx, val):
    tree[idx] += val
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


n = int(input())
seq = list(map(int, input().split()))
size = 1 << (n - 1).bit_length()
tree = [0] * (size * 2)
arr = [(val, i) for i, val in enumerate(seq)]
arr.sort(reverse=True)

answer = 0
for val, i in arr:
    answer += query(size, i + size)
    update(i + size, 1)

print(answer)
