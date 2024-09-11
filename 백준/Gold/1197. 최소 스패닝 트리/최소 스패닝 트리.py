import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


V, E = map(int, input().split())
edges = []

for _ in range(E):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(V + 1)]

answer = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)