import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]


T = int(input())
for _ in range(T):
    F = int(input())
    parent = dict()
    cnt = dict()

    for _ in range(F):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1

        union(a, b)
        print(cnt[find(a)])
