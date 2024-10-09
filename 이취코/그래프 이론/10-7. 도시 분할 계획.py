import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]

answer = 0
last = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        last = c
answer -= last

print(answer)