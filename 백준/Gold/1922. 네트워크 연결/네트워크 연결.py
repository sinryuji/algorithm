import sys

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]

answer = 0
for a, b, dist in edges:
    if find(a) != find(b):
        union(a, b)
        answer += dist

print(answer)