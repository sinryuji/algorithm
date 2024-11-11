import sys

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

parent = [i for i in range(N + 1)]

answer = sum(edge[2] for edge in edges)
for a, b, dist in edges:
    if find(a) != find(b):
        union(a, b)
        answer -= dist

print(answer)
