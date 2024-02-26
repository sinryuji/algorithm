import sys

input = sys.stdin.readline


def solve():
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(N + 1)]
    sum_ = 0
    max_ = 0
    count = 0

    for a, b, dist in edges:
        a, b = find(a), find(b)
        if a != b:
            if a < b:
                parent[a] = b
            else:
                parent[b] = a
            sum_ += dist
            max_ = dist

    print(sum_ - max_)


if __name__ == '__main__':
    solve()
