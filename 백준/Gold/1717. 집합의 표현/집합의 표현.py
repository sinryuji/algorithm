import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")